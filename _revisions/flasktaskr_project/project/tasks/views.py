# /project/tasks/views.py

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from forms import AddTaskForm
from project import db
from project.views import login_required
from project.models import Task


################
#### config ####
################

tasks_blueprint = Blueprint(
    'tasks', __name__,
    url_prefix='/tasks',
    template_folder='templates',
    static_folder='static'
)


################
#### routes ####
################

@tasks_blueprint.route('/tasks/')
@login_required
def tasks():
    open_tasks = db.session.query(Task) \
        .filter_by(status='1').order_by(Task.due_date.asc())
    closed_tasks = db.session.query(Task) \
        .filter_by(status='0').order_by(Task.due_date.asc())
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks,
        closed_tasks=closed_tasks,
        username=session['name']
    )


# Add new tasks:
@tasks_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task():
    import datetime
    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                datetime.datetime.utcnow(),
                '1',
                session['user_id']
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks.tasks'))
        else:
            return render_template('tasks.html', form=form, error=error)


# Mark tasks as complete:
@tasks_blueprint.route('/complete/<int:task_id>/',)
@login_required
def complete(task_id):
    new_id = task_id
    task = db.session.query(Task).filter_by(task_id=new_id)
    if session['user_id'] == task.first().user_id or session['role'] == "admin":
        task.update({"status": "0"})
        db.session.commit()
        flash('The task was marked as complete. Nice.')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only update tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))


# Delete Tasks:
@tasks_blueprint.route('/delete/<int:task_id>/',)
@login_required
def delete_entry(task_id):
    new_id = task_id
    task = db.session.query(Task).filter_by(task_id=new_id)
    if session['user_id'] == task.first().user_id or session['role'] == "admin":
        task.delete()
        db.session.commit()
        flash('The task was deleted. Why not add a new one?')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only delete tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))

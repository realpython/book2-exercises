# /app/tasks/views.py


from app import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.views import login_required, flash_errors
from forms import AddTask
from app.models import FTasks

mod = Blueprint('tasks', __name__, url_prefix='/tasks',
                   template_folder='templates', static_folder='static')

@mod.route('/tasks/')
@login_required
def tasks():
   open_tasks = db.session.query(FTasks).filter_by(status='1').order_by(
                   FTasks.due_date.asc())
   closed_tasks = db.session.query(FTasks).filter_by(status='0').order_by(
                   FTasks.due_date.asc())
   return render_template('tasks/tasks.html',form = AddTask(request.form),
                           open_tasks=open_tasks, closed_tasks=closed_tasks)

@mod.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task():
   form = AddTask(request.form, csrf_enabled=False)
   if form.validate_on_submit():
       new_task = FTasks(
                   form.name.data,
                   form.due_date.data,
                   form.priority.data,
                   form.posted_date.data,
                   '1',
                   session['user_id']
                   )
       db.session.add(new_task)
       db.session.commit()
       flash('New entry was successfully posted. Thanks.')
   else:
       flash_errors(form)
   return redirect(url_for('.tasks'))

@mod.route('/complete/<int:task_id>/',)
@login_required
def complete(task_id):
   new_id = task_id
   db.session.query(FTasks).filter_by(task_id=new_id).update({"status":"0"})
   db.session.commit()
   flash('The task was marked as complete. Nice.')
   return redirect(url_for('.tasks'))

@mod.route('/delete/<int:task_id>/',)
@login_required
def delete_entry(task_id):
   new_id = task_id
   db.session.query(FTasks).filter_by(task_id=new_id).delete()
   db.session.commit()
   flash('The task was deleted. Why not add a new one?')
   return redirect(url_for('.tasks'))

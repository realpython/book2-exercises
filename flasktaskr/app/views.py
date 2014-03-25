# views.py


from app import app, db
from flask import flash, redirect, render_template, session, url_for, request, jsonify
from functools import wraps
from app.models import FTasks

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,error), 'error')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.route('/', defaults={'page': 'index'})
def index(page):
    return(redirect(url_for('users.login')))

@app.route('/api/tasks/')
def tasks():
  if request.method == 'GET':
    results = db.session.query(FTasks).limit(10).offset(0).all()
    json_results = []
    for result in results:
      data = {
            'task_id' : result.task_id,
            'task name': result.name,
            'due date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user id': result.user_id
            }
      json_results.append(data)

    return jsonify(items=json_results)

@app.route('/api/task/<int:task_id>')
def task(task_id):
  if request.method == 'GET':
    result = db.session.query(FTasks).filter_by(task_id=task_id).first()

    json_result = {
            'task_id' : result.task_id,
            'task name': result.name,
            'due date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user id': result.user_id
            }

    return jsonify(items=json_result)

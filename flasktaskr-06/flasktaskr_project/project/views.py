# project/views.py

#################
#### imports ####
#################

from project import app, db
from project.models import Task
from flask import flash, redirect, session, url_for, \
    render_template, request, jsonify, make_response
from functools import wraps
import datetime


##########################
#### helper functions ####
##########################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'error')


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

@app.route('/', defaults={'page': 'index'})
def index(page):
    return redirect(url_for('tasks.tasks'))


########################
#### error handlers ####
########################

@app.errorhandler(404)
def page_not_found(error):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n404 error at {}: {} ".format(current_timestamp, r))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n500 error at {}: {} ".format(current_timestamp, r))
    return render_template('500.html'), 500


#######################
#### API Endpoints ####
#######################

@app.route('/api/tasks/', methods=['GET'])
def tasks():
    if request.method == 'GET':
        results = db.session.query(Task).limit(10).offset(0).all()
        json_results = []
        for result in results:
            data = {
                'task_id': result.task_id,
                'task name': result.name,
                'due date': str(result.due_date),
                'priority': result.priority,
                'posted date': str(result.posted_date),
                'status': result.status,
                'user id': result.user_id
            }
            json_results.append(data)

    return jsonify(items=json_results)


@app.route('/api/tasks/<int:task_id>')
def task(task_id):
    if request.method == 'GET':
        result = db.session.query(Task).filter_by(task_id=task_id).first()
        if result:
            result = {
                'task_id': result.task_id,
                'task name': result.name,
                'due date': str(result.due_date),
                'priority': result.priority,
                'posted date': str(result.posted_date),
                'status': result.status,
                'user id': result.user_id
            }
            code = 200
        else:
            result = {"sorry": "Element does not exist"}
            code = 404
        return make_response(jsonify(result), code)

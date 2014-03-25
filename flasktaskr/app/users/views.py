# /app/users/views.py


from app import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.views import login_required, flash_errors
from forms import RegisterForm, LoginForm
from app.models import User
from sqlalchemy.exc import IntegrityError

mod = Blueprint('users', __name__, url_prefix='/users',
                    template_folder='templates', static_folder='static')

@mod.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('You are logged out. Bye. :(')
    return redirect (url_for('.login'))

@mod.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=='POST':
        u = User.query.filter_by(name=request.form['name'],
                          password=request.form['password']).first()
        if u is None:
            error = 'Invalid username or password.'
        else:
            session['logged_in'] = True
            session['user_id'] = u.id
            flash('You are logged in. Go Crazy.')
            return redirect(url_for('tasks.tasks'))

    return render_template("users/login.html",
                           form = LoginForm(request.form),
                           error = error)

@mod.route('/register/', methods=['GET','POST'])
def register():
    error = None
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(
                    form.name.data,
                    form.email.data,
                    form.password.data,
                    )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('.login'))
        except IntegrityError:
            error = 'Oh no! That username and/or email already exist. Please try again.'
    else:
        flash_errors(form)
    return render_template('/users/register.html', form=form, error=error)

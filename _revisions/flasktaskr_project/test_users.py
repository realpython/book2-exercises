# test_users.py


import os
import unittest

from project import app, db
from config import basedir
from project.models import User

TEST_DB = 'test.db'


class UsersTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ########################
    #### helper methods ####
    ########################

    def login(self, name, password):
        return self.app.post(
            '/users/',
            data=dict(
                name=name,
                password=password
            ),
            follow_redirects=True
        )

    def register(self):
        return self.app.post(
            'users/register/',
            data=dict(
                name='Fletcher',
                email='fletcher@realpython.com',
                password='python101',
                confirm='python101'
            ),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('users/logout/', follow_redirects=True)

    ###################
    #### templates ####
    ###################

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/users/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)

    def test_404_error(self):
        response = self.app.get('/this-route-does-not-exist/')
        self.assertEquals(response.status_code, 404)
        self.assertIn('Sorry. There\'s nothing here.', response.data)

    ###############
    #### views ####
    ###############

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password.', response.data)

    def test_users_can_login(self):
        self.register()
        response = self.login('Fletcher', 'python101')
        self.assertIn('Welcome!', response.data)

    def test_logged_in_users_can_logout(self):
        self.register()
        self.login('Fletcher', 'python101')
        response = self.logout()
        self.assertIn('You are logged out.', response.data)

    def test_not_logged_in_users_cannot_logout(self):
        response = self.logout()
        self.assertNotIn('You are logged out. Bye. :(', response.data)

    def test_user_registeration(self):
        self.app.get('users/register/', follow_redirects=True)
        response = self.register()
        self.assertIn('Thanks for registering. Please login.', response.data)

    ###############
    #### forms ####
    ###############

    def test_invalid_form_data(self):
        self.register()
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn('Invalid username or password.', response.data)

    def test_form_is_present_on_register_page(self):
        response = self.app.get('users/register/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please register to start a task list', response.data)

    def test_duplicate_user_registeration_throws_error(self):
        self.register()
        response = self.register()
        self.assertIn(
            'Sorry that username and/or email error already exist.',
            response.data
        )

    def test_user_registeration_field_errors(self):
        response = self.app.post(
            'users/register/',
            data=dict(
                name='Fletcher',
                email='fletcher',
                password='python101',
                confirm=''
            ),
            follow_redirects=True
        )
        self.assertIn('This field is required.', response.data)
        self.assertIn('Invalid email address.', response.data)

    def test_user_login_field_errors(self):
        response = self.app.post(
            '/users/',
            data=dict(
                name='',
                password='python101',
            ),
            follow_redirects=True
        )
        self.assertIn('This field is required.', response.data)

    ################
    #### models ####
    ################

    def test_string_reprsentation_of_the_user_object(self):

        db.session.add(
            User(
                "Johnny",
                "john@doe.com",
                "johnny"
            )
        )

        db.session.commit()

        users = db.session.query(User).all()
        for user in users:
            self.assertEquals(user.name, 'Johnny')

    def test_default_user_role(self):

        db.session.add(
            User(
                "Johnny",
                "john@doe.com",
                "johnny"
            )
        )

        db.session.commit()

        users = db.session.query(User).all()
        for user in users:
            self.assertEquals(user.role, 'user')


if __name__ == "__main__":
    unittest.main()

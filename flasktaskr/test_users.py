# test.py
    
    
import os
import unittest
    
from app import app, db
from app.models import User, FTasks
from config import basedir

from datetime import datetime, date
    
TEST_DB = 'test.db'
    
class UserTests(unittest.TestCase):
    
    # setup db and teardown
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
    
    def tearDown(self):
        db.drop_all()


    # helper methods
    def login(self, username, password):
        return self.app.post('users/', data=dict(
            name=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('users/logout', follow_redirects=True)

    def register(self):
        return self.app.post('users/register/', data=dict(
            name= 'michael',
            email = 'michael@realpython.com',
            password = 'herman',
            confirm="herman"
        ),follow_redirects=True)

    def create_user(self):
        new_user = User("mherman","michael@mherman.org","michaelherman")
        db.session.add(new_user)
        db.session.commit()


    # testing the views
    def test_users_can_login(self):
        self.create_user()
        response = self.login('mherman','michaelherman')
        assert 'You are logged in. Go Crazy.' in response.data

    def test_users_cannot_login_unless_registered(self):
        response = self.login('mherman','michaelherman')
        assert 'Invalid username or password.' in response.data

    def test_users_can_logout(self):
        self.create_user()
        response = self.logout()
        assert 'You are logged out. Bye. :(' in response.data

    def test_loggedin_users_can_access_tasks(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        response = self.app.get('tasks/tasks/',follow_redirects=True)
        assert 'Add a new task:' in response.data

    def test_not_logggedin_users_cannot_access_tasks(self):  
        response = self.app.get('tasks/tasks/',follow_redirects=True)
        assert 'You need to login first.' in response.data

    def test_user_registeration(self):
        self.app.get('users/register/',follow_redirects=True)
        response = self.register()
        assert 'Thanks for registering. Please login.' in response.data

    def test_user_registeration_error(self):
        self.app.get('users/register/',follow_redirects=True)
        self.register()
        self.app.get('users/register/',follow_redirects=True)
        response = self.register()
        assert 'Oh no! That username and/or email already exist. Please try again.' in response.data

    def test_404_error(self):
        response = self.app.get('/xxxxxxxxx/',follow_redirects=True)
        assert 'There\'s nothing here!' in response.data


    # testing the models
    def test_users_can_register_model(self):
        self.create_user()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "mherman"


if __name__ == "__main__":
    unittest.main()

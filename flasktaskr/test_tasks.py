# test.py
    
    
import os
import unittest
    
from app import app, db
from app.models import User, FTasks
from config import basedir

from datetime import datetime, date
    
TEST_DB = 'test.db'

class TasksTest(unittest.TestCase):
    
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

    def create_task(self):
        return self.app.post('tasks/add/', data=dict(
            name = 'Go to the bank',
            due_date = '02/05/2014',
            priority = '1',
            posted_date = '02/04/2014',
            status = '1'
        ), follow_redirects=True)


    # testing the views
    def test_users_can_add_tasks(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        self.app.get('tasks/tasks/',follow_redirects=True)
        response = self.create_task()
        assert 'New entry was successfully posted. Thanks.' in response.data

    def test_users_can_complete_tasks(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        self.app.get('/tasks/tasks',follow_redirects=True)
        self.create_task()
        response = self.app.get("tasks/complete/1/", follow_redirects=True)
        assert 'The task was marked as complete. Nice.' in response.data

    def test_users_can_delete_tasks(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        self.app.get('tasks/tasks/',follow_redirects=True)
        self.create_task()
        response = self.app.get("tasks/delete/1/", follow_redirects=True)
        assert 'The task was deleted. Why not add a new one?' in response.data

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        self.app.get('/tasks/tasks',follow_redirects=True)
        response = self.app.post('tasks/add/', data=dict(
            name = 'Go to the bank',
            due_date = '02/05/2014',
            priority = '1',
            posted_date = '',
            status = '1'
        ), follow_redirects=True)
        assert 'Error in the Posted Date (mm/dd/yyyy) field - This field is required.' in response.data


    # testing the models
    def test_users_can_add_tasks_model(self):
        self.create_user()
        self.login('mherman','michaelherman')   
        self.app.get('tasks/tasks/',follow_redirects=True)
        new_task = FTasks("Go to the bank", date.today(), "1", date.today(), "1", "1") 
        db.session.add(new_task) 
        db.session.commit()
        test = db.session.query(FTasks).all()
        for t in test:
            t.name
        assert t.name == "Go to the bank" 


if __name__ == "__main__":
    unittest.main()

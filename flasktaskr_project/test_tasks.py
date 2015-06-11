# test_tasks.py


import os
import unittest

from project import app, db, bcrypt
from config import basedir
from project.models import Task, User

TEST_DB = 'test.db'


class TasksTests(unittest.TestCase):

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

    def create_user(self):
        new_user = User(
            name='Michael',
            email='michael@realpython.com',
            password=bcrypt.generate_password_hash('python')
        )
        db.session.add(new_user)
        db.session.commit()

    def create_admin_user(self):
        new_user = User(
            name='Superman',
            email='admin@realpython.com',
            password=bcrypt.generate_password_hash('allpowerful'),
            role='admin'
        )
        db.session.add(new_user)
        db.session.commit()

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

    def create_task(self):
        return self.app.post('tasks/add/', data=dict(
            name='Go to the bank',
            due_date='02/05/2014',
            priority='1',
            posted_date='02/04/2014',
            status='1'
        ), follow_redirects=True)

    ###################
    #### templates ####
    ###################

    def test_task_template_displays_logged_in_user_name(self):
        self.register()
        self.login('Fletcher', 'python101')
        response = self.app.get('tasks/tasks/', follow_redirects=True)
        self.assertIn('Fletcher', response.data)

    ###############
    #### views ####
    ###############

    def test_logged_in_users_can_access_tasks_page(self):
        self.register()
        self.login('Fletcher', 'python101')
        response = self.app.get('tasks/tasks/', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Add a new task:', response.data)

    def test_not_logged_in_users_cannot_access_tasks_page(self):
        response = self.app.get('tasks/tasks/', follow_redirects=True)
        self.assertIn('You need to login first.', response.data)

    def test_users_cannot_see_task_modify_links_for_tasks_not_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register()
        response = self.login('Fletcher', 'python101')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.assertNotIn(
            'Mark as complete', response.data
        )
        self.assertNotIn(
            'Delete', response.data
        )

    def test_users_can_see_task_modify_links_for_tasks_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register()
        self.login('Fletcher', 'python101')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            'tasks/complete/2/', response.data
        )
        self.assertIn(
            'tasks/delete/2/', response.data
        )

    def test_admin_users_can_see_task_modify_links_for_all_tasks(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Superman', 'allpowerful')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            'tasks/complete/1/', response.data
        )
        self.assertIn(
            'tasks/delete/1/', response.data
        )
        self.assertIn(
            'tasks/complete/2/', response.data
        )
        self.assertIn(
            'tasks/delete/2/', response.data
        )

    ###############
    #### forms ####
    ###############

    def test_users_can_add_tasks(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            'New entry was successfully posted. Thanks.', response.data
        )

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.post('tasks/add/', data=dict(
            name='Go to the bank',
            due_date='',
            priority='1',
            posted_date='02/05/2014',
            status='1'
        ), follow_redirects=True)
        self.assertIn('This field is required.', response.data)

    def test_users_can_complete_tasks(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get("tasks/complete/1/", follow_redirects=True)
        self.assertIn('The task was marked as complete. Nice.', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get("tasks/delete/1/", follow_redirects=True)
        self.assertIn('The task was deleted.', response.data)

    def test_users_cannot_complete_tasks_that_are_not_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register()
        self.login('Fletcher', 'python101')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.get("tasks/complete/1/", follow_redirects=True)
        self.assertIn(
            'You can only update tasks that belong to you.', response.data
        )

    def test_users_cannot_delete_tasks_that_are_not_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register()
        self.login('Fletcher', 'python101')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.get("tasks/delete/1/", follow_redirects=True)
        self.assertIn(
            'You can only delete tasks that belong to you.', response.data
        )

    def test_admin_users_can_complete_tasks_that_are_not_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Superman', 'allpowerful')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.get("complete/1/", follow_redirects=True)
        self.assertNotIn(
            'You can only update tasks that belong to you.', response.data
        )

    def test_admin_users_can_delete_tasks_that_are_not_created_by_them(self):
        self.create_user()
        self.login('Michael', 'python')
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Superman', 'allpowerful')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.get("delete/1/", follow_redirects=True)
        self.assertNotIn(
            'You can only delete tasks that belong to you.', response.data
        )

    ################
    #### models ####
    ################

    def test_string_reprsentation_of_the_task_object(self):

        from datetime import date
        db.session.add(
            Task(
                "Run around in circles",
                date(2015, 1, 22),
                10,
                date(2015, 1, 05),
                1,
                1
            )
        )

        db.session.commit()

        tasks = db.session.query(Task).all()
        for task in tasks:
            self.assertEquals(task.name, 'Run around in circles')


if __name__ == "__main__":
    unittest.main()

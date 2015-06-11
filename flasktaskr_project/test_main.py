# test_main.py


import os
import unittest
from datetime import date

from project import app, db
from config import basedir
from project.models import Task


TEST_DB = 'test.db'


class MainTests(unittest.TestCase):

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

    def add_tasks(self):
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

        db.session.add(
            Task(
                "Purchase Real Python",
                date(2016, 2, 23),
                10,
                date(2016, 2, 07),
                1,
                1
            )
        )
        db.session.commit()

    ###############
    #### views ####
    ###############

    def test_index(self):
        """ Ensure flask was set up correctly. """
        response = self.app.get(
            '/', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_collection_endpoint_returns_correct_data(self):
        self.add_tasks()
        response = self.app.get('api/tasks/', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('Run around in circles', response.data)
        self.assertIn('Purchase Real Python', response.data)

    def test_resource_endpoint_returns_correct_data(self):
        self.add_tasks()
        response = self.app.get('api/tasks/2', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('Purchase Real Python', response.data)
        self.assertNotIn('Run around in circles', response.data)

    def test_invalid_resource_endpoint_returns_error(self):
        self.add_tasks()
        response = self.app.get('api/tasks/209', follow_redirects=True)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('Element does not exist', response.data)


if __name__ == "__main__":
    unittest.main()

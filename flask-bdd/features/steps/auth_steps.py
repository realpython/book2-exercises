from behave import *

@given(u'flaskr is setup')
def flask_setup(context):
    assert context.client and context.db
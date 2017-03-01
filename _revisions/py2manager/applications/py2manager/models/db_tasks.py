db.define_table('company',
     Field('company_name', notnull=True, unique=True),
     Field('email'),
     Field('phone', notnull=True),
     Field('url'),
     format = '%(company_name)s')  

db.company.email.requires=IS_EMAIL()
db.company.url.requires=IS_EMPTY_OR(IS_URL())        

db.define_table('project',
     Field('name', notnull=True),
     Field('employee_name', db.auth_user, default=auth.user_id),
     Field('company_name', 'reference company', notnull=True),
     Field('description', 'text', notnull=True),
     Field('start_date', 'date', notnull=True),
     Field('due_date', 'date', notnull=True),
     Field('completed', 'boolean', notnull=True),
     format = '%(company_name)s')

db.define_table('note',
     Field('post_id', 'reference project', writable=False),
     Field('post', 'text', notnull=True),
     Field('created_on', 'datetime', default=request.now, writable=False),
     Field('created_by', db.auth_user, default=auth.user_id))

db.note.post_id.readable = db.note.post_id.writable = False
db.note.created_on.readable = db.note.created_on.writable = False
db.note.created_on.requires = IS_DATE(format=T('%m-%d-%Y'),
            error_message='Must be MM-DD-YYYY!')
db.note.created_by.readable = db.note.created_by.writable = False 

db.project.employee_name.readable = db.project.employee_name.writable = False
db.project.start_date.requires = IS_DATE(format=T('%m-%d-%Y'),
        error_message='Must be MM-DD-YYYY!')

db.project.due_date.requires = IS_DATE(format=T('%m-%d-%Y'),
        error_message='Must be MM-DD-YYYY!')

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


@auth.requires_login()
def index():
    response.flash = T('Welcome!')
    notes = [lambda project: A('Notes', _class="btn", _href=URL("default","note",args=[project.id]))]
    grid = SQLFORM.grid(db.project, create=False, links=notes, 
    fields=[db.project.name, db.project.employee_name, db.project.company_name, 
    db.project.start_date, db.project.due_date, db.project.completed], deletable=False, maxtextlength=50)
    return locals()

@auth.requires_login()               
def note():
    project = db.project(request.args(0))
    db.note.post_id.default = project.id
    form = crud.create(db.note) if auth.user else "Login to Post to the Project"
    allnotes = db(db.note.post_id==project.id).select()
    return locals()

def tester():
    return locals()

@auth.requires_login()  
def add():
    project_form = SQLFORM(db.project).process()
    return dict(project_form=project_form)

@auth.requires_login()  
def company():
    company_form = SQLFORM(db.company).process()
    grid = SQLFORM.grid(db.company, create=False, deletable=False, editable=False, 
    maxtextlength=50, orderby=db.company.company_name)
    return locals()

@auth.requires_login()  
def employee():
    employee_form = SQLFORM(db.auth_user).process()
    grid = SQLFORM.grid(db.auth_user, create=False, fields=[db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email], deletable=False, editable=False, maxtextlength=50)
    return locals()  

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

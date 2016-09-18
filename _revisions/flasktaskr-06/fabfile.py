from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


# prep

def test():
    with settings(warn_only=True):
        result = local("nosetests -v", capture=True)
    if result.failed and not confirm("Tests failed. Continue?"):
        abort("Aborted at user request.")


def commit():
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -am '{}'".format(message))


def push():
    local("git push origin master")


def prepare():
    test()
    commit()
    push()


# deploy

def pull():
    local("git pull origin master")


def heroku():
    local("git push heroku master")


def heroku_test():
    local("heroku run nosetests -v")


def deploy():
    pull()
    test()
    commit()
    heroku()
    heroku_test()


# rollback

def rollback():
    local("heroku rollback")

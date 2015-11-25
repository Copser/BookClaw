from fabric.api import local


# Git deployment setup
def commit():
    local('git add .')
    print("Enter your git commit message: ")
    comment = raw_input()
    local('git commit -m "%s"' % comment)


def prep():
    commit()


def push():
    local('git push -u origin master')
    local('heroku maintenance:on')
    local('git push heroku master')
    local('heroku maintenance:off')


def deploy():
    push()

import os
from fabric.api import *

env.hosts = ['webfaction']

def deploy():
    code_dir = '~/webapps/pedal/pedal'
    with cd(code_dir):
        local('git push')
        run('git pull')
        run('python2.7 manage.py collectstatic --noinput')
        run('../apache2/bin/restart')

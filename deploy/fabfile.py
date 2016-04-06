import random

from fabric.contrib.files import exists, sudo, append
from fabric.api import env, local, run, get


env.use_ssh_config = True

REPO_URL = 'https://github.com/nicorellius/fiblist.git'
SETTINGS_FOLDER = 'fiblist/conf/settings'
PROJECT = 'fiblist'
VIRTENV_FOLDER = '/home/{0}/dev/virtenvs/{1}'.format(env.user, PROJECT)


def deploy():

    site_folder = '/home/{0}/sites/{1}'.format(env.user, PROJECT)
    source_folder = '{0}/source'.format(site_folder)
    secret_key_file = '/etc/prv/{0}/secret_key.txt'.format(PROJECT)
    http_server = 'nginx'
    uwsgi_server = 'uwsgi'

    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(site_folder, source_folder)
    _generate_secret_key(source_folder, secret_key_file)
    _update_virtenv(site_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _restart_servers(http_server, uwsgi_server)


def _create_directory_structure_if_necessary(site_folder):

    for subfolder in ('database', 'static', 'source'):
        run('mkdir -p {0}/{1}'.format(site_folder, subfolder))


def _get_latest_source(site_folder, source_folder):

    if exists('{0}/{1}'.format(site_folder, '.git')):
        run('cd {0} && git fetch'.format(source_folder))

    else:
        run('git clone {0} {1}'.format(REPO_URL, source_folder))

    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('cd {0} && git reset --hard {1}'.format(source_folder, current_commit))


def _generate_secret_key(source_folder, secret_key_file):

    settings_file = '{0}/{1}/staging.py'.format(source_folder, SETTINGS_FOLDER)

    if exists(secret_key_file):
        get(remote_path=secret_key_file, local_path='/tmp/secret_key.txt')

        tmp_key_path = '/tmp/secret_key.txt'
        with open(tmp_key_path, 'r') as key_file:
            data = key_file.read().replace('\n', '')

        tmp_key_file = data

        if tmp_key_file is not '':
            append(settings_file, '\nSECRET_KEY = "{0}"'.format(tmp_key_file))

    else:
        print("[localhost] print: Remote key file does not exist. Making one now.")
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        generated_key = ''.join([random.SystemRandom().choice(chars) for _ in range(50)])

        append(settings_file, '\nSECRET_KEY = "{0}"'.format(generated_key))


def _update_virtenv(site_folder):

    virtenv_folder = VIRTENV_FOLDER

    if not exists('{0}/bin/pip'.format(virtenv_folder)):
        run('mkvirtualenv --python=/usr/bin/python3 {0}'.format(virtenv_folder))

    run('{0}/bin/pip install -r {1}/requirements.txt'.format(
        virtenv_folder,
        site_folder
    ))


def _update_static_files(source_folder):
    run('cd {0} && {1}/bin/python3 manage.py collectstatic --noinput --settings={2}.conf.settings.staging'.format(
        source_folder,
        VIRTENV_FOLDER,
        PROJECT
    ))


def _update_database(source_folder):
    run('cd {0} && {1}/bin/python3 manage.py migrate --noinput --settings={2}.conf.settings.staging'.format(
        source_folder,
        VIRTENV_FOLDER,
        PROJECT
    ))


def _restart_servers(http_server, uwsgi_server):
    sudo('service {0} restart'.format(http_server))
    sudo('restart {0}'.format(uwsgi_server))

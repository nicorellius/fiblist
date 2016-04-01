import random

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'https://github.com/nicorellius/fiblist.git'


def deploy():

    site_folder = '/home/{0}/sites/{1}'.format(env.user, env.host)
    source_folder = '{0}/{1}'.format(site_folder, '/source')

    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_ssettings(source_folder, env.host)
    _update_virtenv(source_folder)
    _update_static_diles(source_folder)
    _update_database(source_folder)

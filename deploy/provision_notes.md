# Provisioning a new site

## Required packages

- Python 3
- Git
- nginx
- pip
- virtualenvwrapper
- uwsgi

On Ubuntu:

sudo apt-get install nginx
sudo apt-get install vim git python3 python3-pip
sudo pip install virtualenvwrapper

Add to ~/.bashrc:

export WORKON_HOME=$HOME/dev/virtenvs
source /usr/local/bin/virtualenvwrapper.sh
# Provisioning a new site

## Required packages

- Python 3
- Git
- nginx
- pip
- virtualenvwrapper
- uwsgi

**Ubuntu and Python packages**

> `sudo apt-get install nginx`  
> `sudo apt-get install vim git python3 python3-pip`  
> `sudo pip install virtualenvwrapper`  

**Add to `~/.bashrc`**

> `export WORKON_HOME=$HOME/dev/virtenvs`  
> `source /usr/local/bin/virtualenvwrapper.sh`

## nginx virtual host configuration

- See the `nginx/template.conf` for template.

## uWSGI compilation and configuration

- Download uWSGI and build with no Python, so custom plugins ca be created.

- See uwsgi/template.ini for template.

## Upstart scripts

- See `upstart/nginx.conf` and `upstart/uwsgi.conf` for templates.

## Source tree

- See `source_tree.md` for more information.


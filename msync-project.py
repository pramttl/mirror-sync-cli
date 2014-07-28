#! /usr/bin/env python

import click
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urlparse
import settings

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
def project_commands():
    """
    Mirror Syncing CLI to add, update, remove projects.
    """


@project_commands.command('add', short_help='Used to add a project')
@click.argument('project')
@click.argument('host')
@click.argument('rsyncmod')
@click.argument('rsyncpwd')
@click.argument('dest')
@click.option('--cron', help='Cron options')
def add_project(project, host, rsyncmod, rsyncpwd, dest, cron):
    """
    Used to schedule projects for syncing. Most of the paramters are required.
    Cron options is a JSON String like:
    \'{"minute": "*", "start_date": "2014-05-7 18:00"}\'
    """
    url1 = 'http://' + settings.MASTER_HOSTNAME + ':' + str(settings.MASTER_PORT)
    url2 = '/add_project/'
    url = urlparse.urljoin(url1, url2)

    data = {
     "project": project,
     "rsync_module": rsyncmod,                             # rsync module
     "rsync_host": host,
     "dest": dest,
     "rsync_password": rsyncpwd,
     "cron_options": json.loads(cron),
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth('root', 'root'), data=json.dumps(data), headers=headers)
    click.echo('Added the project')


@project_commands.command('remove', context_settings=CONTEXT_SETTINGS)
@click.argument('project_id')
def remove_project(project_id, cron):
    """
    Used to schedule projects for syncing. Most of the paramters are required.
    """
    url1 = 'http://' + settings.MASTER_HOSTNAME + ':' + str(settings.MASTER_PORT)
    url2 = '/remove_project/'
    url = urlparse.urljoin(url1, url2)

    data = {
     "id": project_id,
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth('root', 'root'), data=json.dumps(data), headers=headers)
    click.echo('Removed project')


if __name__ == '__main__':
    project_commands()


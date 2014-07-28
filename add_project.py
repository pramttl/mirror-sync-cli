#! /usr/bin/env python

import click
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urlparse
import settings

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('project')
@click.argument('host')
@click.argument('rsyncmod')
@click.argument('rsyncpwd')
@click.argument('dest')
@click.option('--cron', help='''Cron options is a JSON String like: 
                             \'{"minute": "*", "start_date": "2014-05-7 18:00"}\'''')
def add_project(project, host, rsyncmod, rsyncpwd, dest, cron):
    """
    Used to schedule projects for syncing. Most of the paramters are required.
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


if __name__ == '__main__':
    add_project()


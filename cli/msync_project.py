#! /usr/bin/env python

import click
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urlparse
from dateutil.parser import parse

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

import os
import sys
USR_DIR = sys.prefix
CONFIG_DIR = os.path.join(USR_DIR, 'local/mirror-sync-cli')

CONFIG_FILE = 'config/config.cfg'
for loc in os.curdir, os.path.expanduser("~"), CONFIG_DIR, os.environ.get("MYPROJECT_CONF"):
    try: 
        open(TEMP_CONFIG_FILE)
        CONFIG_FILE = TEMP_CONFIG_FILE
    except:
        pass


try:
    f = open(CONFIG_FILE)
    config = json.loads(f.read())
    ROOT_USERNAME = config['username']
    ROOT_PASSWORD = config['password']
    MASTER_HOSTNAME = config['master_hostname']
    MASTER_HOSTNAME = int(config['master_port'])
    f.close()
except:
    ROOT_USERNAME = 'root'
    ROOT_PASSWORD = 'root'
    MASTER_HOSTNAME = 'localhost'
    MASTER_PORT = 5000

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
    To schedule projects for syncing. Most of the paramters are required.
    Cron options is a JSON String like:
    \'{"minute": "*", "start_date": "2014-05-7 18:00"}\'
    """
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
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
    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)
    click.echo('Added the project')


@project_commands.command('remove', context_settings=CONTEXT_SETTINGS)
@click.argument('project_id')
def remove_project(project_id, cron):
    """
    To schedule projects for syncing. Most of the paramters are required.
    """
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/remove_project/'
    url = urlparse.urljoin(url1, url2)

    data = {
     "id": project_id,
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)
    click.echo('Removed project')


@project_commands.command('update', short_help='To update basic parameters of a project.')
@click.argument('project_id')
@click.option('--project', help='A new name for the project')
@click.option('--rsynchost', help='New rsync hostname')
@click.option('--rsyncmod', help='New rsync module name')
@click.option('--rsyncpwd', help='Updated rsync password if any')
@click.option('--dest', help='Updated destination for syncing on master node')
@click.option('--rsync_options', help='Rsync options in json format')
def update_project_basic(project_id, project, host, rsyncmod, rsyncpwd, dest, cron):
    """
    To update basic parameters of a project.
    """
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/update_project/basic/'
    url = urlparse.urljoin(url1, url2)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # Project id is the only required paramter.
    data['id'] = project_id

    if project:
        data['project'] = project
    if host:
        data['rsync_host'] = host
    if rsyncmod:
        data['rsync_module'] = rsyncmod
    if dest:
        data['dest'] = dest,
    if rsync_options:
        data['rsync_options'] = json.loads(rsync_options)

    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)
    click.echo('Updated basic project parameters.')


@project_commands.command('reschedule', short_help='To update syncing schedule of a project')
@click.argument('project_id')
@click.option('--year', help='4-digit year number')
@click.option('--month', help='month number (1-12)')
@click.option('--day', help='day of the month (1-31)')
@click.option('--week', help='ISO week number (1-53)')
@click.option('--day_of_week', help='number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)')
@click.option('--hour', help='hour (0-23)')
@click.option('--minute', help='minute (0-59)')
@click.option('--second', help='second (0-59)')
@click.option('--start_date', help='Start date in human readable string format (fuzzy parsed to python datetime internally)')
def update_project_schedule(project_id, year, month, day, week, day_of_week, hour, minute, second, start_date):
    """
    To update syncing schedule of a project.
    """
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/update_project/schedule/'
    url = urlparse.urljoin(url1, url2)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # Project id is the only required paramter.
    data['id'] = project_id

    if year:
        data['year'] = project
    if month:
        data['month'] = month
    if day:
        data['day'] = day
    if week:
        data['week'] = week
    if day_of_week:
        data['day_of_week'] = day_of_week
    if hour:
        data['hour'] = hour
    if minute:
        data['minute'] = minute
    if second:
        data['second'] = second
    if start_date:
        data['start_date'] = parse(start_date, fuzzy=True)

    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)


@project_commands.command('list', short_help='To list ids of existing projects scheduled for syncing.')
def list_projects():
    """
    To list id's of exisitng projects scheduled for syncing.
    Id's of projects are same as name by default.
    """
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/list_projects/'
    url = urlparse.urljoin(url1, url2)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(dict()), headers=headers)
    projects = json.loads(r.text)
    for project in projects:
        click.echo(project['id'])

def main():
    project_commands()

if __name__=='__main__':
    main()

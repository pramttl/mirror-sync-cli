#! /usr/bin/env python

import click
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urlparse

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

try:
    f = open('config.cfg')
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
def slave_commands():
    """
    Mirror Syncing CLI to add, update, remove projects.
    """


@slave_commands.command('add', short_help='Used to add a slave to the mirror syncing cluster')
@click.option('--hostname', default='locahost', help='hostname of slave node')
@click.option('--port', default=7000, help='port number on which slave daemon runs')
def add_slave(hostname, port):
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/add_slave/'
    url = urlparse.urljoin(url1, url2)

    data = {
     'hostname': hostname,
     'port': str(port),
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)


@slave_commands.command('remove', short_help='Used to remove a slave from the mirror syncing cluster')
@click.option('--hostname', default='locahost', help='hostname of slave node')
def remove_slave(hostname, port):
    url1 = 'http://' + MASTER_HOSTNAME + ':' + str(MASTER_PORT)
    url2 = '/remove_slave/'
    url = urlparse.urljoin(url1, url2)

    data = {
     'hostname': hostname,
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth(ROOT_USERNAME, ROOT_PASSWORD), data=json.dumps(data), headers=headers)


def main():
    slave_commands()

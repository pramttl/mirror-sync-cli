#! /usr/bin/env python

import click
import simplejson as json

import os
import sys
USR_DIR = sys.prefix
CONFIG_DIR = os.path.join(USR_DIR, 'local/mirror-sync-cli')

CONFIG_FILE = 'config/config.cfg'
for loc in os.curdir, os.path.expanduser("~"), CONFIG_DIR, os.environ.get("MYPROJECT_CONF"):
    try: 
        TEMP_CONFIG_FILE = os.path.join(loc, "config.cfg")
        open(TEMP_CONFIG_FILE)
        CONFIG_FILE = TEMP_CONFIG_FILE
    except:
        pass

@click.group()
def config_commands():
    """
    The following can be configured: \n
      - Master daemon hostname and port\n
      - Setting root credentials to connect to mirror-sync-api
    """


@config_commands.command('root', short_help='to set root credentials to connect to api')
@click.option('--username', default='root', help='Root username, same as in mirror-syncing-api')
@click.option('--password', default='root', help='Root password as in mirror-sync-api')
def set_root_credentials(username, password):
    """
    Allows the user to tell the CLI the root credentials to connect to the
    mirror-sync-api
    """
    # Read original config and update
    f = open(CONFIG_FILE, 'r')
    config = json.loads(f.read())
    config['username'] = username
    config['password'] = password
    f.close()

    # Write updated config
    f = open(CONFIG_FILE, 'w')
    f.write(json.dumps(config))
    f.close()


@config_commands.command('master', short_help='Set hostname and port of master daemon')
@click.option('--hostname', default='localhost', help='Hostname of the master node in mirror syncing cluster')
@click.option('--port', default=5000, help='Port on which mirror-syncing-api master daemon runs')
def set_master(hostname, port):
    """
    Allows the user to tell the details of the master node and the master api
    daemon the cli indirectly connects to for issuing commands.
    """
    # Read original config and update
    f = open(CONFIG_FILE, 'r')
    config = json.loads(f.read())
    config['master_hostname'] = hostname
    config['master_port'] = int(port)
    f.close()

    # Write updated config
    f = open(CONFIG_FILE, 'w')
    f.write(json.dumps(config))
    f.close()

def main():
    config_commands()

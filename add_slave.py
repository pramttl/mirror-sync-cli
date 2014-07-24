#! /usr/bin/env python

import click
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import urlparse
import settings

@click.command()
@click.option('--hostname', default='locahost', help='hostname of slave node')
@click.option('--port', default=7000, help='port number on which slave daemon runs')
def add_slave(hostname, port):
    url1 = 'http://' + settings.MASTER_HOSTNAME + ':' + str(settings.MASTER_PORT)
    url2 = '/add_slave/'
    url = urlparse.urljoin(url1, url2)

    data = {
     'hostname': hostname,
     'port': str(port),
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, auth=HTTPBasicAuth('root', 'root'), data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    add_slave()

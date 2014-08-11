#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

import sys
import os

USR_DIR = sys.prefix
CONFIG_DIR = os.path.join(USR_DIR, 'local/mirror-sync-cli')

dependencies = ['click', 'simplejson', 'requests', 'python-dateutil',]

setup(
        name='msync',
        version='0.0.3',
        description='Mirror Syncing CLI',
        url='https://github.com/pramttl/mirror-sync-cli',
        author='Pranjal Mittal',
        author_email='pranjal.mittal.ece10@iitbhu.ac.in',
        install_requires=dependencies,
        packages=['cli',],
        entry_points={
            'console_scripts': [
                'msync-configure=cli.set_config:main',
                'msync-project=cli.msync_project:main',
                'msync-slave=cli.msync_slave:main',
            ]
        },
        data_files=[(CONFIG_DIR, ['config/config.cfg',]),]
)

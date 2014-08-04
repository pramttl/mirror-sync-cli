## Mirror Syncing CLI

The following command types are available at the moment

## Setup/Start Mirror Syncing API

Setup and start the Mirror Syncing API first, as explained [here](https://github.com/pramttl/mirror-sync-api)
The CLI internally interacts with the mirror syncing api, so it is important to
start it before using the CLI commands.

    git clone git@github.com:pramttl/mirror-sync-cli.git
    cd mirror-sync-cli
    virtualenv venv             #Optional
    source venv/bin/activate    #Optional
    python setup.py install


### Commands

After the CLI is installed via setuptools, the following command groups are available
in the bash context, along with *Tab* completion. Each command group has its own subset
of commands.

#### msync-configure

Used to set default configuration parameters like root credentials to connect to API,
hostname and port of master daemon so that you do not have to provide them everytime
while using other commands in the cli.

    msync-configure --help

#### msync-project

    msync-project.py [OPTIONS] COMMAND [ARGS]...

    # To get help on all the commands included use:
    msync-project --help

#### msync-slave

    //Todo


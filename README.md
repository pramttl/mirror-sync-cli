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

To update an existing installation

    # Activate venv in context if any
    pip uninstall msync
    cd /path/to/mirror-sync-cli
    python setup.py install

## Commands

After the CLI is installed via setuptools, the following command groups are available
in the bash context, along with *Tab* completion. Each command group has its own subset
of commands.

### msync-configure

Used to set default configuration parameters like root credentials to connect to API,
hostname and port of master daemon so that you do not have to provide them everytime
while using other commands in the cli.

    msync-configure [OPTIONS] COMMAND [ARGS]...

The following can be configured:

    - Master daemon hostname and port
    - Setting root credentials to connect to mirror-sync-api

Commands:

    master  Set hostname and port of master daemon (Default: localhost, 5000)
    root    to set root credentials to connect to api (Default: root, root)

**Examples**:

To change the hostname and port of the master node.

    msync-configure master --hostname localhost --port 5000

To change the root username to pranjal

    msync-configure root --username pranjal


### msync-project

    msync-project [OPTIONS] COMMAND [ARGS]...

Mirror Syncing CLI to add, update, remove projects.

Commands:

    add         Used to add a project
    remove      To schedule projects for syncing.
    reschedule  To update syncing schedule of a project
    update      To update basic parameters of a project.


### msync-slave

    msync-slave [OPTIONS] COMMAND [ARGS]...

Mrror Syncing CLI to add, update, remove projects.

Commands:

    add     Used to add a slave to the mirror syncing cluster
    remove  Used to remove a slave from the mirror syncing cluster


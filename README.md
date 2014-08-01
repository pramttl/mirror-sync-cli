## Mirror Syncing CLI

The following command types are available at the moment

### Setup/Start Mirror Syncing API

Setup and start the Mirror Syncing API first, as explained [here](https://github.com/pramttl/mirror-sync-api)
The CLI internally interacts with the mirror syncing api, so it is important to
start it before using the CLI commands.

    git clone git@github.com:pramttl/mirror-sync-cli.git
    cd mirror-sync-cli
    virtualenv venv
    pip install -r requirements.txt

### msync-project.py

Project related commands

    msync-project.py [OPTIONS] COMMAND [ARGS]...

    # To get help on all the commands included use:
    msync-project.py --help

### msync-slave.py

    //Todo


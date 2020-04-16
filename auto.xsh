#!/usr/bin/env xonsh

from syspy import Shell
from syspy.tools import getInputs, parseOptions
from config import dir
sh = Shell()

version = 'Version: 0.0.1'

synopsis_msg = '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
auto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
automating tasks for building our chrome extension continuously with dependencies
'''
def synopsis():
    print(synopsis_msg)

help_msg = '''options
    -h, --help :\thelp menu
    --synopsis :\tpackage description
    -v, --verbose :\ttalk to me
    --version :\tversion

commands
    build: create project by pulling dependencies
    load: run the extension in chromium (kills all instances of chromium)
'''

def help():
    print(help_msg)

shortOpts = 'hv'
longOpts = [
    'help',
    'synopsis',
    'verbose',
    'version',
    ]

# parsed options and gathers remainder (command)
options, command, remainder = parseOptions(getInputs(), shortOpts, longOpts)

# deals with options accordingly
for opt, arg in options:
    if opt in ('-h', '--help'): help(); sh.log.succeed()
    elif opt in ('--synopsis'): synopsis(); sh.log.succeed()
    elif opt in ('-v', '--verbose'): sh.verbose = True
    elif opt == '--version': print(version); sh.log.succeed()

if (command):
    if command == 'load':
        # killall chromium
        # chromium --load-extension=@(dir.build) 'reddit.com'
        ./scripts/load.sh &
    elif command == 'build':
        ./scripts/build.xsh
    else: print('unrecognized command')
else:
    # default behavior of the package
    synopsis()
    help()


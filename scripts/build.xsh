#!/usr/bin/xonsh
import os
from syspy import Shell, extend
sh = Shell()

from config import dir

reset='\033[0m'
cyan = '\033[36m'

def build_step(partial_function):
    def whole_function(*args, **kwargs):
        print('{}_______________________________________________{}'.format(cyan, reset))
        print(cyan, '[Build Step]', reset, partial_function.__name__.replace('_', ' '))
        print()
        partial_function(*args, **kwargs)
        print()
    return whole_function

@build_step
def reset_and_update_uBlock():
    if sh.exists(dir.uBlock):
        sh.cd(dir.uBlock)
        git reset --hard HEAD
        git clean -f
        git clean -fd
        git pull
    else:
        git clone https://github.com/gorhill/uBlock.git


@build_step
def build_uBlock_for_chrome():
    sh.cd(dir.uBlock)
    bash 'tools/copy-common-files.sh' @(dir.chromium)

@build_step
def move_chrome_uBlock_to_adium():
    if sh.exists(dir.build): sh.rm(dir.build)
    sh.mkdir(dir.build)
    sh.cp(dir.chromium, dir.build)

# TODO: potentially clone uBlock if doesn't exist
sh.verbose = True
reset_and_update_uBlock()
build_uBlock_for_chrome()
move_chrome_uBlock_to_adium()
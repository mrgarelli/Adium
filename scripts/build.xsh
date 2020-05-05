#!/usr/bin/env xonsh
import os
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
    if os.path.exists(dir.uBlock):
        cd @(dir.uBlock)
        git reset --hard HEAD
        git clean -f
        git clean -fd
        git pull
    else:
        git clone https://github.com/gorhill/uBlock.git


@build_step
def build_uBlock_for_chrome():
    cd @(dir.uBlock)
    bash 'tools/copy-common-files.sh' @(dir.chromium)

@build_step
def move_chrome_uBlock_to_adium():
    if os.path.exists(dir.build):
        rm -rf @(dir.build)
    # mkdir @(dir.build)
    cp -r @(dir.chromium)  @(dir.build)

reset_and_update_uBlock()
build_uBlock_for_chrome()
move_chrome_uBlock_to_adium()
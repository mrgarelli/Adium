#!/usr/bin/env python3
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

def build_ublock(sh):

    @build_step
    def reset_and_update_uBlock():
        if sh.exists(dir.uBlock):
            sh.cd(dir.uBlock)
            sh.command('git reset --hard HEAD')
            sh.command('git clean -f')
            sh.command('git clean -fd')
            sh.command('git pull')
        else:
            sh.command('git clone https://github.com/gorhill/uBlock.git')


    @build_step
    def build_uBlock_for_chrome():
        sh.cd(dir.uBlock)
        sh.command(['bash', 'tools/copy-common-files.sh', dir.chromium])

    @build_step
    def move_chrome_uBlock_to_adium():
        if sh.exists(dir.build):
            sh.command(['rm -rf', dir.build])
        sh.command(['cp -r', dir.chromium, dir.build])

    reset_and_update_uBlock()
    build_uBlock_for_chrome()
    move_chrome_uBlock_to_adium()
#!/usr/bin/env xonsh

import os
from syspy import Shell, extend
sh = Shell()

class dir:
    adium = sh.dirname(os.path.abspath(__file__))
    uBlock = extend(adium, 'uBlock')
    chromium = extend(uBlock, 'platform/chromium')
    build = extend(adium, 'build')

#!/usr/bin/env xonsh

import os

class dir:
    adium = os.path.dirname(os.path.abspath(__file__))
    uBlock = os.path.join(adium, 'uBlock')
    chromium = os.path.join(uBlock, 'platform', 'chromium')
    build = os.path.join(adium, 'build')

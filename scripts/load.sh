#!/usr/bin/env bash

killall chromium
chromium --load-extension='./build' 'reddit.com' &

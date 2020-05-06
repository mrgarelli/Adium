#!/usr/bin/env bash

source ./env/bin/activate
pip install -r ./requirements.txt
pip install --upgrade -i https://test.pypi.org/simple/ syspy
pip install --upgrade -i https://test.pypi.org/simple/ declarecli

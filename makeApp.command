#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH
python3 -m venv $SCRIPTPATH/path/to/venv
source $SCRIPTPATH/path/to/venv/bin/activate
python3 -m pip install setuptools
python3 -m pip install jaraco.text




python3 setup.py py2app
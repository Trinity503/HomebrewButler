#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH
python3 -m venv $SCRIPTPATH/path/to/venv
source $SCRIPTPATH/path/to/venv/bin/activate

pyinstaller \
    --clean \
    --windowed \
    --name "HomebrewButler" \
    --icon "media/HomebrewButler_menubar_y.icns" \
    --add-data "media:media" \
    --add-data "brew_upgrade.sh:." \
    HomebrewButler.py
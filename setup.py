from setuptools import setup

APP = ['HomebrewButler.py']
DATA_FILES = ['media','brew_upgrade.sh']
OPTIONS = {
    'argv_emulation': False,#changed to false because of missing carbon framework: https://github.com/jaredks/rumps/issues/208#issuecomment-1817662981
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile':'media/HomebrewButler_app.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
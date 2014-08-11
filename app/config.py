# config.py

import os

# grab the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLE = True
SECRET_KEY = 'zfFMC46cyipZuYDUT;HkttxH4HXj3DgCYV!e'

# defines the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
import sys

project_home = '/home/katekatekatem/online_clock'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from clock_app.server import app as application

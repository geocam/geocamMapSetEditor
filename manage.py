#!/usr/bin/env python
# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

import os
import sys

# try to bootstrap before hooking into django management stuff
if 'bootstrap' in sys.argv:
    extraArgs = sys.argv[2:]
else:
    extraArgs = []
ret = os.spawnl(os.P_WAIT, sys.executable, sys.executable,
                '%s/management/bootstrap.py' % os.path.dirname(__file__),
                *extraArgs)
if ret != 0 or extraArgs:
    sys.exit(ret)

from django.core.management import execute_manager
try:
    import settings  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)

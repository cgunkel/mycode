#!/usr/bin/env python3

import shutil
import os

# Set the working directory
os.chdir('/home/student/mycode/')

# The following line will rename a file
# Move the file or folder
shutil.move('raynor.obj', 'ceph_storage/')

# Prompt for input for new newname
xname = input('What is the new name for kerrigan.obj? ')

# Rename kerrigan.obj
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

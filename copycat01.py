#!/usr/bin/env python3

#import additional code
import shutil
import os

#Set the working direectory
os.chdir("/home/student/mycode/")

# copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# The following line will create the directory if it does not exist already
# copy directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")



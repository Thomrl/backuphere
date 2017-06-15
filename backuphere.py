#! python3.5
#Backup files chosen folder. Making a backup folder in that folder.
import os, sys
from distutils.dir_util import copy_tree

#Select folder and check if it exists
path = sys.argv[1]
if os.path.exists(path):
    print("\""+path+"\""+" exists.")

#Check if _Backup folder exists if not, copy_tree into a new _Backup folder which will be created.
if os.path.exists(path+"\\_Backup"):
    print("\""+path+"\\_Backup\""+" already exists, please check the current \"_Backup\" folder out")
else:
    copy_tree(path, path+"\\_Backup")
    print("Your files have now been backed up! :)")

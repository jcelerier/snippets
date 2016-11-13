#!/usr/bin/python

import os
import sys
import zipfile
import shutil
import subprocess

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

def contains_jpg(string):
	return ".jpg" in string or ".JPG" in string or ".Jpg" in string or ".jpeg" in string or ".png" in string

rootdir = sys.argv[1]
for root, subfolders, files in os.walk(rootdir):
	for file in files:
		if ".pdf" in file or ".PDF" in file:
			print file
			filepath = os.path.join(root, file)
#			print filepath
			filedir = os.path.splitext(filepath)[0]
#			print filedir

			if(not os.path.exists(filedir)):
				os.mkdir(filedir)
			
				command = 'pdfimages -all \"' + filepath + '\" \"' + filedir + '/image\"'
				subprocess.call(['pdfimages', '-all', filepath, filedir + '/image'])
#				print command		
				os.remove(filepath)

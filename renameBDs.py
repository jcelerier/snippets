#!/usr/bin/python

import os
import sys
import zipfile
import shutil

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

def contains_jpg(string):
	return ".jpg" in string or ".JPG" in string or ".Jpg" in string or ".jpeg" in string or ".png" in string

rootdir = sys.argv[1]
for root, subfolders, files in os.walk(rootdir):
	if all(contains_jpg(file) for file in files) and len(files) > 0 and len(subfolders)== 0:
		# zip it!
		print root
		zipf = zipfile.ZipFile(root + '.cbz', 'w')
		zipdir(root, zipf)
		shutil.rmtree(root)

#! /usr/bin/env python
# download file from requested url, handling name collisions and storing 
# information on the source of the file

# download file storing it named as it is in the url e.g. http://www.google.com/image.png
# as image.png
# if there is already a file named image.png stored, the file will be named using a hash of 
# the url.
# When a file is downloaded a json blob stored in a like named file within the .json directory
# will be saved recording metadata about the download such as url, time, etc
# 
# a hash of the downloaded url will be stored in a directory below the working directory
# named .hashes.  The hashes in this directory will be used to avoid downloading of the same
# url more than once.

import os.path
import urlparse
import json

HASH_DIR = ".hashes"
META_DIR = ".json"

def get_hash(for_this):
    import hashlib
    h = hashlib.sha256()
    h.update(for_this)
    return h.hexdigest()

url = "http://www.google.com/something/image.png"
file_name = os.path.basename(urlparse.urlparse(url)[2])

print("file name: %s " % (file_name))
print("hash: %s " % (get_hash(url)))


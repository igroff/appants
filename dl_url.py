#! /usr/bin/env python
# download file from requested url, handling name collisions and storing 
# information on the source of the file

# download file storing it named as it is in the url e.g.
# http://www.google.com/image.png
# as image.png
# if there is already a file named image.png stored, the file will be named
# using a hash of the url
# When a file is downloaded a json blob stored in a like named file within the
# .json directory
# will be saved recording metadata about the download such as url, time, etc
# 
# a hash of the downloaded url will be stored in a directory below the
#  working directory
# named .hashes.  The hashes in this directory will be used to avoid
# downloading of the same
# url more than once.

import os.path
import urlparse
import json
import argparse
import sys

HASH_DIR = ".hashes"
META_DIR = ".json"

def get_hash(for_this):
    import hashlib
    h = hashlib.sha256()
    h.update(for_this)
    return h.hexdigest()

parser = argparse.ArgumentParser(description='downloads the url')
parser.add_argument('urls', nargs='+',
                   help='urls to be fetched')
args = parser.parse_args(sys.argv)

cwd = os.getcwd()
hash_dir = os.path.join(cwd, HASH_DIR)
meta_dir = os.path.join(cwd, META_DIR)

def fetch_url(url, to_file_name):
    print("url: %s" % (url))
    print("file name: %s " % (file_name))

def store_meta(for_url, data={}):
    data['url'] = for_url
    print json.dumps(data)

def store_hash(for_url):
    print("hash: %s " % (get_hash(url)))

for url in args.urls:
    file_name = os.path.basename(urlparse.urlparse(url)[2])
    if not file_name == os.path.basename(__file__):
        fetch_url(url, file_name)
        store_meta(url, {})
        store_hash(url)



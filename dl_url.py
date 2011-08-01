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

if not os.path.exists(meta_dir):
    os.makedirs(meta_dir)
if not os.path.exists(hash_dir):
    os.makedirs(hash_dir)

def fetch_url(url, to_file_name):
    import urllib2
    with urllib2.urlopen(url) as resp:
        with open(os.path.join(cwd, to_file_name), "w+") as out:
            for line in resp:
                out.write(line)

def store_meta(for_url, to_file,  data={}):
    data['url'] = for_url
    with open(os.path.join(meta_dir, to_file), "w+") as file:
        json.dump(data, file)

def store_hash(for_url):
    hash = get_hash(url)
    hash_path = os.path.join(hash_dir, hash)
    if os.path.exists(hash_path):
        raise Exception("url already downloaded")
    with open(hash_path, "w+") as file:
        pass

for url in args.urls:
    file_name = os.path.basename(urlparse.urlparse(url)[2])
    if not file_name == os.path.basename(__file__):
        fetch_url(url, file_name)
        store_meta(url, file_name, {})
        store_hash(url)



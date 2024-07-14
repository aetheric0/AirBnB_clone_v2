#!/usr/bin/python3
""" Uses fabric to compress web_static files
"""
from fabric.api import local
import os
from datetime import datetime

def do_pack():
    """ Packs the web_static files into the versions directory
    named according to date created.
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    folder_to_archive = 'web_static'
    output_file = 'versions/webstatic_{}.tgz'.format(date)
    result = local("tar -czf {} -v {}".format(output_file, folder_to_archive))

    if result.ok:
        return output_file
    else:
        return None

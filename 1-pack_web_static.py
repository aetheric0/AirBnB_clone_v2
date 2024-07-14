#!/usr/bin/python3
from fabric import task
import os, tarfile
from datetime import datetime

@task
def do_pack(c):
    if not os.path.exists("versions"):
        c.run("mkdir versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    folder_to_archive = 'web_static'
    output_file = 'versions/webstatic_{}.tgz'.format(date)
    result = c.run("tar -czf {} -v {}".format(output_file, folder_to_archive), pty=True, echo=True)

    if result.ok:
        return output_file
    else:
        return None

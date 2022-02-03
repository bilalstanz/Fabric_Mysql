
import logging
import os
from fabric import connection

def sshConnect():
    c = connection.Connection(
        host=os.getenv('VMIP'),
        user=os.getenv('VMUSERNAME'),
        connect_kwargs={
            "key_filename": os.getenv('VMSSHKEY'),
        },
    )
    logging.info('ssh connection established')
    return c

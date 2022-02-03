
# from os import environ
import os
from fabric import connection

c = connection.Connection(
    host=os.environ['VMIP'],
    user=os.environ['VMUSERNAME'],
    connect_kwargs={
        "key_filename": os.environ['VMSSHKEY'],
    },
)
result = c.run('uname -a')
print(result.command)


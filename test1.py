

from sshConnection import sshConnect

# c = sshConnect()
# result = c.run('uname -a')
# print(result.connection)
"""
commands = ['sudo apt update -y',
            # 'sudo apt upgrade -y',
            'sudo apt install mysql-server -y',
            'sudo mysql -u root -p',
            f'ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "{MYSQLPASS}";']
"""

print(MYSQLPASS)

# result = c.run('sudo apt update && sudo apt upgrade -y')
# for com in commands:
#     result = c.run(com, hide=True)
#     if result.ok == True:
#         print(result)
    # print(result.ok)

# if result.ok == True:
#     print('okay')

# result = sshConnect('uname -a')
# print(result.connection)




from os import getenv
from sshConnection import sshConnect

c = sshConnect()
# result = c.run('uname -a')
# print(result.connection)

commands = ['sudo apt update -y',
            # 'sudo apt upgrade -y',
            'sudo apt install mysql-server -y',
            'sudo mysql -u root -p',
            f'ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "{getenv("MYSQLPASS")}";']

# result = c.run('sudo apt update && sudo apt upgrade -y')
for com in commands:
    # result = c.run(com, hide=True)
    result = c.run(com)
    # if result.ok == True:
    #     print(result)
    # print(result.ok)

# if result.ok == True:
#     print('okay')

# result = sshConnect('uname -a')
# print(result.connection)


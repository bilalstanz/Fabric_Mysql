
from os import getenv
from sshConnection import sshConnect


c = sshConnect()
mysqlPass = getenv('MYSQLPASS')

commands = ["sudo apt update -y",

            "sudo apt install mysql-server -y",

            f"sudo mysql -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{mysqlPass}';\"",

            f"sudo mysql -u root -p{mysqlPass} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{mysqlPass}';\"",

            "sudo sed -i 's/127.0.0.1/0.0.0.0/g'  /etc/mysql/mysql.conf.d/mysqld.cnf",

            "sudo systemctl restart mysql.service"]


# result = c.run('sudo apt update && sudo apt upgrade -y')
for comm in commands:
    result = c.run(comm)
    # result = c.run(com, hide=True)
    # if result.ok == True:
    #     print(result)
    # print(result.ok)

# if result.ok == True:
#     print('okay')




import logging
from os import getenv
from sshConnection import sshConnect

c = sshConnect()
mysqlPass = getenv('MYSQLPASS')

update = c.run("sudo apt update -y")

mysqlInstall = c.run("sudo apt install mysql-server -y")

mysqlPassChange = c.run(f"sudo mysql -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{mysqlPass}';\"")

grantPrivileges = c.run(f"sudo mysql -u root -p{mysqlPass} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{mysqlPass}';\"")

replaceLocalHost = c.run("sudo sed -i 's/127.0.0.1/0.0.0.0/g'  /etc/mysql/mysql.conf.d/mysqld.cnf")

restart = c.run("sudo systemctl restart mysql.service")

# if result.ok == True:
#     print('okay')


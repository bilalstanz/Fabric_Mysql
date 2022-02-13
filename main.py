
import logging
from os import getenv
from sshConnection import sshConnect


logging.basicConfig(filename='mysql.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
c = sshConnect()
mysqlPass = getenv('MYSQLPASS')

c.run("sudo apt update -y", hide=True)
logging.info('updating package repo')

logging.info('installing mysql server')
c.run("sudo apt install mysql-server -y", hide=True)

logging.info('changing root password')
c.run(f"sudo mysql -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{mysqlPass}';\"", hide=True)

logging.info('granting privileges')
c.run(f"sudo mysql -u root -p{mysqlPass} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{mysqlPass}';\"", hide=True)

logging.info('configuring mysql')
c.run("sudo sed -i 's/127.0.0.1/0.0.0.0/g'  /etc/mysql/mysql.conf.d/mysqld.cnf", hide=True)

logging.info('restarting mysql')
c.run("sudo systemctl restart mysql.service", hide=True)



from os import getenv
from sshConnection import sshConnect

c = sshConnect()
# result = c.run('uname -a')
# print(result.connection)
# sqlInitialPass = Responder(
#     pattern=r'Enter password:',
#     response='\n')
# c.run('sudo mysql -u root')
mysqlPass = getenv('MYSQLPASS')
c.run("sudo apt update -y")
c.run("sudo apt install mysql-server -y")
c.run(f"sudo mysql -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{mysqlPass}';\"")
c.run(f"sudo mysql -u root -p{mysqlPass} -e \"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '{mysqlPass}';\"")
c.run("sudo sed -i 's/127.0.0.1/0.0.0.0/g'  /etc/mysql/mysql.conf.d/mysqld.cnf")
c.run("sudo systemctl restart mysql.service")

# sqlChangePass = Responder(
#     pattern=r'mysql> ',
#     response=f'ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "{getenv("MYSQLPASS")}";\n')
# c.run(f'ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "{getenv("MYSQLPASS")}";')
# c.run(watchers=[sqlChangePass])
# if result.ok == True:
#     print('okay')

# result = sshConnect('uname -a')
# print(result.connection)


## Mysql server configuration with Fabric over SSH

The purpose of this assignment was to be able to get comfort with the idea of using Fabric
to automate server configuration over SSH.

This script calls your VM or cloud instance and run commands for mysql over
SSH on vm.

```
environment variables required

VMIP='vm ip'
VMUSERNAME='vm username'
VMSSHKEY='private ssh-key path'
MYSQLPASS='mysql database password'
```


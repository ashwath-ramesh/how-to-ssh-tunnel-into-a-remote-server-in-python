# SSH tunnel into a remote server using python
How to SSH tunnel into a remote server using python

Context:
1. You need to SSH tunnel into a remote server to run your python code.
2. Use case, would be a database located in a remote server. For example: db_server_dev and db_server_prod
3. Since you can run the code both on your local machine and remote machine, you want to your code to automatically understand which environment it is in and connect to the appropriate server.

1. Set the correct environment varible for your operating system
2. Use SSHTunnel package in python

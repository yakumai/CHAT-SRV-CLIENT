#--*--coding:UTF-8--*--
import socket
import os
import time
host=""
port=1335

#######################################################################################################################
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(5)
client,adresse=sock.accept()
print adresse
########################################################################################################################
while 1:
    recep = client.recv(2048)
    if recep=='end':
        break
    print ("Client> %s \n") % recep
    envs = raw_input("Server>Envoyer votre message \n")
    client.send(envs)
client.close()
sock.close()
########################################################################################################################

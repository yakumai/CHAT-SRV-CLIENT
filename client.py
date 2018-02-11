#--*--coding:UTF-8--*--
#yakumai
import socket
import time
host="192.168.1.16"
port=1335

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

print("Vous êtes connecté")
while 1:
    req = raw_input("Client>Envoyer votre message \n")
    client.send(req)
    rep=client.recv(2048)
    if req == 'end':
        break
    print ("Server> \n") + rep
client.close()

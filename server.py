#coding=utf-8
import socket
import time

def sendToAll(connections, data):
    for conn in connections:
        conn[0].send(b"msg")
        conn[0].send(data)

playersCount = 2

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(playersCount)

connections = []
for i in range(playersCount):
    connections.append(sock.accept())
    username = sock.recv(1024)
    sendToAll(bytes("User " + username + "connected."))
    print("player.connect")
    print(connections)
    if i < playersCount-1:
        connections[i][0].send(b"wait")
    else:
        sendToAll(connections, b"allPlConnect")


while True:
    for clientNum in range(len(connections)):
        print(clientNum)
        sendToAll(connections, bytes("player " + str(clientNum) + " turn", 'utf8'))
        time.sleep(1)
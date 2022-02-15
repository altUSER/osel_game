#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time

###SETTINGS###
server = "localhost"
port = 9090
##############


username = raw_input("pick username\n>")

print("Connecting to " + server)
sock = socket.socket()
print(sock.connect((server, port)))
#sock.send(bytes(username, "utf-8"))
sock.send(bytes(username))
print("Connected")
time.sleep(1)

while True:
    data = sock.recv(1024)
    print(data)
    if data == "msg":
        print("[SERVER]", sock.recv(1024))
    if data == "exit":
        exit()
    if not data:
        break

sock.close()

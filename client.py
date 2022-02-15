#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

###SETTINGS###
server = "localhost"
port = 9091
##############


username = input("pick username\n>")

print("Connecting to", server)
sock = socket.socket()
sock.connect((server, port))
sock.send(bytes(username, "utf-8"))
print("Connected")
while True:
    data = sock.recv(1024)
    print(data)
    if data == b"msg":
        print("[SERVER]", sock.recv(1024))
    if data == b"exit":
        exit()
    if not data:
        break

sock.close()

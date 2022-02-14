#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9091))

#sock.send('hello, world!')

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data)
    if data == b"exit":
        exit()

sock.close()

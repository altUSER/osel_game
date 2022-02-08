import socket

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(2)
conn1, addr = sock.accept()
conn2, addr = sock.accept()

while True:
    data = conn1.recv(1024)
    if not data:
        break
    conn2.send(data.upper())
    conn1.send("Done")
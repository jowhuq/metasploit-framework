import socket as s
h=s.gethostname()
port=12345
server_socket=s.socket()
server_socket.bind((h, port))
server_socket.listen(1)
conn, address=server_socket.accept()
print("Connected to :"+str(address))
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print("Data recieved is :"+str(data))
    data=input(" Enter a message:")
    conn.send(data.encode())
conn.close()

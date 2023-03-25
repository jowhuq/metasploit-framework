import socket as s
h=s.gethostname()
port=12345
client_socket=s.socket()
client_socket.connect((h, port))
message=input("Enter a message:")
while message.lower().strip()!='exit':
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()
    print("Data recieved is "+ data)
    message=input("Enter:")
client_socket.close()

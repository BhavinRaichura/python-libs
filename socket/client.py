import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 8000

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))

name = input("client name : ")

done =True
while done:
    client.send(input("MESSAGE: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done=False
    else:
        print(msg)

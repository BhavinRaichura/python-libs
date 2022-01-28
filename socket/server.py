import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 8000

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()

client, address = server.accept()

done = True


while done:
    msg = client.recv(1024).decode('utf-8')
    if msg=='quit':
        done = False
    else:
        print(msg)
    client.send(input("message: ").encode('utf-8'))

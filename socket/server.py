import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 8000

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()



done = True


while done:
    client, address = server.accept()
    print(f'connected: {address}')
    while client:
        msg = client.recv(1024).decode('utf-8')
        if msg=='quit':
            done = False
            client.close()
        else:
            print(msg)
        reply=input("message: ") +"--server"
        client.send(reply.encode('utf-8'))

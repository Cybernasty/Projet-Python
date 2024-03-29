import threading
import socket

host = '127.0.0.1'
port = 5566

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
pseudos = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pseudo = pseudos[index]
            broadcast(f'{pseudo} a quitté la conversation'.encode())
            pseudos.remove(pseudo)
            break

def receive():
    while True:
        client,adress = server.accept()
        print(f'Connected with {str(adress)}')
        client.send('NICK'.encode())
        pseudo = client.recv(1024).decode()
        pseudos.append(pseudo)
        clients.append(client)
        print(f'pseudo du client est {str(pseudo)}!')
        broadcast(f'{pseudo} a rejoint la conversation !'.encode())
        client.send('Connecté au serveur !'.encode())

        thread = threading.Thread(target=handle,args =(client,))
        thread.start()

print('Serveur Ecoute')
receive()





import socket
import threading

clients = []


def handleClient(sock, addr):
    print(f'starting new thread for {addr}')
    clients.append(sock)
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f'data from {addr}: {data}')
        for client in clients:
            if client == sock:
                continue
            try:
                client.send(data)
            except:
                clients.remove(client)
                pass


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 6060))
sock.listen()
while True:
    [client, addr] = sock.accept()
    print(f'client connected {addr}')
    threading.Thread(target=handleClient, args=(client, addr,)).start()

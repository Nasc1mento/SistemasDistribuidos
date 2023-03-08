import socket

# configurar os parâmetros do socket do servidor
ip_server = "127.0.0.1"
port_number = 60600
endpoint_server = (ip_server, port_number)
buffer_size = 1024 # o tamanaho máximo de dados recebidos uma vez

# criar uma instância de um novo servidor socket
server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associar o endereço IP e a porta do endpoint local do socket
server_socket_tcp.bind(endpoint_server)

# indicar que o socket está pronto para receber conexão
server_socket_tcp.listen(5)

while True:
    # bloquear processo até chegar uma conexão
    client_connection, client_address = server_socket_tcp.accept()

    while True:
        # ler os dados de um socket TCP (recv)
        data_client = client_connection.recv(buffer_size)
        
        if not data_client:
            break

        response = sum([int(i) for i in str(data_client, 'ascii').split(' ')])
        print("A soma é {}".format(response))

        # enviar dados pelo socket UDP (send)
        client_connection.send(bytes(str(response),'ascii'))
        

    client_connection.close()

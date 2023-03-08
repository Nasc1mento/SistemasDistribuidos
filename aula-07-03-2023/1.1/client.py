import socket

print("Cliente Echo TCP")

# paramêtros para configuração do cliente
ip = "127.0.0.1"
port = 60600
endpoint_server = (ip, port)
buffer_size = 1024

while True:
    # armazenar números do input do cliente
    message = input('')
    data = str.encode(message)

    # cria a instância do novo socket do servidor
    client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # estabelecer a conexão com o endpoint remoto
    client_socket_tcp.connect(endpoint_server)

    # enviar dados pelo socket TCP (send)
    client_socket_tcp.send(data)

    # ler dados de um socket TCP (recv)
    data_server = client_socket_tcp.recv(buffer_size)

    print("A soma é: {}".format(str(data_server,'ascii')))

    client_socket_tcp.close()
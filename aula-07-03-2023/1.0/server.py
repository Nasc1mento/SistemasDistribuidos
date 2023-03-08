import socket


server = socket.socket()

server.bind(('0.0.0.0',7550)) # 0.0.0.0 pra toda rede escutar

server.listen() # ouvindo

while True:
    client = server.accept() # aceitando a conexão
    resposta = client[0].recv(1024) # armazenando a mensagem recebida
    retorno = sum([int(i) for i in str(resposta, 'ascii').split(',')]) # removerndo a virgula com o split, transformando de byte para string
    client[0].send(bytes(str(retorno),'ascii')) # tranformando de byte para string e enviando para o cliente
    print(''+str(retorno)) # mostrando o resultado no console



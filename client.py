import socket 

client = socket.socket()
client.connect(('0.0.0.0',7550)) # colocando o ip do servidor e a porta que abri lá



numeros = input('') # abrindo um input para envio dos numeros, separe por virgula para funcionar

client.send(bytes(numeros, 'ascii') ) # trasformado a string ( o input ) para byte e enviando

result = str(client.recv(1024),'ascii') # recebendo a resposta que o cliente enviou, transformando de byte para string

print('A soma é:',result) # printando o resultado

numeros = '' # acho que isso aqui é inútil
    
client.close() # fechando a conexão



# pode colocar o loop while True para enviar infinitamente
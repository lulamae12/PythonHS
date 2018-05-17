#socket client
import socket
Socket = socket.socket()#create new socket
hostname = socket.gethostname()#get loacl machine name
port = 12345
Socket.connect((hostname, port))
print(Socket.recv(1024))#recive tcp connection
while True:
    userInput = input("Client:")
    message = userInput
    connection.sendto(message.encode(),(hostname, port))
#Socket.close

#socket server to be run with client
import socket
Socket = socket.socket()       #creates new socket
hostname = socket.gethostname()#get hostname for current machine
port = 12345 #set network port
Socket.bind((hostname,port)) #make addres. eg: localhost:8900
ConnectionMessage = ("You have connected to:" + hostname)
Socket.listen(5) #wait five seconds for connection
connection, address = Socket.accept() #make connection with client
print(f"Connected to,",address)
message = ConnectionMessage
connection.sendto(message.encode(),(hostname, port))
while True:
    data = Socket.recv(1024)
    modifiedMessage, serverAddress = clientSocket.recvfrom(message.decode('utf-8'))
    #connection.close()#close connection

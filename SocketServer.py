#server side chat
import socket,os
cls = lambda: os.system('cls')
hostname = socket.gethostname()#get hostname
hostIP = socket.gethostbyname(hostname)#get ip

serverSocket = socket.socket()#create new serverside socket
cls()
print("Hostname: ",hostname)
print("IP: ",hostIP)
ServerIPAddress = input("Enter the ip address for the server: ")
ServerPort = input("Enter the Port for the server to use: ")

serverSocket.bind((ServerIPAddress, int(ServerPort)))#bind to port

serverSocket.listen(5)
client, address = serverSocket.accept()#establish connection with client
ConnectionMessage = ("Connected to:" + str(address))
print(hostname + "has Connected.")
message = ConnectionMessage
client.sendto(message.encode(),(hostname, int(ServerPort)))#send message to client
while True:
        data = client.recv(1024)
        #modifiedMessage, serverAddress = serverSocket.recvfrom(message.decode('utf-8'))
        print('Received message:', client.recv(1024))

client.close()

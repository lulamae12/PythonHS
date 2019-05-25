import socket,select,sys,os
cls = lambda: os.system('cls')

localName = socket.gethostname()
localIP = socket.gethostbyname(localName)
cls()
print("Hostname: ",localName)
print("IP: ",localIP)


port = 12345 #set connection port

IPAddress = input("Enter the ip address of the server: ")
port = input("Enter the port of the server: ")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IPAddress, int(port)))#connect to server
print(server.recv(1024))#print recived data from port 1024 where the server is
while True:

    message = input("->")#get message to send
    #time.sleep(0.4)
    server.sendto(message.encode('utf-8'), (localIP, int(port)))# encrypt message  and send
    server.sendto(message.encode('utf-8'), (localIP, int(port)))# encrypt message  and send
server.close # close when done

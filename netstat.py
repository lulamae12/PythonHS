import speedtest
from wifi import Cell, Scheme
import subprocess,socket,sys
import os
from datetime import datetime

cls = lambda: os.system('cls')

st = speedtest.Speedtest()

def uploadSpeed():
    st.get_best_server()
    upload = float(st.upload())
    upload = (upload / 1000000)
    return upload
def downloadSpeed():
    st.get_best_server()
    download = float(st.download())
    download = (download / 1000000)
    return download

def checkPorts():
    cls()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print("============================================")
    print("Scanning server, ",remoteServerIP)
    print("============================================")
    timeStart = datetime.now()
    
    for port in range(23,1025):
        result = sock.connect_ex((remoteServer,int(port)))
        if result == 0:
            print("Port ",port," is open")
    timeFinish = datetime.now()
    totalTime = timeFinish - timeStart
    print("finished in ", totalTime)
def checkPort(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    result = sock.connect_ex(('76.22.229.4',int(port)))
    if result == 0:
        print("Port is open")
    else:
        print ("Port is not open")
    sock.close()

while True:
    portQues = input("port: ")

    checkPort(portQues)
checkPorts()

while False:

    upload = uploadSpeed()
    download = downloadSpeed()
    cls()
    print('==================================================')
    print('==== download: '+ str(download) + '===')
    print('==== upload: '+str(upload) +'===')
    print('====')
    print('==================================================')
    #cls()

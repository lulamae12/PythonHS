import speedtest
from wifi import Cell, Scheme
import subprocess
import os
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



while True:

    upload = uploadSpeed()
    download = downloadSpeed()
    print('==================================================')
    print('==== download: '+ str(download) +'===')
    print('==== upload: '+ upload) +'===')
    print('==================================================')
    cls()

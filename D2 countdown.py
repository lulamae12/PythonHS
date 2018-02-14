import time
print ("Current date and time")
print (time.strftime("%m/%d/%Y")+' '+(time.strftime("%H:%M:%S")))
def countdown(d):
    print("time till destiny 2")
    while d:
        mins, secs = divmod(d, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end ='\n')
        
        time.sleep(1)
        d -= 1
    print ('goodbye! \n \n \n')
d = 30
countdown(d)
    

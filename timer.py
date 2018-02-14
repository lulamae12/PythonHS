import time
d = 60
def countdown(d):
    print("this timer will last for 1 minute. it will begin in 5 seconds.")
    time.sleep(5)
    while d != 0:
        print("there are " + str(d) + " seconds left")
        time.sleep(1)
        d = d - 1
        d -= 0
countdown(60)

import random
import time
def rtd():
    colors = ["Red","Blue","Green","Yellow","Purple","Orange"]
    numbers = random.randint(1,6)
    print('rolling number die.....')
    time.sleep(1)
    print('the number is:' + str(numbers))
    time.sleep(1)
    print('rolling color die.....')
    time.sleep(1)
    print('the color is:' + random.choice(colors))
rtd()

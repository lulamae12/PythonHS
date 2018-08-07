import random
places = ['Junk Junction', 'Anarachy Acres', 'Risky Reels', 'Haunted Hills', 'Pleasent Park', 'Loot Lake', 'Tomato Town', 'Wailing Woods', 'Snobby Shores', 'Tilted Towers', 'Dusty Divot', 'Retail Row', 'Lonely Lodge', 'Greasy Grove', 'Shifty Shafts', 'Salty Springs', 'Flush Factory', 'Fatal Fields',
 'Lucky Landing', 'Moistry Mire']
gridLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
while True:
    redo = input("hit ENTER to find a place to drop.")
    letter = random.choice(gridLetters)
    place = random.choice(places)
    #print("\ndrop at: " + letter + "," + str(random.randint(1,10)))
    print(place +"\n")

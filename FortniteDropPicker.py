import random
places = ['Junk Junction', 'Anarachy Acres', 'Risky Reels', 'Haunted Hills', 'Pleasent Park', 'Loot Lake', 'Tomato Town', 'Anarachy Acres', 'Wailing Woods', 'Snobby Shores', 'Tilted Towers', 'Dusty Divot', 'Retail Row', 'Lonely Lodge', 'Greasy Grove', 'Shifty Shafts', 'Salty Springs', 'Flush Factory', 'Fatal Fields',
 'Lucky Landing', 'Moistry Mire']
gridLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
letter = random.choice(gridLetters)
place = random.choice(places)
print("drop at: " + letter + "," + str(random.randint(1,10)))
print("or, " + place)

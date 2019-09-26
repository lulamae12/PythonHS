word = input("Word: ")
wordList = word.split()
flippedSen = []
for i in range(len(wordList)):
    
    if i % 2 == 0: #even
        flippedSen.append(wordList[i])
    if i % 2 != 0: #odd
        flippedSen.append(wordList[i][::-1])
print(flippedSen)
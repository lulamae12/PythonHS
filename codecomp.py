userInput = input("input up to 5 words")
userInputList = userInput.split()
spot = 0
for item in range(len(userInputList)):
    print(userInputList[item] + "  "+ userInputList[item + 1] +  "  "+ userInputList[item + 2] +  "  "+ userInputList[item + 3] +  "  "+  userInputList[item + 4])

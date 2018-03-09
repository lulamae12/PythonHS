dictionary = {'apple': 'a red fruit', 'banana': 'a yellow fruit', 'orange': 'a orange fruit'}
wordchoice = input('enter a word to look up:')
if wordchoice in dictionary:
    print (dictionary[wordchoice])
else:
    print("Word not found!")

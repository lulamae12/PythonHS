word = input("enter a word: ")
word = word.lower()
wordflipped = ''.join(reversed(word))
if word == wordflipped:
    print("its a palindrome")
else:
    print("its not a palindrome")

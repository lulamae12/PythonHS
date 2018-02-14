def main():
    message = input("please enter your message:")
    x = 1
    flipped = ''
    i = len(message) - 1
    while i >= 0:
        flipped = flipped + message[i]

        i = i - 1
    print(f"your reversed chiper is:",flipped)

    while x == 1:
        playagain = input("would you like to enter another word?(y/n)")
        if playagain == 'n':
            x = 0
            print('Ok. quitting..')
        if playagain == 'y':
            x = 0
            main()
        if playagain != 'y' and playagain != "n":
            print("that is not a valid input! Please enter, 'y' or 'n'! ")
main()

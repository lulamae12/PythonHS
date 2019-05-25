import random,sys

def playGame():
	randomNumber = (random.randint(0,9) + 1)
	guess = input("guess the number between 1 and 10: ")
	if int(guess) == randomNumber:
		print("congratulations! you guessed correctly!")
	else:
		print("wrong!, the number was: " + str(randomNumber))


	playAgain = input("play again? (y,N): ")
	if playAgain.lower() == 'y':
		playGame()

	else:
		sys.exit()

playGame()

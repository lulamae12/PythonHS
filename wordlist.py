import random
def words():
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]

    chosen_word = random.choice(words).lower()
    player_guess = None # will hold the players guess
    guessed_letters = [] # a list of letters guessed so far
    word_guessed = []
    for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
    joined_word = None # joins the words in the list word_guessed
words()

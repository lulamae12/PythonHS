import markovify





def chat():
    with open("rhap.txt",encoding='utf8') as file:
        corpus = file.read()
    #build model
    model = markovify.Text(corpus,state_size=1)

    chain = model.make_short_sentence(100) 
    print("\n",chain)



#def checkGrammar









for i in range(5):
    chat()
    print("")
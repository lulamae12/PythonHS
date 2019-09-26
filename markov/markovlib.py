import markovify





def chat():
    with open("rhap.txt",encoding='utf8') as file:
        corpus = file.read()
    #build model
    model = markovify.Text(corpus,state_size=2)

    chain = model.make_sentence() 
    print("\n",chain)



#def checkGrammar










chat()
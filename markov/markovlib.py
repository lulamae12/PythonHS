import markovify





def chat():
    with open("trumpSpeeches.txt",encoding='utf8') as file:
        corpus = file.read()
    #build model
    model = markovify.Text(corpus,state_size=2)

    chain = model.make_sentence() 
    print("\n",chain)



#def checkGrammar









for i in range(3):
    chat()
    print("")
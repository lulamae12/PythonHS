import numpy as np

trumpSpeeches = open("rhap.txt",encoding='utf8').read()
corpus = trumpSpeeches.split()

def makeWordPairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i],corpus[i+1])#yield like return but doesnt quit
#pairs = makeWordPairs(corpus)

def cleanWords(corpus):
    
    print(len(corpus))
    for i in range(len(corpus)-1):
        
        if corpus[i] == "TRUMP:":
            print(corpus[i])
            print(i)
            corpus.remove(corpus[i])
            print('removed')
        if corpus[i] == '"':
            corpus.remove(corpus[i])

def pairWords(pairs):
    wordPairs = {}
    for word1, word2 in pairs:
        if word1 in wordPairs:
          wordPairs[word1].append(word2)
        else:
          wordPairs[word1] = [word2]
    return wordPairs

def startChain(wordCount,corpus,pairs):
    #pick random word to start chain
    wordPairs = pairs
    puncList =[".","!","?"]
    firstWord = np.random.choice(corpus)
    while firstWord.islower():
        firstWord = np.random.choice(corpus)
    markovChain = [firstWord]

    numWords = wordCount

    for i in range(numWords):
        markovChain.append(np.random.choice(wordPairs[markovChain[-1]]))
        print(markovChain[len(markovChain)-1])
    #while markovChain[len(markovChain)-1]:
     #   markovChain.append(np.random.choice(wordPairs[markovChain[-1]]))
    print(' '.join(markovChain))





try:
    cleanWords(corpus)
except:
    pass

pairs = makeWordPairs(corpus)
wordPairs = pairWords(pairs)
startChain(30,corpus,wordPairs)



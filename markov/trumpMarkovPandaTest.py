import pandas as pd
from numpy.random import choice
import sys
#trumpSpeeches = "nothing david dobrik ever does will wash away the taste of that lion peeing in his mouth. david if you see this i want you to know you are going to know what lion pee tastes like for the rest of your life. you're disgusting"
trumpSpeeches = open("trumpSpeeches.txt",encoding='utf8').read()
corpus = trumpSpeeches.split()

df = pd.DataFrame(columns=['leading', 'following', 'freq'])#leading word is first word and following is word following leading word and freq is the amount of times that pair appears
df['leading']=corpus#set all words in corpus to lead collumn

following = corpus[1:]#shift all words up
following.append("ENDWORD")


endWords = []#find words that end sentences correctly
for word in corpus:
    if word[-1] in  ['.','!','?'] and word != '.':
        endWords.append(word)
    
#print("END WORDS: ",endWords)
print("DATAFRAME")
print(df)




df['freq']= df.groupby(by=['leading','following'])
['leading','following'].transform('count').copy()#count occurence of leading and following


print("lead len",len((df["leading"])))
print("follow len",len((df["following"])))
print("freq len",len((df["freq"])))


#pivot makes it to a matrix kinda like this
#        FOLLOWING   FOLLOWING  FOLLOWING
#LEADING    VAL         VAL         VAL
#LEADING    VAL         VAL         VAL
#LEADING    VAL         VAL         VAL
#
#And val is the freq of the intersecting words

df = df.drop_duplicates()#remove dupes

pivotDataframe = df.pivot(index= 'leading',columns= 'following', values='freq')
sumOfWords = pivotDataframe.sum(axis=1)
pivotDataframe = pivotDataframe.apply(lambda x: x/sumOfWords)

def makeSentence(start, senLen):
    startingWord = start
    sentence = [startingWord]
    while len(sentence) <senLen:
        nextWord = choice(a = list(pivotDataframe.columns), p = (pivotDataframe.iloc[pivotDataframe.index == startingWord].fillna(0).values)[0])#iloc gets location on axis and fillna fills all unknow values

        if nextWord == 'ENDWORD':
            continue
        elif nextWord in endWords:
            if len(sentence) > 2: #add ending word
                sentence.append(nextWord)
                break
            else:#keep going till ending word
                continue
        else:
            sentence.append(nextWord)#add next word to sen based off predict
        startingWord=nextWord
    sentence = " ".join(sentence)
    return sentence
sentence = makeSentence("Donald",30)
import random
def getcards():
    tfile = open('cards.txt', 'r')
    lines = (tfile).read().splitlines()
    x = 1
    while x == 1:
        card1 = random.choice(lines)
        card2 = random.choice(lines)
        card3 = random.choice(lines)
        card4 = random.choice(lines)
        card5 = random.choice(lines)
        allsamesuit = False
        allsamerank = False
        card1rank = card1.split("|")[0].replace("\n","")
        card1suit = card1.split("|")[1].replace("\n","")
        card1value = card1.split("|")[2].replace("\n","")

        card2rank = card2.split("|")[0].replace("\n","")
        card2suit = card2.split("|")[1].replace("\n","")
        card2value = card2.split("|")[2].replace("\n","")

        card3rank = card3.split("|")[0].replace("\n","")
        card3suit = card3.split("|")[1].replace("\n","")
        card3value = card3.split("|")[2].replace("\n","")

        card4rank = card4.split("|")[0].replace("\n","")
        card4suit = card4.split("|")[1].replace("\n","")
        card4value = card4.split("|")[2].replace("\n","")

        card5rank = card5.split("|")[0].replace("\n","")
        card5suit = card5.split("|")[1].replace("\n","")
        card5value = card5.split("|")[2].replace("\n","")
        cardranknum = int(card1rank) + int(card2rank) + int(card3rank) + int(card4rank) + int(card5rank)
        print(card1, card2, card3, card4, card5)
        hand = [card1, card2, card3, card4, card5]
        handranks = [card1rank, card2rank, card3rank, card4rank, card5rank]

        handrankdupes = [x for x in handranks if handranks.count(x) > 1]
        if len(handrankdupes) > 0:
            handrankduplicates = True
        else:
            handrankduplicates = False



        handsuits = [card1suit, card2suit, card3suit, card4suit, card5suit]
        handsuitdupes = [x for x in handsuits if handsuits.count(x) > 1]
        if len(handsuitdupes) > 0:
            handsuitduplicates = True
        else:
            handsuitduplicates = False

        handvalues = [card1value, card2value, card3value, card4value, card5value]
        handvaldupes = [x for x in handvalues if handvalues.count(x) > 1]
        if len(handvaldupes) > 0:
            handvalduplicates = True
        else:
            handvalduplicates = False
        print(cardranknum)
        print(hand)
        #for value in handvalues:


        if card2suit == card1suit == card5suit == card3suit == card4suit:
            allsamesuit = True
        if card2rank == card1rank == card5rank == card3rank == card4rank:
            allsamerank = True



    #FLUSH
        if allsamesuit == True and cardranknum != 55:
            print("Flush")
            x = 0
    #Royal FLUSH
        if allsamesuit == True and cardranknum == 55 and handvalduplicates == False:
            print("Royal Flush")
            x = 0
    #straightFlush

    #
        #if allsamesuit == True and cardranknum == 55 and handvalduplicates == False:







getcards()

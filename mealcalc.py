appcost = int(input("appetizer cost:"))
entrecost = int(input("entre cost:"))
toto = appcost + entrecost
tplustax = int(toto) *  0.925
fullcost = tplustax + toto
print("total meal cost:" + str(fullcost))

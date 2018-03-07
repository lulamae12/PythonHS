import math, pyperclip

def main():
    myMessage ="""T 
t
ntuAycnrsP 
erensi ueyiW u.s?pcentshoe
w
hi sh er ae
epoionn f.rErhrtno bo	
x e i tuor 
pirFva st OWls.aelcihtrha 
l lan h
iidstosgoebcnieowe f .h,f
 s t c	  f
b shtoAeteTlyeehmnnhrhoon epdcoeecus  o
rrn k i sucyotP tt un.pu ysoi bd	tgttt v e Nihhhrcelxeoolaouo.opxtnynncm
grp
 ,  tp
ierdc tluaMcse.ihharruass	poeniellisMhw gn t oiae tugsionoyrtra tppsnb hagorle  euenefiermt
s s  n auo
eCpicgCts Ssaososhotbh es d,or eoasine i,b rrato.bc ettrrit
ueo r a o"""
    myKey = 41

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

def brute(msg):
    for key in range(1,len(msg)+1):
        print(f"Key: {key}")
        print(decryptMessage(key,msg))
# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    print("what would u like to do?")
    print("1. brute")
    print("2. norm")
    choice = input("choice >>> ")
    if choice == "1":
        brute("""T 
t
ntuAycnrsP 
erensi ueyiW u.s?pcentshoe
w
hi sh er ae
epoionn f.rErhrtno bo	
x e i tuor 
pirFva st OWls.aelcihtrha 
l lan h
iidstosgoebcnieowe f .h,f
 s t c	  f
b shtoAeteTlyeehmnnhrhoon epdcoeecus  o
rrn k i sucyotP tt un.pu ysoi bd	tgttt v e Nihhhrcelxeoolaouo.opxtnynncm
grp
 ,  tp
ierdc tluaMcse.ihharruass	poeniellisMhw gn t oiae tugsionoyrtra tppsnb hagorle  euenefiermt
s s  n auo
eCpicgCts Ssaososhotbh es d,or eoasine i,b rrato.bc ettrrit
ueo r a o
""")
    elif choice == "2":
        main()
    main()

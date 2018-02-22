from math import ceil
key = 0
message = ""
def menu():
    print('________________________')
    print('|Please select a choice:|')
    print('|1.decrypt trasnpostion-|')
    print('|2.encrypt trasnpostion-|')
    print('|_______________________|')
    mode = int(input())
    if mode == 2:
        encrypt()
def encrypt():
    key = int(input("Please enter your key:"))
    message = str(input("Please enter your message to encrypted:"))
    encryptls = []
    biglist = []
    messagelength = len(message)
    amounttorun = ceil(messagelength / key)
    ATRint = int(amounttorun)
    counter = 0
    print(message)
    while counter != amounttorun:
        splicedls = list(message)[0+(key*counter):key+(key*counter)]
        while len(splicedls) < key: splicedls.append("|")
        print(splicedls)
        counter += 1
        biglist.append(splicedls)

    for num in range(key):
        encryptls.append("".join(i[num] for i in biglist))

    print("".join(encryptls))
menu()

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
    result = []
    final = []
    messagelength = len(message)
    amounttorun = ceil(messagelength / key)
    ATRint = int(amounttorun)
    counter = 0
    print(message)
    while counter != amounttorun:
        for char in message:
            encryptls += char

        splicedls = list(message)[0+(key*counter):key+(key*counter)]
        while len(splicedls) < key: splicedls.append("|")
        print(splicedls)
        counter += 1
        result.append(splicedls)
    for eachlist in result:
        final.append("".join(eachlist))
    for num in range(key):
        print("".join(final[num]))
menu()

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
    messagelength = len(message)
    amounttorun = messagelength / key
    ATRint = int(amounttorun)
    print(message)
    for i in range (ATRint):
        for char in message:
            encryptls += char

        splicedls = encryptls[0:key]
        print(splicedls)
        amounttorun - 1
        if amounttorun == 0:
            break
menu()

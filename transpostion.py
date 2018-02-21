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
    for char in message:
        encryptls += char
    splicedls = encryptls[0:key]
    print(encryptls)
    print(splicedls)
menu()

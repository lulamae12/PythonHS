import string
alpha  = list(string.ascii_lowercase)
def encryptOrdecrypt():
    print('________________________')
    print('|Please select a choice:|')
    print('|1.decrypt--------------|')
    print('|2.encrypt--------------|')
    print('|_______________________|')
    mode = input()
    return mode
def MessageToEncryptOrDecrypt():
    print('Please enter your message:')
    message = input()
    return message
def GetShift():
    shift = 0
    while True:
        print("enter your shift:")
        shift = int(input())
        if shift >= 0 and shift <= 25:
            return shift
        if mode == '2':
            EncryptedMessage()
def EncryptedMessage(message, shift):
    Encryptedmessage = ''
    ls = list(message)
    newmessage = []
    for letter in ls:
        if not letter.isalpha():
            newmessage.append(letter)
        else:
            index = alpha.index(letter)
            newIndex = index + shift
            newmessage.append(alpha[newIndex])
        #return newmessage
    print("your encrypted message is:" + "".join(newmessage))


mode = encryptOrdecrypt()
message = MessageToEncryptOrDecrypt()
shift = GetShift()
EncryptedMessage(message, shift)

import string
alphabet  = list(string.ascii_lowercase)
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
        if mode == '2' or mode == '1':
            EncryptedOrDecryptedMessage()
def EncryptedOrDecryptedMessage(message, mode, shift):
    if mode == '2':
        Encryptedmessage = ''
        ls = list(message)
        newmessage = []
        for letter in ls:
            if not letter.isalpha():
                newmessage.append(letter)
            else:
                index = alphabet.index(letter)
                newIndex = index + shift
                newmessage.append(alphabet[newIndex])
                #return new encryoted message
        print("your encrypted message is:" + "".join(newmessage))
    if mode == '1':
        decryptedmessage = ''
        ls = list(message)
        newmessage = []
        for letter in ls:
            if not letter.isalpha():
                newmessage.append(letter)
            else:
                index = alphabet.index(letter)
                newIndex = index - shift
                newmessage.append(alphabet[newIndex])
                    #return new decrypted message
        print("your decrypted message is:" + "".join(newmessage))

mode = encryptOrdecrypt()
message = MessageToEncryptOrDecrypt()
shift = GetShift()
EncryptedOrDecryptedMessage(message, mode, shift)

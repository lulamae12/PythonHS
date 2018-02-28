#dont forget to change key, modulus and string length.

import string
alphabet  = list(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
def encryptOrdecrypt():
    print('________________________')
    print('|Please select a choice:|')
    print('|1.decrypt--------------|')
    print('|2.encrypt--------------|')
    print('|3.bruteforce-----------|')
    print('|_______________________|')
    mode = int(input())

    return mode
def MessageToEncryptOrDecrypt():
    print('Please enter your message:')
    message = str.lower(input())
    return message
def bruteforce():
    num = 0
    if mode == 3:
        for shift in range(0,95):
            decryptedmessage = ''
            ls = list(message)
            newmessage = []

            for letter in ls:

                if not letter.isalpha():
                    newmessage.append(letter)
                else:
                    index = alphabet.index(letter)
                    try:
                        newIndex = index - shift
                    except IndexError:
                        newIndex = 95 - index - shift
                    newmessage.append(alphabet[newIndex])
            num + 1
            print("your decrypted message is:" + "".join(newmessage) + ' with a shift of:' + str(shift))

    if mode != 3:
        pass
def GetShift():
    if mode < 3 and mode > 0:
        shift = 0
        while True:
            print("enter your shift:")
            shift = int(input())
            if shift >= 0 and shift <= 25:
                return shift
                if mode == '2' or mode == '1':
                    EncryptedOrDecryptedMessage()

    if mode == 3:
        pass

# just needed to add modulus to handle when the number went out of the range

def EncryptedOrDecryptedMessage(message, mode, shift):
    if mode == 2:
        Encryptedmessage = ''
        ls = list(message)
        newmessage = []
        for letter in ls:

            index = alphabet.index(letter)
            newIndex = index + shift
            newmessage.append(alphabet[newIndex%95])
                #return new encryoted message
        print("your encrypted message is:" + "".join(newmessage))
    if mode == 1:
        decryptedmessage = ''
        ls = list(message)
        newmessage = []
        for letter in ls:


            index = alphabet.index(letter)
            newIndex = index - shift
            newmessage.append(alphabet[newIndex%95])
                    #return new decrypted message
        print("your decrypted message is:" + "".join(newmessage))

mode = encryptOrdecrypt()

message = MessageToEncryptOrDecrypt()


shift = GetShift()
bruteforce()
EncryptedOrDecryptedMessage(message, mode, shift)

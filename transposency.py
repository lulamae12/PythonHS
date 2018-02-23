import pyperclip
def messaeg():

    message = "this the trasnpostion chiper"
    key = 8
    chipertext = encryptedmessage(key,message)
    print(chipertext + '|')
    pyperclip.copy(chipertext)
messaeg

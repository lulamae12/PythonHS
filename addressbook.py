import json
addressbook = {}
def menu():
    while True:
        print("╔═════════════════╗")
        print("║1.─Add contacts──╢")
        print("║2.─View contacts─╢")
        print("╚═════════════════╝")
        try:
            choice = int(input("Enter your choice:"))
            if choice < 1:
                print('That is not a valid input.')
            if choice > 2:
                print('That is not a valid input.')
            if choice == 1:
                addcontact()
                break
            if choice == 2:
                viewcontacts()
                break
        except(ValueError):
            print('that is not a vaild input.')


def addcontact():
    while True:
        try:
            print('when done, type "done"')
            print('please seperate data with a colon. i.e. (bob:555-123-4567)')
            your_input = input("New contact:")
            key = your_input.split(":")[0]
            val = your_input.split(":")[1]
            addressbook.update({key:val})
            print(addressbook)

        except(IndexError):
            if 'done' not in your_input:
                print('please enter the data correctly')
            if 'done' in your_input:
                json.dump(addressbook, open("addressbookdata.json","a"),indent = 4)
                break

def viewcontacts():
    contacts = json.load(open("addressbookdata.json","r"))
    for contact in contacts:
        print(contact, contacts[contact])
    







menu()

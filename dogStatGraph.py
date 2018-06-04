#python program using matplotlib that graphs the dogs weight and ear length.
import matplotlib as mpl
import numpy as np
from datetime import datetime#dont have to do datetime twice
import json, os
cls = lambda: os.system('cls')
dataTypes = ('EAR LENGTH', 'EL', 'LEN', 'WEIGHT', 'W', 'WGT')
def startMenu():
    cls()
    while True:
        print('╔═════════════════╗')
        print('║1.─Veiw Data─────╢')
        print('║2.─Update Data───╢')
        print('╚═════════════════╝')
        try:
            choice = int(input('Enter your choice:'))
            if choice == 1:#veiw the data
                break
            elif choice == 2:
                updateData(dataTypes)
                break
            else:
                cls()
                print('That is not a valid input.')
        except(ValueError):
            cls()
            print('That is not a valid input!')
def updateData(dataType):
    selectedData = 'null'
    while True:
        print('which data would you like to update? (Ear length or Weight)')
        dataToUpdate = input('Data Type:').upper()
        if dataToUpdate in dataType:
            break
        else:
            cls()
            print('That is an unrecognized data type! The acceptable inputs for the data types are as follows (they are case insensitive!):\n\nEar Length:',dataType[0:3],"\nWeight:", dataType[4:6],"\n")

    if dataToUpdate in dataType[0:3]:
        selectedData = "Ear Length"
        cls()
        print('Currently Updating:',selectedData)
        while True:
            try:
                newEarLength = float(input('Please enter the ear length in inches to the nearest tenth:'))
                date = datetime.today().strftime('%m/%d/%y')
                break
            except(ValueError):
                print(newEarLength,' is invalid! Please enter just the number with no unit identifier.')
        cls()
        while True:
            print('You are about to enter new data for', selectedData,'\nThe data to be entered is:',newEarLength,'Inches, for the date:',date)
            dataVerified = input('Please verify that this data is correct?(y,n):').lower()
            if dataVerified == 'y':
                eardata = ({'Date':date, 'Length':newEarLength})
                print(eardata)
                json.dump(eardata, open("dogLengthStats.json","a"),indent = 4)
                print('Data entered!')
                gotomenu = input('Press any key to return to the main menu.')
                startMenu()
                break
            elif dataVerified == 'n':
                gotomenu = input('Data will not be added. Press any key to return to the main menu.')
                startMenu()
                break
            else:
                print('That is not a valid input!')
    elif dataToUpdate in dataType[4:6]:
        selectedData = 'Weight'
        cls()
        print('currently updating:',selectedData)
        while True:
            try:
                newWeight = float(input('Please enter the weight in pounds to the nearest tenth:'))
                date = datetime.today().strftime('%m/%d/%y')
                break
            except(ValueError):
                print(newWeight,' is invalid! Please enter just the number with no unit identifier.')
        cls()
        while True:
            print('You are about to enter new data for', selectedData,'\nThe data to be entered is:',newWeight,'Pounds, for the date:',date)
            dataVerified = input('Please verify that this data is correct?(y,n):').lower()
            if dataVerified == 'y':
                weightData = ({'Date':date, 'Weight':newWeight})
                print(weightData)
                json.dump(weightData, open("dogWeightStats.json","a"),indent = 4)
                print('Data entered!')
                gotomenu = input('Press any key to return to the main menu.')
                startMenu()
                break
            elif dataVerified == 'n':
                gotomenu = input('Data will not be added. Press any key to return to the main menu.')
                startMenu()
                break
            else:
                print('That is not a valid input!')

startMenu()

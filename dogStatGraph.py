#python program using matplotlib that graphs the dogs weight and ear length.
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime#dont have to do datetime twice
from datetime import date
from dateutil import relativedelta
from sys import exit

import os,dateutil
cls = lambda: os.system('cls')
dataTypes = ('EAR LENGTH', 'EL', 'LEN', 'WEIGHT', 'W', 'WGT')
def startMenu():
    cls()
    while True:
        print('╔═════════════════╗')
        print('║1.─Veiw Data─────╢')
        print('║2.─Update Data───╢')
        print('║3.─Puppy Stats───╢')
        print('║4.─Quit──────────╢')
        print('╚═════════════════╝')
        try:
            choice = int(input('Enter your choice:'))
            if choice == 1:#veiw the data
                cls()
                while True:
                    print('╔════════════════════════╗')
                    print('║1.─Veiw All Data────────╢')
                    print('║2.─Veiw Weight Data─────╢')
                    print('║3.─Veiw Ear Length Data─╢')
                    print('╚════════════════════════╝')
                    try:
                        choice = int(input('Enter your choice:'))
                        if choice == 1:#veiw the data
                            veiwAllData()
                            break
                        elif choice == 2:
                            veiwWeightData()
                            break
                        elif choice == 3:
                            veiwELData()
                            break
                        else:
                            cls()
                            print('That is not a valid input.')
                    except(ValueError):
                        cls()
                        print('That is not a valid input!')
                break
            elif choice == 2:
                updateData(dataTypes)
                break
            elif choice == 3:
                puppyStats()
                break
            elif choice == 4:
                print("quitting...")
                exit()
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
                earLengths = open('dogLengthStatsLen.txt', 'a')
                earLengths.write(str(newEarLength))
                earLengths.write('\n')
                earLengths.close()
                earDates = open('dogLengthStatsDates.txt', 'a')
                earDates.write(str(date))
                earDates.write('\n')
                earDates.close()
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
                dogWeight = open('dogWeigthStatsWeight.txt', 'a')
                dogWeight.write(str(newWeight))
                dogWeight.write('\n')
                dogWeight.close()
                wheightDates = open('dogWeigthStatsDates.txt', 'a')
                wheightDates.write(str(date))
                wheightDates.write('\n')
                wheightDates.close()
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

def veiwAllData():#graph the data
    earLengthList = []
    earDateList = []
    weightList = []
    weightDateList = []
    earDateNum = 0
    weightDateNum = 0
    earLengths = open('dogLengthStatsLen.txt', 'r')
    for line in earLengths:
        cleanedline = line.strip()#gets rid of return char
        earLengthList.append(float(cleanedline))
    earLengths.close()
    earDates = open('dogLengthStatsDates.txt', 'r')
    for line in earDates:
        cleanedline = line.strip()#gets rid of return char
        earDateList.append(cleanedline)
    earDates.close()
    dogWeight = open('dogWeigthStatsWeight.txt', 'r')
    for line in dogWeight:
        cleanedline = line.strip()#gets rid of return char
        weightList.append(float(cleanedline))
    dogWeight.close()
    wheightDates = open('dogWeigthStatsDates.txt', 'r')
    for line in wheightDates:
        cleanedline = line.strip()#gets rid of return char
        weightDateList.append(cleanedline)
    wheightDates.close()
    earX = []#make new list for dates for the ear
    for item in earDateList:#for every date add num to list to show how many to have
        earDateNum += 1#add one to count
        earX.append(earDateNum)#append to list
    '''ear graph'''
    earLenXAxis = earDateList#put on axis num of times.
    plt.xticks(earX, earLenXAxis)
    plt.plot(earX, earLengthList, linestyle='-', marker='o', color='b')
    plt.ylabel('Ear Length (Inches)')
    plt.xlabel('Date')
    plt.title('Ear Length')
    plt.figure()
    '''weight graph'''
    weightX = []#make new list for dates for the ear
    for item in weightDateList:#for every date add num to list to show how many to have
        weightDateNum += 1#add one to count
        weightX.append(weightDateNum)#append to list
    weightXAxis = weightDateList#put on axis num of times.
    plt.xticks(weightX, weightXAxis)
    plt.plot(weightX, weightList, linestyle='-', marker='o', color='b')
    plt.ylabel('Weight (Pounds)')
    plt.xlabel('Date')
    plt.title('Weight')
    plt.show()
def veiwWeightData():
    weightList = []
    weightDateList = []
    weightDateNum = 0
    dogWeight = open('dogWeigthStatsWeight.txt', 'r')
    for line in dogWeight:
        cleanedline = line.strip()#gets rid of return char
        weightList.append(float(cleanedline))
    dogWeight.close()
    wheightDates = open('dogWeigthStatsDates.txt', 'r')
    for line in wheightDates:
        cleanedline = line.strip()#gets rid of return char
        weightDateList.append(cleanedline)
    wheightDates.close()
    weightX = []#make new list for dates for the ear
    for item in weightDateList:#for every date add num to list to show how many to have
        weightDateNum += 1#add one to count
        weightX.append(weightDateNum)#append to list
    weightXAxis = weightDateList#put on axis num of times.
    plt.xticks(weightX, weightXAxis)
    plt.plot(weightX, weightList, linestyle='-', marker='o', color='b')
    plt.ylabel('Weight (Pounds)')
    plt.xlabel('Date')
    plt.title('Weight')
    plt.show()
def veiwELData():
    earLengthList = []
    earDateList = []
    earDateNum = 0
    earLengths = open('dogLengthStatsLen.txt', 'r')
    for line in earLengths:
        cleanedline = line.strip()#gets rid of return char
        earLengthList.append(float(cleanedline))
    earLengths.close()
    earDates = open('dogLengthStatsDates.txt', 'r')
    for line in earDates:
        cleanedline = line.strip()#gets rid of return char
        earDateList.append(cleanedline)
    earDates.close()
    earX = []#make new list for dates for the ear
    for item in earDateList:#for every date add num to list to show how many to have
        earDateNum += 1#add one to count
        earX.append(earDateNum)#append to list
    '''ear graph'''
    earLenXAxis = earDateList#put on axis num of times.
    plt.xticks(earX, earLenXAxis)
    plt.plot(earX, earLengthList, linestyle='-', marker='o', color='b')
    plt.ylabel('Ear Length (Inches)')
    plt.xlabel('Date')
    plt.title('Ear Length')
    plt.show()
def puppyStats():
    name = 'Ruby Smith'
    dob = '03/27/18'
    pob = 'Science Hill, Kentucky'#place of birth
    parents = 'Roscoe and Shelby Haney'
    dobDate = date(2018, 3, 27)

    today = date.today()
    age = dateutil.relativedelta.relativedelta(today, dobDate)
    age = today - dobDate



    print('╔══════════════════════════════════════╗')
    print('║Name:  ',name,'───────────────────╢')
    print('║Age:   ',age,'─────────────╢')
    print('║Birthplace: ',pob,'──╢')
    print('║Parents: ',parents,'────╢')
    print('╚══════════════════════════════════════╝')

startMenu()

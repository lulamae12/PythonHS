from datetime import timedelta
import time
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import sys
#def getdate():

def choicemenu():
    while True:
        print('________________________')
        print('|Please select a choice:|')
        print('|1.Dow 30---------------|')
        print('|2.non Dow 30-----------|')
        print('|3.my stocks------------|')
        print('|4.Find a stock---------|')
        print('|5.Quit-----------------|')
        print('|_______________________|')

        try:
            choice = int(input())

            if choice > 5 or choice < 1:
                print('that is not a valid choice')
            if choice == 1:
                dow30stocks()
                break
            if choice == 2:
                nondow30stocks()
                break
            if choice == 3:
                mystocks()
            if choice == 4:
                findstock()
                break
            if choice == 5:

                #4 the aesthetic
                print("quitting.")
                time.sleep(.5)
                print("quitting..")
                time.sleep(.5)
                print('quitting...')
                sys.exit()
        except(ValueError):
            print("please enter a valid number.")




def findstock():
    cont = 1
    while True:
        print("please enter the EXACT name of the stock ticker")
        stockticker = input()
        if len(stockticker) < 5:
            style.use('ggplot')
            start = dt.datetime.now() - timedelta(days=1)
            end = dt.datetime.now()
            fullstockinfo = web.DataReader(stockticker, "google", start, end)


            print(fullstockinfo.head())
        else:
            #my current knowledge of python will not allow me to find a way to supress traceback. so this is my solution
            print("\nERROR: please make sure the stock ticker is, at most,\nfour characters in length and, is a valid stock.\n")
            #newdf = fullstockinfo[['Close']]
            #print(newdf)
        print('____________________________ ')
        print('|What would you like to do?:|')
        print('|1.Enter another stock------|')
        print('|2.Go back to the main menu-|')
        print('|3.Quit---------------------|')
        print('|___________________________|')
        try:
            menuchoice = int(input())

            while cont == 1:
                if menuchoice == 2:
                    cont = 0
                    choicemenu()
                if menuchoice == 1:
                    cont = 0
                    findstock()
                if menuchoice == 3:
                    cont = 0
                    #4 the aesthetic
                    print("quitting.")
                    time.sleep(.5)
                    print("quitting..")
                    time.sleep(.5)
                    print('quitting...')
                    sys.exit()
        except(ValueError):
            print('please enter a valid number.')
            print('____________________________ ')
            print('|What would you like to do?:|')
            print('|1.Enter another stock------|')
            print('|2.Go back to the main menu-|')
            print('|3.Quit---------------------|')
            print('|___________________________|')
            menuchoice = int(input())

            while cont == 1:
                if menuchoice == 2:
                    cont = 0
                    choicemenu()
                if menuchoice == 1:
                    cont = 0
                    findstock()
                if menuchoice == 3:
                    cont = 0
                    #4 the aesthetic
                    print("quitting.")
                    time.sleep(.5)
                    print("quitting..")
                    time.sleep(.5)
                    print('quitting...')
                    sys.exit()

def dow30stocks():
        dowstocksCurrentTotalinput = 0.0
        dowDollarsTotal = 0
        dollarsgainedorlost = 'null'
        dowtotalcont = 0
        cont = 1
        file = open("dow30stocks.txt", "r")
        lines = file.readlines()
        dowStock1Ticker = lines[8]
        dowStock1PricePerShareWhenBought = int(lines[9])
        dowStock1SharesBought = int(lines[10])
        dowStock1TotalPriceWhenBought = int(lines[11])
        dowStock2Ticker = lines[13]
        dowStock2PricePerShareWhenBought = int(lines[14])
        dowStock2SharesBought = int(lines[15])
        dowStock2TotalPriceWhenBought = int(lines[16])
        dowStock3Ticker = lines[18]
        dowStock3PricePerShareWhenBought = float(lines[19])
        dowStock3SharesBought = int(lines[20])
        dowStock3TotalPriceWhenBought = float(lines[21])
        dowStock4Ticker = lines[23]
        dowStock4PricePerShareWhenBought = float(lines[24])
        dowStock4SharesBought = int(lines[25])
        dowStock4TotalPriceWhenBought = float(lines[26])
        dowStock5Ticker = lines[28]
        dowStock5PricePerShareWhenBought = float(lines[29])
        dowStock5SharesBought = int(lines[30])
        dowStock5TotalPriceWhenBought = float(lines[31])
        dowStock6Ticker = lines[33]
        dowStock6PricePerShareWhenBought = float(lines[34])
        dowStock6SharesBought = int(lines[35])
        dowStock6TotalPriceWhenBought = int(lines[36])
        dowStocksTotalWhenBought = float(lines[39])
        #DIVIDENDSBELOW
        dowStock1Dividend = float(lines[43])
        dowStock2Dividend = float(lines[46])
        dowStock3Dividend = float(lines[49])
        dowStock4Dividend = int(lines[52])
        dowStock5Dividend = float(lines[55])
        dowStock6Dividend = float(lines[58])

        print('____________________________ ')
        print('|What would you like to do?:|')
        print('|1.View my dow 30 stocks----|')
        print('|2.Go back to the main menu-|')
        print('|3.Quit---------------------|')
        print('|___________________________|')
        menuchoice = int(input())
        if menuchoice == 2:
            choicemenu()
        if menuchoice == 3:
            #4 the aesthetic
            print("quitting.")
            time.sleep(.5)
            print("quitting..")
            time.sleep(.5)
            print('quitting...')
            sys.exit()
        while cont == 1:
            if menuchoice == 1:
                print('______________________________________')
                print('|How would you like to veiw them?------|')
                print('|1.View my dow 30 stocks---------------|')
                print('|2.View my dow 30 stocks current totals|')
                print('|3.Veiw my total money gained/lost-----|')
                print('|4.Go back to the main menu------------|')
                print('|5.Quit--------------------------------|')
                print('|______________________________________|')
            dowmenuchoice = int(input())
            if dowmenuchoice == 1:
                #times are set back a day because of when the stock markets open/close bc it cant get live data
                start = dt.datetime.now() - timedelta(days=1)
                end = dt.datetime.now() - timedelta(days=1)
                dowstock1 = web.DataReader(dowStock1Ticker, "google", start, end)
                dowstock2 = web.DataReader(dowStock2Ticker, "google", start, end)
                dowstock3 = web.DataReader(dowStock3Ticker, "google", start, end)
                dowstock4 = web.DataReader(dowStock4Ticker, "google", start, end)
                dowstock5 = web.DataReader(dowStock5Ticker, "google", start, end)
                dowstock6 = web.DataReader(dowStock6Ticker, "google", start, end)
                print("\nNOTE: due to limitaions of the google fininace API,\nstock times have to be delayed by one day.\n")
                input("Press the Enter key to proceed...")
                print("----------------------------------------------------")
                print(dowStock1Ticker)
                print(dowstock1)
                print("\n")
                print("----------------------------------------------------")

                print(dowStock2Ticker)
                print(dowstock2)
                print("\n")
                print("----------------------------------------------------")

                print(dowStock3Ticker)
                print(dowstock3)
                print("\n")
                print("----------------------------------------------------")

                print(dowStock4Ticker)
                print(dowstock4)
                print("\n")
                print("----------------------------------------------------")

                print(dowStock5Ticker)
                print(dowstock5)
                print("\n")
                print("----------------------------------------------------")

                print(dowStock6Ticker)
                print(dowstock6)
                print("\n")
                print("----------------------------------------------------")

                print('____________________________ ')
                print('|What would you like to do?:|')
                print('|1.Go back to the main menu-|')
                print('|2.Quit---------------------|')
                print('|___________________________|')
                choice1menuchoice = int(input())
                if choice1menuchoice == 1:
                    cont = 0
                    choicemenu()

                if choice1menuchoice == 2:
                    cont = 0
                    #4 the aesthetic
                    print("quitting.")
                    time.sleep(.5)
                    print("quitting..")
                    time.sleep(.5)
                    print('quitting...')
                    sys.exit()

            if dowmenuchoice == 2:
                start = dt.datetime.now() - timedelta(days=1)
                end = dt.datetime.now() - timedelta(days=1)
                totaldowstock1 = web.DataReader(dowStock1Ticker, "google", start, end)
                totaldowstock2 = web.DataReader(dowStock2Ticker, "google", start, end)
                totaldowstock3 = web.DataReader(dowStock3Ticker, "google", start, end)
                totaldowstock4 = web.DataReader(dowStock4Ticker, "google", start, end)
                totaldowstock5 = web.DataReader(dowStock5Ticker, "google", start, end)
                totaldowstock6 = web.DataReader(dowStock6Ticker, "google", start, end)
                currentDowStock1PortfoiloValue = totaldowstock1 * dowStock1SharesBought
                currentDowStock2PortfoiloValue = totaldowstock2 * dowStock2SharesBought
                currentDowStock3PortfoiloValue = totaldowstock3 * dowStock3SharesBought
                currentDowStock4PortfoiloValue = totaldowstock4 * dowStock4SharesBought
                currentDowStock5PortfoiloValue = totaldowstock5 * dowStock5SharesBought
                currentDowStock6PortfoiloValue = totaldowstock6 * dowStock6SharesBought
                print("\nNOTE: due to limitaions of the google fininace API,\nstock times have to be delayed by one day.\nTo see the total amount that all your shares are worth,\nlook under the column titled \"close\".\n")
                input("Press the Enter key to proceed...")
                print("----------------------------------------------------")
                print("your total value of:" + dowStock1Ticker)
                print(currentDowStock1PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")

                print("your total value of:" + dowStock2Ticker)
                print(currentDowStock2PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")

                print("your total value of:" + dowStock3Ticker)
                print(currentDowStock3PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")

                print("your total value of:" + dowStock4Ticker)
                print(currentDowStock4PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")

                print("your total value of:" + dowStock5Ticker)
                print(currentDowStock5PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")

                print("your total value of:" + dowStock6Ticker)
                print(currentDowStock6PortfoiloValue)
                print("\n")
                print("----------------------------------------------------")
            if dowmenuchoice == 3:

                start = dt.datetime.now() - timedelta(days=1)
                end = dt.datetime.now() - timedelta(days=1)
                totaldowstock1 = web.DataReader(dowStock1Ticker, "google", start, end)
                totaldowstock2 = web.DataReader(dowStock2Ticker, "google", start, end)
                totaldowstock3 = web.DataReader(dowStock3Ticker, "google", start, end)
                totaldowstock4 = web.DataReader(dowStock4Ticker, "google", start, end)
                totaldowstock5 = web.DataReader(dowStock5Ticker, "google", start, end)
                totaldowstock6 = web.DataReader(dowStock6Ticker, "google", start, end)
                currentDowStock1PortfoiloValue = totaldowstock1 * dowStock1SharesBought
                currentDowStock2PortfoiloValue = totaldowstock2 * dowStock2SharesBought
                currentDowStock3PortfoiloValue = totaldowstock3 * dowStock3SharesBought
                currentDowStock4PortfoiloValue = totaldowstock4 * dowStock4SharesBought
                currentDowStock5PortfoiloValue = totaldowstock5 * dowStock5SharesBought
                currentDowStock6PortfoiloValue = totaldowstock6 * dowStock6SharesBought
                dowstocksCurrentTotal = currentDowStock1PortfoiloValue + currentDowStock2PortfoiloValue + currentDowStock3PortfoiloValue + currentDowStock4PortfoiloValue + currentDowStock5PortfoiloValue + currentDowStock6PortfoiloValue
                totaldowstock1DIVIDENDS = dowStock1Dividend * dowStock1SharesBought
                totaldowstock2DIVIDENDS = dowStock2Dividend * dowStock2SharesBought
                totaldowstock3DIVIDENDS = dowStock3Dividend * dowStock3SharesBought
                totaldowstock4DIVIDENDS = dowStock4Dividend * dowStock4SharesBought
                totaldowstock5DIVIDENDS = dowStock5Dividend * dowStock5SharesBought
                totaldowstock6DIVIDENDS = dowStock6Dividend * dowStock6SharesBought
                dowDividendsSum = totaldowstock1DIVIDENDS + totaldowstock2DIVIDENDS + totaldowstock3DIVIDENDS + totaldowstock4DIVIDENDS + totaldowstock5DIVIDENDS + totaldowstock6DIVIDENDS




                print("\nNOTE: due to limitaions of the google fininace API, stock times have to be delayed by one day.\nThe following result is the total money gained/lost after yesterdays closing.\nTo see the total amount that all your shares are worth, look under the column titled \"close\".\n")
                input("Press the Enter key to proceed...\n")
                print(f"The sum of your dividends is:",dowDividendsSum)
                print(f"You had a starting total value of:",dowStocksTotalWhenBought)
                print(f'-------------------------------------------------------------',"\nthe current total value of your Dow stocks is:\n",dowstocksCurrentTotal,'\n------------------------------------------------------------')
                while dowtotalcont == 0:
                    try:
                        dowstocksCurrentTotalinput = float(input("please enter the current total of your Dow stocks:"))
                        if dowstocksCurrentTotalinput > dowStocksTotalWhenBought:
                            dowDollarsTotal =  dowstocksCurrentTotalinput - dowStocksTotalWhenBought
                            dollarsgainedorlost = "Congratulations! you gained:"
                        if dowstocksCurrentTotalinput < dowStocksTotalWhenBought:
                            dowDollarsTotal =  dowStocksTotalWhenBought - dowstocksCurrentTotalinput
                            dollarsgainedorlost = "Dont panic! you lost:"
                        #dollarsgainedorlostpercent = dollarsgainedorlost / dowStocksTotalWhenBought * 100
                        print(f"",dollarsgainedorlost,dowDollarsTotal,'since your initial investment.')
                        #print(f"",dollarsgainedorlost,dowDollarsgainedorlostpercent,'%\ since your initial investment')
                        dowtotalcont = 1
                        break
                    except(ValueError):
                        print("that is not a valid input!")











            if dowmenuchoice == 4:
                cont = 0
                choicemenu()

            if dowmenuchoice == 5:
                cont = 0
                #4 the aesthetic
                print("quitting.")
                time.sleep(.5)
                print("quitting..")
                time.sleep(.5)
                print('quitting...')
                sys.exit()

def nondow30stocks():
    nondowstocksCurrentTotalinput = 0.0
    nondowtotalcont = 0

    nowdowDollarsTotal = 0
    dollarsgainedorlost = 'null'
    nonDowPositivtyResult = 'null'
    cont = 1
    file = open("nondow30stocks.txt", "r")
    lines = file.readlines()
    nondowStock1Ticker = lines[8]
    nondowStock1PricePerShareWhenBought = float(lines[9])
    nondowStock1SharesBought = int(lines[10])
    nondowStock1TotalPriceWhenBought = float(lines[11])
    nondowStock2Ticker = lines[13]
    nondowStock2PricePerShareWhenBought = int(lines[14])
    nondowStock2SharesBought = int(lines[15])
    nondowStock2TotalPriceWhenBought = int(lines[16])
    nondowStock3Ticker = lines[18]
    nondowStock3PricePerShareWhenBought = float(lines[19])
    nondowStock3SharesBought = int(lines[20])
    nondowStock3TotalPriceWhenBought = float(lines[21])
    nondowStock4Ticker = lines[23]
    nondowStock4PricePerShareWhenBought = float(lines[24])
    nondowStock4SharesBought = int(lines[25])
    nondowStock4TotalPriceWhenBought = float(lines[26])
    nondowStock5Ticker = lines[28]
    nondowStock5PricePerShareWhenBought = float(lines[29])
    nondowStock5SharesBought = int(lines[30])
    nondowStock5TotalPriceWhenBought = float(lines[31])
    nondowStock6Ticker = lines[33]
    nondowStock6PricePerShareWhenBought = float(lines[34])
    nondowStock6SharesBought = int(lines[35])
    nondowStock6TotalPriceWhenBought = float(lines[36])
    nondowStocksTotalWhenBought = float(lines[39])
    #DIVIDENDSBELOW
    nondowStock1Dividend = float(lines[43])
    nondowStock2Dividend = float(lines[46])
    nondowStock3Dividend = float(lines[49])
    nondowStock4Dividend = float(lines[52])
    nondowStock5Dividend = float(lines[55])
    nondowStock6Dividend = float(lines[58])

    print('____________________________ ')
    print('|What would you like to do?:|')
    print('|1.View my non dow stocks---|')
    print('|2.Go back to the main menu-|')
    print('|3.Quit---------------------|')
    print('|___________________________|')
    menuchoice = int(input())
    if menuchoice == 2:
        choicemenu()
    if menuchoice == 3:
        #4 the aesthetic
        print("quitting.")
        time.sleep(.5)
        print("quitting..")
        time.sleep(.5)
        print('quitting...')
        sys.exit()
    while cont == 1:
        if menuchoice == 1:
            print('________________________________________')
            print('|How would you like to veiw them?-------|')
            print('|1.View my non dow stocks---------------|')
            print('|2.View my non dow stocks current totals|')
            print('|3.Veiw my total money gained/lost------|')
            print('|4.Go back to the main menu-------------|')
            print('|5.Quit---------------------------------|')
            print('|_______________________________________|')
        nondowmenuchoice = int(input())
        if nondowmenuchoice == 1:
            #times are set back a day because of when the stock markets open/close bc it cant get live data
            start = dt.datetime.now() - timedelta(days=1)
            end = dt.datetime.now() - timedelta(days=1)
            nondowstock1 = web.DataReader(nondowStock1Ticker, "google", start, end)
            nondowstock2 = web.DataReader(nondowStock2Ticker, "google", start, end)
            nondowstock3 = web.DataReader(nondowStock3Ticker, "google", start, end)
            nondowstock4 = web.DataReader(nondowStock4Ticker, "google", start, end)
            nondowstock5 = web.DataReader(nondowStock5Ticker, "google", start, end)
            nondowstock6 = web.DataReader(nondowStock6Ticker, "google", start, end)
            print("\nNOTE: due to limitaions of the google fininace API,\nstock times have to be delayed by one day.\n")
            input("Press the Enter key to proceed...")
            print("----------------------------------------------------")
            print(nondowStock1Ticker)
            print(nondowstock1)
            print("\n")
            print("----------------------------------------------------")

            print(nondowStock2Ticker)
            print(nondowstock2)
            print("\n")
            print("----------------------------------------------------")

            print(nondowStock3Ticker)
            print(nondowstock3)
            print("\n")
            print("----------------------------------------------------")

            print(nondowStock4Ticker)
            print(nondowstock4)
            print("\n")
            print("----------------------------------------------------")

            print(nondowStock5Ticker)
            print(nondowstock5)
            print("\n")
            print("----------------------------------------------------")

            print(nondowStock6Ticker)
            print(nondowstock6)
            print("\n")
            print("----------------------------------------------------")

            print('____________________________ ')
            print('|What would you like to do?:|')
            print('|1.Go back to the main menu-|')
            print('|2.Quit---------------------|')
            print('|___________________________|')
            choice1menuchoice = int(input())
            if choice1menuchoice == 1:
                cont = 0
                choicemenu()

            if choice1menuchoice == 2:
                cont = 0
                #4 the aesthetic
                print("quitting.")
                time.sleep(.5)
                print("quitting..")
                time.sleep(.5)
                print('quitting...')
                sys.exit()

        if nondowmenuchoice == 2:
            start = dt.datetime.now() - timedelta(days=1)
            end = dt.datetime.now() - timedelta(days=1)
            totalnondowstock1 = web.DataReader(nondowStock1Ticker, "google", start, end)
            totalnondowstock2 = web.DataReader(nondowStock2Ticker, "google", start, end)
            totalnondowstock3 = web.DataReader(nondowStock3Ticker, "google", start, end)
            totalnondowstock4 = web.DataReader(nondowStock4Ticker, "google", start, end)
            totalnondowstock5 = web.DataReader(nondowStock5Ticker, "google", start, end)
            totalnondowstock6 = web.DataReader(nondowStock6Ticker, "google", start, end)
            currentnonDowStock1PortfoiloValue = totalnondowstock1 * nondowStock1SharesBought
            currentnonDowStock2PortfoiloValue = totalnondowstock2 * nondowStock2SharesBought
            currentnonDowStock3PortfoiloValue = totalnondowstock3 * nondowStock3SharesBought
            currentnonDowStock4PortfoiloValue = totalnondowstock4 * nondowStock4SharesBought
            currentnonDowStock5PortfoiloValue = totalnondowstock5 * nondowStock5SharesBought
            currentnonDowStock6PortfoiloValue = totalnondowstock6 * nondowStock6SharesBought
            print("\nNOTE: due to limitaions of the google fininace API,\nstock times have to be delayed by one day.\nTo see the total amount that all your shares are worth,\nlook under the column titled \"close\".\n")
            input("Press the Enter key to proceed...")
            print("----------------------------------------------------")
            print("your total value of:" + nondowStock1Ticker)
            print(currentnonDowStock1PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")

            print("your total value of:" + nondowStock2Ticker)
            print(currentnonDowStock2PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")

            print("your total value of:" + nondowStock3Ticker)
            print(currentnonDowStock3PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")

            print("your total value of:" + nondowStock4Ticker)
            print(currentnonDowStock4PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")

            print("your total value of:" + nondowStock5Ticker)
            print(currentnonDowStock5PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")

            print("your total value of:" + nondowStock6Ticker)
            print(currentnonDowStock6PortfoiloValue)
            print("\n")
            print("----------------------------------------------------")
        if nondowmenuchoice == 3:
            start = dt.datetime.now() - timedelta(days=1)
            end = dt.datetime.now() - timedelta(days=1)
            totalnondowstock1 = web.DataReader(nondowStock1Ticker, "google", start, end)
            totalnondowstock2 = web.DataReader(nondowStock2Ticker, "google", start, end)
            totalnondowstock3 = web.DataReader(nondowStock3Ticker, "google", start, end)
            totalnondowstock4 = web.DataReader(nondowStock4Ticker, "google", start, end)
            totalnondowstock5 = web.DataReader(nondowStock5Ticker, "google", start, end)
            totalnondowstock6 = web.DataReader(nondowStock6Ticker, "google", start, end)
            currentnonDowStock1PortfoiloValue = totalnondowstock1 * nondowStock1SharesBought
            currentnonDowStock2PortfoiloValue = totalnondowstock2 * nondowStock2SharesBought
            currentnonDowStock3PortfoiloValue = totalnondowstock3 * nondowStock3SharesBought
            currentnonDowStock4PortfoiloValue = totalnondowstock4 * nondowStock4SharesBought
            currentnonDowStock5PortfoiloValue = totalnondowstock5 * nondowStock5SharesBought
            currentnonDowStock6PortfoiloValue = totalnondowstock6 * nondowStock6SharesBought
            nondowstocksCurrentTotal = currentnonDowStock1PortfoiloValue + currentnonDowStock2PortfoiloValue + currentnonDowStock3PortfoiloValue + currentnonDowStock4PortfoiloValue + currentnonDowStock5PortfoiloValue + currentnonDowStock6PortfoiloValue
            totalnondowstock1DIVIDENDS = nondowStock1Dividend * nondowStock1SharesBought
            totalnondowstock2DIVIDENDS = nondowStock2Dividend * nondowStock2SharesBought
            totalnondowstock3DIVIDENDS = nondowStock3Dividend * nondowStock3SharesBought
            totalnondowstock4DIVIDENDS = nondowStock4Dividend * nondowStock4SharesBought
            totalnondowstock5DIVIDENDS = nondowStock5Dividend * nondowStock5SharesBought
            totalnondowstock6DIVIDENDS = nondowStock6Dividend * nondowStock6SharesBought
            nondowDividendsSum = totalnondowstock1DIVIDENDS + totalnondowstock2DIVIDENDS + totalnondowstock3DIVIDENDS + totalnondowstock4DIVIDENDS + totalnondowstock5DIVIDENDS + totalnondowstock6DIVIDENDS




            print("\nNOTE: due to limitaions of the google fininace API, stock times have to be delayed by one day.\nThe following result is the total money gained/lost after yesterdays closing.\nTo see the total amount that all your shares are worth, look under the column titled \"close\".\n")
            input("Press the Enter key to proceed...\n")
            print(f"The sum of your dividends is:",nondowDividendsSum)
            print(f"You had a starting total value of:",nondowStocksTotalWhenBought)
            print(f'-------------------------------------------------------------',"\nthe current total value of your Dow stocks is:\n",nondowstocksCurrentTotal,'\n------------------------------------------------------------')
            while nondowtotalcont == 0:
                try:
                    nondowstocksCurrentTotalinput = float(input("please enter the current total of your Dow stocks:"))
                    if nondowstocksCurrentTotalinput > nondowStocksTotalWhenBought:
                        nondowDollarsTotal =  nondowstocksCurrentTotalinput - nondowStocksTotalWhenBought
                        dollarsgainedorlost = "Congratulations! you gained:"
                    if nondowstocksCurrentTotalinput < nondowStocksTotalWhenBought:
                        nondowDollarsTotal =  nondowStocksTotalWhenBought - nondowstocksCurrentTotalinput
                        dollarsgainedorlost = "Dont panic! you lost:"
                    print(f"",dollarsgainedorlost,nondowDollarsTotal,'since your initial investment.')

                    nondowtotalcont = 1
                    break
                except(ValueError):
                    print("that is not a valid input!")










        if nondowmenuchoice == 4:
            cont = 0
            choicemenu()

        if nondowmenuchoice == 5:
            cont = 0
            #4 the aesthetic
            print("quitting.")
            time.sleep(.5)
            print("quitting..")
            time.sleep(.5)
            print('quitting...')
            sys.exit()
def mystocks():
    cont = 1
    ndfile = open("nondow30stocks.txt", "r")
    ndlines = ndfile.readlines()
    nondowStock1Ticker = ndlines[8]
    nondowStock2Ticker = ndlines[13]
    nondowStock3Ticker = ndlines[18]
    nondowStock4Ticker = ndlines[23]
    nondowStock5Ticker = ndlines[28]
    nondowStock6Ticker = ndlines[33]
    dfile = open("dow30stocks.txt", "r")
    dlines = dfile.readlines()
    dowStock1Ticker = dlines[8]
    dowStock2Ticker = dlines[13]
    dowStock3Ticker = dlines[18]
    dowStock4Ticker = dlines[23]
    dowStock5Ticker = dlines[28]
    dowStock6Ticker = dlines[33]
    start = dt.datetime.now() - timedelta(days=1)
    end = dt.datetime.now() - timedelta(days=1)
    dowstock1 = web.DataReader(dowStock1Ticker, "google", start, end)
    dowstock2 = web.DataReader(dowStock2Ticker, "google", start, end)
    dowstock3 = web.DataReader(dowStock3Ticker, "google", start, end)
    dowstock4 = web.DataReader(dowStock4Ticker, "google", start, end)
    dowstock5 = web.DataReader(dowStock5Ticker, "google", start, end)
    dowstock6 = web.DataReader(dowStock6Ticker, "google", start, end)
    nondowstock1 = web.DataReader(nondowStock1Ticker, "google", start, end)
    nondowstock2 = web.DataReader(nondowStock2Ticker, "google", start, end)
    nondowstock3 = web.DataReader(nondowStock3Ticker, "google", start, end)
    nondowstock4 = web.DataReader(nondowStock4Ticker, "google", start, end)
    nondowstock5 = web.DataReader(nondowStock5Ticker, "google", start, end)
    nondowstock6 = web.DataReader(nondowStock6Ticker, "google", start, end)
    print("\nNOTE: due to limitaions of the google fininace API,\nstock times have to be delayed by one day.\n")
    input("Press the Enter key to proceed and veiw all of your stocks...")
    print("--------------------[DOW Stocks]--------------------")
    print("----------------------------------------------------")
    print(dowStock1Ticker)
    print(dowstock1)
    print("\n")
    print("----------------------------------------------------")

    print(dowStock2Ticker)
    print(dowstock2)
    print("\n")
    print("----------------------------------------------------")

    print(dowStock3Ticker)
    print(dowstock3)
    print("\n")
    print("----------------------------------------------------")

    print(dowStock4Ticker)
    print(dowstock4)
    print("\n")
    print("----------------------------------------------------")

    print(dowStock5Ticker)
    print(dowstock5)
    print("\n")
    print("----------------------------------------------------")

    print(dowStock6Ticker)
    print(dowstock6)
    print("\n")
    print("----------------------------------------------------")
    print("\n")
    print("------------------[NON-DOW Stocks]------------------")
    print("----------------------------------------------------")
    print(nondowStock1Ticker)
    print(nondowstock1)
    print("\n")
    print("----------------------------------------------------")

    print(nondowStock2Ticker)
    print(nondowstock2)
    print("\n")
    print("----------------------------------------------------")

    print(nondowStock3Ticker)
    print(nondowstock3)
    print("\n")
    print("----------------------------------------------------")

    print(nondowStock4Ticker)
    print(nondowstock4)
    print("\n")
    print("----------------------------------------------------")

    print(nondowStock5Ticker)
    print(nondowstock5)
    print("\n")
    print("----------------------------------------------------")

    print(nondowStock6Ticker)
    print(nondowstock6)
    print("\n")
    print("----------------------------------------------------")

    print('____________________________ ')
    print('|What would you like to do?:|')
    print('|1.Go back to the main menu-|')
    print('|2.Quit---------------------|')
    print('|___________________________|')
    while cont == 1:
        try:
            choice = int(input())


            if choice == 1:
                cont = 0
                choicemenu()
                break
            if choice == 2:
                cont = 0
                #4 the aesthetic
                print("quitting.")
                time.sleep(.5)
                print("quitting..")
                time.sleep(.5)
                print('quitting...')

                sys.exit()
        except(ValueError):
            print("please enter a valid number.")

choicemenu()

print (" ")
print (" ")
print (" _  _  ____    __    ____  ___    ___  ____  _  _  ___  ____     ")
print ("( \\/ )( ___)  /__\\  (  _ \\/ __)  / __)(_  _)( \\( )/ __)( ___)    ")
print (" \\  /  )__)  /(__)\\  )   /\\__ \\  \\__ \\ _)(_  )  (( (__  )__)   ")  
print (" (__) (____)(__)(__)(_)\\_)(___/  (___/(____)(_)\\_)\\___)(____)   ") 
print ("  ___    __    __    ___  __  __  __      __   ____  _____  ____ ")
print (" / __)  /__\\  (  )  / __)(  )(  )(  )    /__\\ (_  _)(  _  )(  _ \\")
print ("( (__  /(__)\\  )(__( (__  )(__)(  )(__  /(__)\\  )(   )(_)(  )   /")
print (" \\___)(__)(__)(____)\\___)(______)(____)(__)(__)(__) (_____)(_)\\_)")
print (" ")
print (" ")
enterToEnter = input("Press [ENTER] key to start! ")
calcIDSes = int(26)
if calcIDSes == 26:
    if calcIDSes == 26:
        if calcIDSes == 26:
            if calcIDSes == 26:
                    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print ("Years since")
                    print ("\nSelect a mode: ")
                    print ("\n[Year only] - ID: 1 ")
                    print ("\n[Year + month] - ID: 2 ")
                    print ("\n[Year + month + day] - ID: 3")
                    print ("\n[Year + month + day + hour] - ID: 4")
                    print ("\n[Year + month + day + hour + minute] - ID: 5")
                    print ("\n[Year + month + day + hour + minute + second] - ID: 6")
                    entID = str(input("Enter an ID to begin: "))
                    if (entID == "1" or entID == "0"):
                        print ("Year only mode")
                        startYear = int(input("Enter a starting year: "))
                        endYear = int(input("Enter a destination year: "))
                        if (startYear < endYear):
                            distantYear = int(endYear - startYear)
                        if (startYear > endYear):
                            distantYear = int(startYear - endYear)
                        print ("Difference in years: " + str(distantYear))
                    if (entID == "2"):
                        print ("Year and month mode")
                        startMonth = int(input("Enter a starting month number (1-12): "))
                        if (startMonth > 12):
                            print ("Error! The number you entered is too high! Reverting to 12... ")
                            startMonth == 12
                        if (startMonth < 1):
                            print ("Error! The number you entered is too low! Reverting to 1... ")
                            startMonth == 12
                        endMonth = int(input("Enter an ending month number (1-12): "))
                        startYear = int(input("Enter a starting year: "))
                        endYear = int(input("Enter a destination year: "))
                        if (startMonth < endMonth):
                            distantMonth = int(endMonth - startMonth)
                        if (startMonth > endMonth):
                            distantMonth = int(startMonth - endMonth)
                        if (startMonth == endMonth):
                            distantMonth = int(0)
                        if (startYear < endYear):
                            distantYear = int(endYear - startYear)
                        if (startYear > endYear):
                            distantYear = int(startYear - endYear)
                        if (startYear == endYear):
                            distantYear = int(0)
                        if (startMonth == 1):
                            startMonthStr = str("January")
                        if (startMonth == 2):
                            startMonthStr = str("February")
                        if (startMonth == 3):
                            startMonthStr = str("March")	
                        if (startMonth == 4):
                            startMonthStr = str("April")
                        if (startMonth == 5):
                            startMonthStr = str("May")
                        if (startMonth == 6):
                            startMonthStr = str("June")	
                        if (startMonth == 7):
                            startMonthStr = str("July")
                        if (startMonth == 8):
                            startMonthStr = str("August")
                        if (startMonth == 9):
                            startMonthStr = str("September")	
                        if (startMonth == 10):
                            startMonthStr = str("October")
                        if (startMonth == 11):
                            startMonthStr = str("November")
                        if (startMonth == 12):
                            startMonthStr = str("December")	
                        if (endMonth == 1):
                            endMonth2Str = str("January")
                        if (endMonth == 2):
                            endMonth2Str = str("February")
                        if (endMonth == 3):
                            endMonth2Str = str("March")	
                        if (endMonth == 4):
                            endMonth2Str = str("April")
                        if (endMonth == 5):
                            endMonth2Str = str("May")
                        if (endMonth == 6):
                            endMonth2Str = str("June")	
                        if (endMonth == 7):
                            endMonth2Str = str("July")
                        if (endMonth == 8):
                            endMonth2Str = str("August")
                        if (endMonth == 9):
                            endMonth2Str = str("September")	
                        if (endMonth == 10):
                            endMonth2Str = str("October")
                        if (endMonth == 11):
                            endMonth2Str = str("November")
                        if (endMonth == 12):
                            endMonth2Str = str("December")	
                        #if (endMonth > startMonth):
                        #	distantYear = int
                        #	distantYear = distantYear - 1
                        #if (endMonth < startMonth):
                        #	distantYear = int
                        #	distantYear = distantYear + 0
                        print ("Start date: " + str(startMonthStr) + ", " + str(startYear))
                        print ("End date: " + str(endMonth2Str) + ", " + str(endYear))
                        if (distantYear == 1 and not distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " year, " + str(distantMonth) + " months") 
                        if (distantYear == 1 and distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " year, " + str(distantMonth) + " month") 
                        if not (distantYear == 1 and not distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " years, " + str(distantMonth) + " months") 
                        if not (distantYear == 1 and distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " years, " + str(distantMonth) + " month")
                        print ("This also equals: ")
                        monthCount1 = int
                        monthCount2 = int(distantYear * 12)
                        monthCount3 = int(distantMonth)
                        monthCount1 = (monthCount2 + monthCount3)
                        print ("Months: " + str(monthCount1))
                    if (entID == "3"):
                        print ("Year, month, and day mode")
                        startMonth = int(input("Enter a starting month number (1-12): "))
                        if (startMonth > 12):
                            print ("Error! The number you entered is too high! Reverting to 12... ")
                            startMonth == 12
                        if (startMonth < 1):
                            print ("Error! The number you entered is too low! Reverting to 1... ")
                            startMonth == 12
                        endMonth = int(input("Enter an ending month number (1-12): "))
                        startYear = int(input("Enter a starting year: "))
                        endYear = int(input("Enter a destination year: "))
                        startDay = int(input("Enter a starting day: "))
                        endDay = int(input("Enter a destination day: "))
                        if (startMonth < endMonth):
                            distantMonth = int(endMonth - startMonth)
                        if (startMonth > endMonth):
                            distantMonth = int(startMonth - endMonth)
                        if (startMonth == endMonth):
                            distantMonth = int(0)
                        if (startYear < endYear):
                            distantYear = int(endYear - startYear)
                        if (startYear > endYear):
                            distantYear = int(startYear - endYear)
                        if (startYear == endYear):
                            distantYear = int(0)
                        if (startMonth == 1):
                            startMonthStr = str("January")
                        if (startMonth == 2):
                            startMonthStr = str("February")
                        if (startMonth == 3):
                            startMonthStr = str("March")	
                        if (startMonth == 4):
                            startMonthStr = str("April")
                        if (startMonth == 5):
                            startMonthStr = str("May")
                        if (startMonth == 6):
                            startMonthStr = str("June")	
                        if (startMonth == 7):
                            startMonthStr = str("July")
                        if (startMonth == 8):
                            startMonthStr = str("August")
                        if (startMonth == 9):
                            startMonthStr = str("September")	
                        if (startMonth == 10):
                            startMonthStr = str("October")
                        if (startMonth == 11):
                            startMonthStr = str("November")
                        if (startMonth == 12):
                            startMonthStr = str("December")	
                        if (endMonth == 1):
                            endMonth2Str = str("January")
                        if (endMonth == 2):
                            endMonth2Str = str("February")
                        if (endMonth == 3):
                            endMonth2Str = str("March")	
                        if (endMonth == 4):
                            endMonth2Str = str("April")
                        if (endMonth == 5):
                            endMonth2Str = str("May")
                        if (endMonth == 6):
                            endMonth2Str = str("June")	
                        if (endMonth == 7):
                            endMonth2Str = str("July")
                        if (endMonth == 8):
                            endMonth2Str = str("August")
                        if (endMonth == 9):
                            endMonth2Str = str("September")	
                        if (endMonth == 10):
                            endMonth2Str = str("October")
                        if (endMonth == 11):
                            endMonth2Str = str("November")
                        if (endMonth == 12):
                            endMonth2Str = str("December")
                        if (startDay < 32 and startMonth == 1): # January
                            destinationDay == int(0)
                            destinationDay == startDay
                        if (startDay < 30 and startMonth == 2): # February
                            destinationDay == int(0)
                            destinationDay == startDay + 31
                        if (startDay < 32 and startMonth == 3): # March
                            destinationDay == int(0)
                            destinationDay == startDay + 60
                        if (startDay < 31 and startMonth == 4): # April
                            destinationDay == int(0)
                            destinationDay == startDay + 91
                        if (startDay < 32 and startMonth == 5): # May
                            destinationDay == int(0) 
                            destinationDay == startDay + 122
                        if (startDay < 31 and startMonth == 6): # June
                            destinationDay == int(0)
                            destinationDay == startDay + 153
                        if (startDay < 32 and startMonth == 7): # July
                            destinationDay == int(0)
                            destinationDay == startDay + 183
                        if (startDay < 32 and startMonth == 8): # August 
                            destinationDay == int(0)
                            destinationDay == startDay + 214
                        if (startDay < 31 and startMonth == 9): # September 
                            destinationDay == int(0)
                            destinationDay == startDay + 245 
                        if (startDay < 32 and startMonth == 10): # October 
                            destinationDay == int(0)
                            destinationDay == startDay + 275
                        if (startDay < 31 and startMonth == 11): # November
                            destinationDay == int(0)
                            destinationDay == startDay + 306
                        if (startDay < 32 and startMonth == 12): # December 
                            destinationDay == int(0)
                            destinationDay == startDay + 336
                        if (startDay < 1):
                            startDay == 1
                        if (endDay < 32 and startMonth == 1): # January
                            destinationDay == int(0)
                            destinationDay == endDay
                        if (endDay < 30 and startMonth == 2): # February
                            destinationDay == int(0)
                            destinationDay == endDay + 31
                        if (endDay < 32 and startMonth == 3): # March
                            destinationDay == int(0)
                            destinationDay == endDay + 60
                        if (endDay < 31 and startMonth == 4): # April
                            destinationDay == int(0)
                            destinationDay == endDay + 91
                        if (endDay < 32 and startMonth == 5): # May
                            destinationDay == int(0)
                            destinationDay == endDay + 122
                        if (endDay < 31 and startMonth == 6): # June
                            destinationDay == int(0)
                            destinationDay == endDay + 153
                        if (endDay < 32 and startMonth == 7): # July
                            destinationDay == int(0)
                            destinationDay == endDay + 183
                        if (endDay < 32 and startMonth == 8): # August 
                            destinationDay == int(0)
                            destinationDay == endDay + 214
                        if (endDay < 31 and startMonth == 9): # September
                            destinationDay == int(0)
                            destinationDay == endDay + 245 
                        if (endDay < 32 and startMonth == 10): # October 
                            destinationDay == int(0)
                            destinationDay == endDay + 275
                        if (endDay < 31 and startMonth == 11): # November
                            destinationDay == int(0)
                            destinationDay == endDay + 306
                        if (endDay < 32 and startMonth == 12): # December 
                            destinationDay == int(0)
                            destinationDay == endDay + 336
                        if (endDay < 1):
                            endDay == 1
                        # This phrase has helped me out A LOT:
                        # Thirty days has September, April, June, and November
                        #if (endMonth > startMonth):
                        #	distantYear = int
                        #	distantYear = distantYear - 1
                        #if (endMonth < startMonth):
                        #	distantYear = int
                        #	distantYear = distantYear + 0
                        distantDay = int(destinationDay)
                        print ("Start year: " + str(startMonthStr) + ", " + str(startYear))
                        print ("End year: " + str(endMonth2Str) + ", " + str(endYear))
                        if (distantYear == 1 and not distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " year, " + str(distantMonth) + " months, " + str(distantDay) + " days") 
                        if (distantYear == 1 and distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " year, " + str(distantMonth) + " month, " + str(distantDay) + " days") 
                        if not (distantYear == 1 and not distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " years, " + str(distantMonth) + " months, " + str(distantDay) + " days") 
                        if not (distantYear == 1 and distantMonth == 1):
                            print ("\nDifference: " + str(distantYear) + " years, " + str(distantMonth) + " month, " + str(distantDay) + " days")
                        print ("This also equals: ")
                        monthCount1 = int
                        monthCount2 = int(distantYear * 12)
                        monthCount3 = int(distantMonth)
                        monthCount1 = (monthCount2 + monthCount3)
                        print ("Months: " + str(monthCount1))
noMore = input("\n\nAn unexpected error has occurred\nPress [ENTER] key to continue")
'''

Development Difficulty

Year only mode: Easiest
Year and month mode: easy
Year, month, and day mode: difficult
Year, month, day, and hour mode: not yet attempted 
Year, month, day, hour, and minute mode: not yet attempted 
Year, month, day, hour, minute, and second mode: not yet attempted

'''
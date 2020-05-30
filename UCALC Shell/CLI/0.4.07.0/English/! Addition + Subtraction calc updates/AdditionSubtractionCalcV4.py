# start of script
'''
Documentation
This is a new and improved version of the basic Addition calculator
English Calculator
=====
There are 2 modes:
with decimals
without decimals
to get to the "with decimals" mode, just type 0
to get to the "without decimals" mode, just type 1
=====
The with decimals mode does calculations containing decimals. 
The without decimals mode does calculations with no decimals
pretty easy
There are 2 basic easter eggs enabled:
To activate them, try to add 1 and 1 or 2 and 2 in either mode
There is 1 special easter egg enabled:
to activate it, add numbers together in either mode and reach the number 42
'''
# comment divider
'''
Function list
helpGuide()
easterEggA1()
easterEggA2()
easterEggB1()
easterEggB2()
restartShell()
findTheMeaningA()
findTheMeaningB()
findTheMeaningC()
findTheMeaningD()
'''
# comment divider
def helpGuide(): # Help guide function
	print ("Documentation")
	print ("This is a new and improved version of the basic Addition calculator")
	print ("English Calculator")
	print ("=====")
	print ("There are 2 modes:")
	print ("with decimals")
	print ("without decimals")
	print ("to get to the 'with decimals' mode, just type 0")
	print ("to get to the 'without decimals' mode, just type 1")
	print ("=====")
	print ("The with decimals mode does calculations containing decimals.")
	print ("The without decimals mode does calculations with no decimals")
	print ("pretty easy")
	print ("There are 2 basic easter eggs enabled:")
	print ("To activate them, try to add 1 and 1 or 2 and 2 in either mode")
	print ("There is 1 special easter egg enabled:")
	print ("to activate it, add numbers together in either mode and reach the number 42")
print ("Addition and subtraction calculator")
curTotal = int(0)
print (" ")
print ("Select a mode: ")
print ("=============================================")
print ("[Addition] With decimals [0]")
print ("[Addition] Without decimals [1]")
print ("[Subtraction] with decimals [2]")
print ("[Subtraction] without decimals [3]")
print ("Help [4]")
print ("Quit [5]")
print ("=============================================")
print ("Alternatively, you can add a - before a number\nin the addition calculator for subtraction")
print ("=============================================")
def restartShell():
	print ("Addition and subtraction calculator")
	print (" ")
	curTotal = int(0)
	print ("Select a mode: ")
	print ("=============================================")
	print ("With decimals [0]")
	print ("Without decimals [1]")
	print ("[Subtraction] with decimals [2]")
	print ("[Subtraction] without decimals [3]")
	print ("Help [4] (this option is disabled)")
	print ("Quit [5]")
	print ("=============================================")
	print ("Alternatively, you can add a - before a number\nin the addition calculator for subtraction")
	print ("=============================================")
	modeType = str(input("Mode ID: "))
	if (modeType == "0"):
		print ("Error: cannot load")
		print ("There was a recursion error")
		noMore = input("Press [ENTER] key to return")
		print (restartShell())
	if (modeType == "1"):
		print ("Error: cannot load")
		print ("There was a recursion error")
		noMore = input("Press [ENTER] key to return")
	if (modeType == "2"):
		print ("Error: cannot load")
		print ("There was a recursion error")
		noMore = input("Press [ENTER] key to return")
	if (modeType == "3"):
		print ("Error: cannot load")
		print ("There was a recursion error")
		noMore = input("Press [ENTER] key to return")
		print (restartShell())
	if (modeType == "4"):
		print ("Error: cannot load")
		print ("You have already viewed the help guide in your current session")
		noMore = input("Press [ENTER] key to quit")
		print (restartShell())
	if (modeType == "5"):
		print ("Preparing to close")
		quitIt = str(input("Press [ENTER] key to confirm"))
		print (crash())
	if not (modeType == "0" or modeType == "1" or modeType == "2" or modeType == "3" or modeType == "4" or modeType == "5"):
		print ("Error: Invalid ID entered")
		noMore = input("Press [ENTER] key to return")
		print (restartShell())
	modeType = str(input("Mode ID: "))
# addition mode 
modeType = str(input("Mode ID: "))
if (modeType == "0"):
	fNum1 = float(input("Add number: "))
	print (str(fNum1))
	fNum2 = float(input("Add number: "))
	fCurTotal = float(fNum1 + fNum2)
	print (str(fCurTotal))
	equationLength = int(999999999)
	def easterEggA1():
		if (fNum1 == 1.0):
			if (fNum2 == 1.0):
				print ("You can't be serious")
				print ("1 + 1 is 2")
	def easterEggA2():
		if (fNum1 == 2.0):
			if (fNum2 == 2.0):
				print ("You can't be serious")
				print ("2 + 2 is 4")
	def findTheMeaningA():
		if (fCurTotal == 42.0):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(fCurTotal))
	if (fNum1 == 1.0):
		if (fNum2 == 1.0):
			print (easterEggA1())
	if (fNum1 == 2.0):
		if (fNum2 == 2.0):
			print (easterEggA2())
	if (fCurTotal == 42.0):
		print (findTheMeaningA())
	fCurTotal2 = float(fCurTotal)
	def findTheMeaningB():
		if (fCurTotal2 == 42.0):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(fCurTotal2))
	while (equationLength == equationLength):
		fNewNum = float(input("Add number: "))
		fCurTotal2 = fCurTotal2 + fNewNum
		if (fCurTotal2 == 42.0):
			print (findTheMeaningB())
		print (str(fCurTotal2))
if (modeType == "1"):
	num1 = int(input("Add number: "))
	print (str(num1))
	num2 = int(input("Add number: "))
	curTotal = int(num1 + num2)	
	print (str(curTotal))
	equationLength = int(999999999)
	def easterEggB1():
		if (num1 == 1):
			if (num2 == 1):
				print ("You can't be serious")
				print ("1 + 1 is 2")
	def easterEggB2():
		if (num1 == 2):
			if (num2 == 2):
				print ("You can't be serious")
				print ("2 + 2 is 4")
	def findTheMeaningC():
		if (curTotal == 42):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(curTotal))
	if (num1 == 1):
		if (num2 == 1):
			print (easterEggB1())
	if (num1 == 2):
		if (num2 == 2):
			print (easterEggB2())
	if (curTotal == 42):
		print (findTheMeaningC())
	curTotal2 = int(curTotal)
	def findTheMeaningD():
		if (curTotal2 == 42):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(curTotal2))
	while (equationLength == equationLength):
		newNum = int(input("Add number: "))
		curTotal2 = curTotal2 + newNum
		if (curTotal2 == 42):
			print (findTheMeaningD())
		print (str(curTotal2))
# subtraction mode
if (modeType == "2"):
	fNum1 = float(input("Subtract number: "))
	print (str(fNum1))
	fNum2 = float(input("Subtract number: "))
	fCurTotal = float(fNum1 - fNum2)
	print (str(fCurTotal))
	equationLength = int(999999999)
	def findTheMeaningA():
		if (fCurTotal == 42.0):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(fCurTotal))
	if (fCurTotal == 42.0):
		print (findTheMeaningA())
	fCurTotal2 = float(fCurTotal)
	def findTheMeaningB():
		if (fCurTotal2 == 42.0):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(fCurTotal2))
	while (equationLength == equationLength):
		fNewNum = float(input("Add number: "))
		fCurTotal2 = fCurTotal2 - fNewNum
		if (fCurTotal2 == 42.0):
			print (findTheMeaningB())
		print (str(fCurTotal2))
if (modeType == "3"):
	num1 = int(input("Subtract number: "))
	print (str(num1))
	num2 = int(input("Subtract number: "))
	curTotal = int(num1 - num2)	
	print (str(curTotal))
	equationLength = int(999999999)
	def findTheMeaningC():
		if (curTotal == 42):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(curTotal))
	if (curTotal == 42):
		print (findTheMeaningC())
	curTotal2 = int(curTotal)
	def findTheMeaningD():
		if (curTotal2 == 42):
			print ("Answer to the Ultimate Question of Life, The Universe, and Everything is " + str(curTotal2))
	while (equationLength == equationLength):
		newNum = int(input("Add number: "))
		curTotal2 = curTotal2 - newNum
		if (curTotal2 == 42):
			print (findTheMeaningD())
		print (str(curTotal2))
if (modeType == "4"):
	print (helpGuide())
	noMore = input("Press [ENTER] key to return")
	print (restartShell())
if (modeType == "5"):
	print ("Preparing to close")
	quitIt = str(input("Press [ENTER] key to confirm"))
	print (crash())
if not (modeType == "0" or modeType == "1" or modeType == "2" or modeType == "3" or modeType == "4" or modeType == "5"):
	print ("Error: Invalid ID entered")
	noMore = input("Press [ENTER] key to return")
	print (restartShell())
# end of script
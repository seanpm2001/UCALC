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
There are 2 easter eggs enabled:
To activate them, try to add 1 and 1 or 2 and 2 in either mode
'''
def helpGuide():
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
	print ("There are 2 easter eggs enabled:")
	print ("To activate them, try to add 1 and 1 or 2 and 2 in either mode")
print ("Addition calculator")
curTotal = int(0)
print ("Select a mode: ")
print ("With decimals [0]")
print ("Without decimals [1]")
print ("Help [2]")
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
	if (fNum1 == 1.0):
		if (fNum2 == 1.0):
			print (easterEggA1())
	if (fNum1 == 2.0):
		if (fNum2 == 2.0):
			print (easterEggA2())
	fCurTotal2 = float(fCurTotal)
	while (equationLength == equationLength):
		fNewNum = float(input("Add number: "))
		fCurTotal2 = fCurTotal2 + fNewNum
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
	if (num1 == 1):
		if (num2 == 1):
			print (easterEggB1())
	if (num1 == 2):
		if (num2 == 2):
			print (easterEggB2())
	curTotal2 = int(curTotal)
	while (equationLength == equationLength):
		newNum = int(input("Add number: "))
		curTotal2 = curTotal2 + newNum
		print (str(curTotal2))
if (modeType == "2"):
	print (helpGuide())
	noMore = input("Press [ENTER] key to exit")
	# print (restart())
if not (modeType == "0" or modeType == "1" or modeType == "2"):
	noMore = input("Press [ENTER] key to quit")
# end of script
# obsolete notes below
'''
This is a new and improved version of the basic Addition calculator
'''

'''
def easterEgg1():
	if (curTotal == 2):
		print ("You can't be serious")	
'''
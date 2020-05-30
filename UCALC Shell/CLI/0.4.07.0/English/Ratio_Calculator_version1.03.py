# start of script |||||||#
# start pf program      |#
print ("[][]       [][]")#
print ("[][]  (*)  [][]")#
print ("[][]       [][]")#
print ("[][]  (*)  [][]")#
print ("[][]       [][]")#
print ("Ratio calculator")
enterToEnter = input("Press [ENTER] key to start")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n===============================")
print ("Data type")
print ("Number without decimals [1]")
print ("Number with decimals [2]")
print ("===============================")
numDID = str(input("Enter an ID: "))
if (numDID == "1"): # int edition
	print ("===============================")
	print ("Mode")
	print ("2 Objects [A]")
	print ("2 Numbers [B]")
	print ("===============================")
	modeID = str(input("Enter a letter to start: "))
	if (modeID == "a" or modeID == "A"):
		print ("===============================")
		print ("Object mode")
		print ("===============================")
		obj1Name = str(input("Enter the name of object1: "))
		obj1Value = int(input("Enter a value for " + str(obj1Name) + " "))
		obj2Name = str(input("Enter the name of object2: "))
		obj2Value = int(input("Enter a value for " + str(obj1Name) + " "))
		ratio1 = int(obj1Value / obj2Value)
		ratioA = int(obj1Value)
		ratioB = int(obj2Value)
		print ("===============================")
		print ("The ratio of " + str(obj1Name) + " to " + str(obj2Name) + " is " + str(obj1Value) + ":" + str(obj2Value))
		print ("===============================")
		noMore = input("Press [ENTER] key to quit")
	if (modeID == "b" or modeID == "B"):
		print ("===============================")
		print ("Multi-number mode")
		val1 = int(input("Enter a number: "))
		val2 = int(input("Enter a second number: "))
		print ("The ratio is " + str(val1) + ":" + str(val2))
if (numDID == "2"): # float edition
	print ("===============================")
	print ("Mode")
	print ("2 Objects [A]")
	print ("2 Numbers [B]")
	print ("===============================")
	modeID = str(input("Enter a letter to start: "))
	if (modeID == "a" or modeID == "A"):
		print ("===============================")
		print ("Object mode")
		obj1Name = str(input("Enter the name of object1: "))
		obj1Value = float(input("Enter a value for " + str(obj1Name) + " "))
		obj2Name = str(input("Enter the name of object2: "))
		obj2Value = float(input("Enter a value for " + str(obj1Name) + " "))
		ratio1 = float(obj1Value / obj2Value)
		ratioA = float(obj1Value)
		ratioB = float(obj2Value)
		print ("===============================")
		print ("The ratio of " + str(obj1Name) + " to " + str(obj2Name) + " is " + str(obj1Value) + ":" + str(obj2Value))
		print ("===============================")
		noMore = input("Press [ENTER] key to quit")
	if (modeID == "b" or modeID == "B"):
		print ("===============================")
		print ("Multi-number mode")
		val1 = float(input("Enter a number: "))
		val2 = float(input("Enter a second number: "))
		print ("The ratio is " + str(val1) + ":" + str(val2))
print ("===============================")
crash1 = input("You did not enter a valid ID. The program will now exit.\nPress [ENTER] key to quit")
print ("Goodbye")
# end of program
# | * | #
'''
Program info
| requirements 
Build 4 Version 1.03
System requirements: 16 Megabytes of RAM 
Space requirements: 16 Kilobytes
| Feature info
Feature designed for UCALC 
Originally made on February 25th 2019 @ 8:25 am
Ratio testing 
# inspired by K H A N - A C A D E M Y . O R G 
| Description
A ratio making software that is distributed through UCALC. Originally designed as a test
'''
# end of script
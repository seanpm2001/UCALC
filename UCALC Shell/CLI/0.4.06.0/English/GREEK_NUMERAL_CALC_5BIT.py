import random
print ("Greek numeral calculator")
print ("Note: this program is locked in 5 bit mode")
print ("Maximum value is 32")
enterToEnter = input("Press [ENTER] key to start")
print ("Select a calculation mode: ")
print ("\nAddition              | ID: 1 |")
print ("Subtraction           | ID: 2 |")
print ("Multiplication        | ID: 3 |")
print ("Division              | ID: 4 |")
print ("Modular division      | ID: 5 |")
print ("Direct translate      | ID: 6 |")
print ("Random                | ID: 7 |")
calcModeID = str(input("Enter an ID to continue >> "))
if (calcModeID == "1"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to add (NO DECIMALS): "))
	curanswer = int(firstNum + secondNum)
	if (curanswer < 33):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 5 bit registry")
if (calcModeID == "2"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to subtract (NO DECIMALS): "))
	curanswer = int(firstNum - secondNum)
	if (curanswer < 33):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 5 bit registry")
if (calcModeID == "3"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to multiply (NO DECIMALS): "))
	curanswer = int(firstNum * secondNum)
	if (curanswer < 33):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 5 bit registry")
if (calcModeID == "4"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to divide by (NO DECIMALS): "))
	curanswer = int(firstNum / secondNum)
	if (curanswer < 33):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 5 bit registry")
if (calcModeID == "5"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to mod by (NO DECIMALS): "))
	curanswer = int(firstNum % secondNum)
	if (curanswer < 33):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 5 bit registry")
if (calcModeID == "6"):
	directNum = int(input("Enter a number to translate (NO DECIMALS)"))
if (calcModeID == "7"):
	curanswer = int()
	ranGreek = int(random.randint(1, 32))
	print ("Random number: " + str(ranGreek))
	if (ranGreek == 1):
		greekNumeral = str("I")
	if (ranGreek == 2):
		greekNumeral = str("II")
	if (ranGreek == 3):
		greekNumeral = str("III")
	if (ranGreek == 4):
		greekNumeral = str("IIII")
	if (ranGreek == 5):
		greekNumeral = str("┌")
	if (ranGreek == 6):
		greekNumeral = str("┌I")
	if (ranGreek == 7):
		greekNumeral = str("┌II")
	if (ranGreek == 8):
		greekNumeral = str("┌III")
	if (ranGreek == 9):
		greekNumeral = str("┌IIII")
	if (ranGreek == 10):
		greekNumeral = str("∆")
	if (ranGreek == 11):
		greekNumeral = str("∆I")
	if (ranGreek == 12):
		greekNumeral = str("∆II")
	if (ranGreek == 13):
		greekNumeral = str("∆III")
	if (ranGreek == 14):
		greekNumeral = str("∆IIII")
	if (ranGreek == 15):
		greekNumeral = str("∆┌")
	if (ranGreek == 16):
		greekNumeral = str("∆┌I")
	if (ranGreek == 17):
		greekNumeral = str("∆┌II")
	if (ranGreek == 18):
		greekNumeral = str("∆┌III")
	if (ranGreek == 19):
		greekNumeral = str("∆┌IIII")
	if (ranGreek == 20):
		greekNumeral = str("∆∆")
	if (ranGreek == 21):
		greekNumeral = str("∆∆I")
	if (ranGreek == 22):
		greekNumeral = str("∆∆II")
	if (ranGreek == 23):
		greekNumeral = str("∆∆III")
	if (ranGreek == 24):
		greekNumeral = str("∆∆IIII")
	if (ranGreek == 25):
		greekNumeral = str("∆∆┌")
	if (ranGreek == 26):
		greekNumeral = str("∆∆┌I")
	if (ranGreek == 27):
		greekNumeral = str("∆∆┌II")
	if (ranGreek == 28):
		greekNumeral = str("∆∆┌III")
	if (ranGreek == 29):
		greekNumeral = str("∆∆┌IIII")
	if (ranGreek == 30):
		greekNumeral = str("∆∆∆")
	if (ranGreek == 31):
		greekNumeral = str("∆∆∆I")
	if (ranGreek == 32):
		greekNumeral = str("∆∆∆II")
	print ("Translation: " + str(greekNumeral))
if (curanswer < 33):
	if (curanswer == 1):
		greekNumeral = str("I")
	if (curanswer == 2):
		greekNumeral = str("II")
	if (curanswer == 3):
		greekNumeral = str("III")
	if (curanswer == 4):
		greekNumeral = str("IIII")
	if (curanswer == 5):
		greekNumeral = str("┌")
	if (curanswer == 6):
		greekNumeral = str("┌I")
	if (curanswer == 7):
		greekNumeral = str("┌II")
	if (curanswer == 8):
		greekNumeral = str("┌III")
	if (curanswer == 9):
		greekNumeral = str("┌IIII")
	if (curanswer == 10):
		greekNumeral = str("∆")
	if (curanswer == 11):
		greekNumeral = str("∆I")
	if (curanswer == 12):
		greekNumeral = str("∆II")
	if (curanswer == 13):
		greekNumeral = str("∆III")
	if (curanswer == 14):
		greekNumeral = str("∆IIII")
	if (curanswer == 15):
		greekNumeral = str("∆┌")
	if (curanswer == 16):
		greekNumeral = str("∆┌I")
	if (curanswer == 17):
		greekNumeral = str("∆┌II")
	if (curanswer == 18):
		greekNumeral = str("∆┌III")
	if (curanswer == 19):
		greekNumeral = str("∆┌IIII")
	if (curanswer == 20):
		greekNumeral = str("∆∆")
	if (curanswer == 21):
		greekNumeral = str("∆∆I")
	if (curanswer == 22):
		greekNumeral = str("∆∆II")
	if (curanswer == 23):
		greekNumeral = str("∆∆III")
	if (curanswer == 24):
		greekNumeral = str("∆∆IIII")
	if (curanswer == 25):
		greekNumeral = str("∆∆┌")
	if (curanswer == 26):
		greekNumeral = str("∆∆┌I")
	if (curanswer == 27):
		greekNumeral = str("∆∆┌II")
	if (curanswer == 28):
		greekNumeral = str("∆∆┌III")
	if (curanswer == 29):
		greekNumeral = str("∆∆┌IIII")
	if (curanswer == 30):
		greekNumeral = str("∆∆∆")
	if (curanswer == 31):
		greekNumeral = str("∆∆∆I")
	if (curanswer == 32):
		greekNumeral = str("∆∆∆II")
	print ("| Translation in greek numerals: " + str(greekNumeral))
noMore = input("Press [ENTER] key to quit")
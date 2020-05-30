import random
print ("Greek numeral calculator")
print ("Note: this program is locked in 8 bit mode")
print ("Maximum value is 256")
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
	if (curanswer < 257):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 8 bit registry")
if (calcModeID == "2"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to subtract (NO DECIMALS): "))
	curanswer = int(firstNum - secondNum)
	if (curanswer < 257):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 8 bit registry")
if (calcModeID == "3"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to multiply (NO DECIMALS): "))
	curanswer = int(firstNum * secondNum)
	if (curanswer < 257):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 8 bit registry")
if (calcModeID == "4"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to divide by (NO DECIMALS): "))
	curanswer = int(firstNum / secondNum)
	if (curanswer < 257):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 8 bit registry")
if (calcModeID == "5"):
	firstNum = int(input("Enter a starting number (NO DECIMALS): "))
	secondNum = int(input("Enter a number to mod by (NO DECIMALS): "))
	curanswer = int(firstNum % secondNum)
	if (curanswer < 257):
		print ("The answer is " + str(curanswer))
	else:
		print ("Overflow error! Number exceeds the 8 bit registry")
if (calcModeID == "6"):
	directNum = int(input("Enter a number to translate (NO DECIMALS)"))
if (calcModeID == "7"):
	curanswer = int()
	ranGreek = int(random.randint(1, 256))
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
	if (ranGreek == 33):
		greekNumeral = str("∆∆∆III")
	if (ranGreek == 34):
		greekNumeral = str("∆∆∆IIII")
	if (ranGreek == 35):
		greekNumeral = str("∆∆∆┌")
	if (ranGreek == 36):
		greekNumeral = str("∆∆∆┌I")
	if (ranGreek == 37):
		greekNumeral = str("∆∆∆┌II")
	if (ranGreek == 38):
		greekNumeral = str("∆∆∆┌III")
	if (ranGreek == 39):
		greekNumeral = str("∆∆∆┌IIII")
	if (ranGreek == 40):
		greekNumeral = str("∆∆∆∆")
	if (ranGreek == 41):
		greekNumeral = str("∆∆∆∆I")
	if (ranGreek == 42):
		greekNumeral = str("∆∆∆∆II")
	if (ranGreek == 43):
		greekNumeral = str("∆∆∆∆III")
	if (ranGreek == 44):
		greekNumeral = str("∆∆∆∆IIII")
	if (ranGreek == 45):
		greekNumeral = str("∆∆∆∆┌")
	if (ranGreek == 46):
		greekNumeral = str("∆∆∆∆┌I")
	if (ranGreek == 47):
		greekNumeral = str("∆∆∆∆┌II")
	if (ranGreek == 48):
		greekNumeral = str("∆∆∆∆┌III")
	if (ranGreek == 49):
		greekNumeral = str("∆∆∆∆┌IIII")
	if (ranGreek == 50):
		greekNumeral = str("∆∆∆∆∆")
	if (ranGreek == 51):
		greekNumeral = str("∆∆∆∆∆I")
	if (ranGreek == 52):
		greekNumeral = str("∆∆∆∆∆II")
	if (ranGreek == 53):
		greekNumeral = str("∆∆∆∆∆III")
	if (ranGreek == 54):
		greekNumeral = str("∆∆∆∆∆IIII")
	if (ranGreek == 55):
		greekNumeral = str("∆∆∆∆∆┌")
	if (ranGreek == 56):
		greekNumeral = str("∆∆∆∆∆┌I")
	if (ranGreek == 57):
		greekNumeral = str("∆∆∆∆∆┌II")
	if (ranGreek == 58):
		greekNumeral = str("∆∆∆∆∆┌III")
	if (ranGreek == 59):
		greekNumeral = str("∆∆∆∆∆┌IIII")
	if (ranGreek == 60):
		greekNumeral = str("∆∆∆∆∆∆")
	if (ranGreek == 61):
		greekNumeral = str("∆∆∆∆∆∆I")
	if (ranGreek == 62):
		greekNumeral = str("∆∆∆∆∆∆II")
	if (ranGreek == 63):
		greekNumeral = str("∆∆∆∆∆∆III")
	if (ranGreek == 64):
		greekNumeral = str("∆∆∆∆∆∆IIII")
	if (ranGreek == 65):
		greekNumeral = str("∆∆∆∆∆∆┌")
	if (ranGreek == 66):
		greekNumeral = str("∆∆∆∆∆∆┌I")
	if (ranGreek == 67):
		greekNumeral = str("∆∆∆∆∆∆┌II")
	if (ranGreek == 68):
		greekNumeral = str("∆∆∆∆∆∆┌III")
	if (ranGreek == 69):
		greekNumeral = str("∆∆∆∆∆∆┌IIII")
	if (ranGreek == 70):
		greekNumeral = str("∆∆∆∆∆∆∆")
	if (ranGreek == 71):
		greekNumeral = str("∆∆∆∆∆∆∆I")
	if (ranGreek == 72):
		greekNumeral = str("∆∆∆∆∆∆∆II")
	if (ranGreek == 73):
		greekNumeral = str("∆∆∆∆∆∆∆III")
	if (ranGreek == 74):
		greekNumeral = str("∆∆∆∆∆∆∆IIII")
	if (ranGreek == 75):
		greekNumeral = str("∆∆∆∆∆∆∆┌")
	if (ranGreek == 76):
		greekNumeral = str("∆∆∆∆∆∆∆┌I")
	if (ranGreek == 77):
		greekNumeral = str("∆∆∆∆∆∆∆┌II")
	if (ranGreek == 78):
		greekNumeral = str("∆∆∆∆∆∆∆┌III")
	if (ranGreek == 79):
		greekNumeral = str("∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 80):
		greekNumeral = str("∆∆∆∆∆∆∆∆")
	if (ranGreek == 81):
		greekNumeral = str("∆∆∆∆∆∆∆∆I")
	if (ranGreek == 82):
		greekNumeral = str("∆∆∆∆∆∆∆∆II")
	if (ranGreek == 83):
		greekNumeral = str("∆∆∆∆∆∆∆∆III")
	if (ranGreek == 84):
		greekNumeral = str("∆∆∆∆∆∆∆∆IIII")
	if (ranGreek == 85):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌")
	if (ranGreek == 86):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌I")
	if (ranGreek == 87):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌II")
	if (ranGreek == 88):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌III")
	if (ranGreek == 89):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 90):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆")
	if (ranGreek == 91):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆I")
	if (ranGreek == 92):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆II")
	if (ranGreek == 93):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆III")
	if (ranGreek == 94):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆IIII")
	if (ranGreek == 95):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌")
	if (ranGreek == 96):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌I")
	if (ranGreek == 97):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌II")
	if (ranGreek == 98):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌III")
	if (ranGreek == 99):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 100):
		greekNumeral = str("H")
	if (ranGreek == 101):
		greekNumeral = str("HI")
	if (ranGreek == 102):
		greekNumeral = str("HII")
	if (ranGreek == 103):
		greekNumeral = str("HIII")
	if (ranGreek == 104):
		greekNumeral = str("HIIII")
	if (ranGreek == 105):
		greekNumeral = str("H┌")
	if (ranGreek == 106):
		greekNumeral = str("H┌I")
	if (ranGreek == 107):
		greekNumeral = str("H┌II")
	if (ranGreek == 108):
		greekNumeral = str("H┌III")
	if (ranGreek == 109):
		greekNumeral = str("H┌IIII")
	if (ranGreek == 110):
		greekNumeral = str("H∆")
	if (ranGreek == 111):
		greekNumeral = str("H∆I")
	if (ranGreek == 112):
		greekNumeral = str("H∆II")
	if (ranGreek == 113):
		greekNumeral = str("H∆III")
	if (ranGreek == 114):
		greekNumeral = str("H∆IIII")
	if (ranGreek == 115):
		greekNumeral = str("H∆┌")
	if (ranGreek == 116):
		greekNumeral = str("H∆┌I")
	if (ranGreek == 117):
		greekNumeral = str("H∆┌II")
	if (ranGreek == 118):
		greekNumeral = str("H∆┌III")
	if (ranGreek == 119):
		greekNumeral = str("H∆┌IIII")
	if (ranGreek == 120):
		greekNumeral = str("H∆∆")
	if (ranGreek == 121):
		greekNumeral = str("H∆∆I")	
	if (ranGreek == 122):
		greekNumeral = str("H∆∆II")	
	if (ranGreek == 123):
		greekNumeral = str("H∆∆III")
	if (ranGreek == 124):
		greekNumeral = str("H∆∆IIII")	
	if (ranGreek == 125):
		greekNumeral = str("H∆∆┌")
	if (ranGreek == 126):
		greekNumeral = str("H∆∆┌I")	
	if (ranGreek == 127):
		greekNumeral = str("H∆∆┌II")
	if (ranGreek == 128):
		greekNumeral = str("H∆∆┌III")
	if (ranGreek == 129):
		greekNumeral = str("H∆∆┌IIII")	
	if (ranGreek == 130):
		greekNumeral = str("H∆∆∆")		
	if (ranGreek == 131):
		greekNumeral = str("H∆∆∆I")
	if (ranGreek == 132):
		greekNumeral = str("H∆∆∆II")
	if (ranGreek == 133):
		greekNumeral = str("H∆∆∆III")
	if (ranGreek == 134):
		greekNumeral = str("H∆∆∆IIII")
	if (ranGreek == 135):
		greekNumeral = str("H∆∆∆┌")
	if (ranGreek == 136):
		greekNumeral = str("H∆∆∆┌I")
	if (ranGreek == 137):
		greekNumeral = str("H∆∆∆┌II")
	if (ranGreek == 138):
		greekNumeral = str("H∆∆∆┌III")
	if (ranGreek == 139):
		greekNumeral = str("H∆∆∆┌IIII")
	if (ranGreek == 140):
		greekNumeral = str("H∆∆∆∆")	
	if (ranGreek == 141):
		greekNumeral = str("H∆∆∆∆I")
	if (ranGreek == 142):
		greekNumeral = str("H∆∆∆∆II")
	if (ranGreek == 143):
		greekNumeral = str("H∆∆∆∆III")
	if (ranGreek == 144):
		greekNumeral = str("H∆∆∆∆IIII")
	if (ranGreek == 145):
		greekNumeral = str("H∆∆∆∆┌")
	if (ranGreek == 146):
		greekNumeral = str("H∆∆∆∆┌I")
	if (ranGreek == 147):
		greekNumeral = str("H∆∆∆∆┌II")
	if (ranGreek == 148):
		greekNumeral = str("H∆∆∆∆┌III")
	if (ranGreek == 149):
		greekNumeral = str("H∆∆∆∆┌IIII")
	if (ranGreek == 150):
		greekNumeral = str("H∆∆∆∆∆")	
	if (ranGreek == 151):
		greekNumeral = str("H∆∆∆∆∆I")
	if (ranGreek == 152):
		greekNumeral = str("H∆∆∆∆∆II")	
	if (ranGreek == 153):
		greekNumeral = str("H∆∆∆∆∆III")
	if (ranGreek == 154):
		greekNumeral = str("H∆∆∆∆∆IIII")
	if (ranGreek == 155):
		greekNumeral = str("H∆∆∆∆∆┌")		
	if (ranGreek == 156):
		greekNumeral = str("H∆∆∆∆∆┌I")		
	if (ranGreek == 157):
		greekNumeral = str("H∆∆∆∆∆┌II")	
	if (ranGreek == 158):
		greekNumeral = str("H∆∆∆∆∆┌III")
	if (ranGreek == 159):
		greekNumeral = str("H∆∆∆∆∆┌IIII")
	if (ranGreek == 160):
		greekNumeral = str("H∆∆∆∆∆∆")
	if (ranGreek == 161):
		greekNumeral = str("H∆∆∆∆∆∆I")
	if (ranGreek == 162):
		greekNumeral = str("H∆∆∆∆∆∆II")
	if (ranGreek == 163):
		greekNumeral = str("H∆∆∆∆∆∆III")
	if (ranGreek == 164):
		greekNumeral = str("H∆∆∆∆∆∆IIII")
	if (ranGreek == 165):
		greekNumeral = str("H∆∆∆∆∆∆┌")
	if (ranGreek == 166):
		greekNumeral = str("H∆∆∆∆∆∆┌I")
	if (ranGreek == 167):
		greekNumeral = str("H∆∆∆∆∆∆┌II")
	if (ranGreek == 168):
		greekNumeral = str("H∆∆∆∆∆∆┌III")
	if (ranGreek == 169):
		greekNumeral = str("H∆∆∆∆∆∆┌IIII")
	if (ranGreek == 170):
		greekNumeral = str("H∆∆∆∆∆∆∆")		
	if (ranGreek == 171):
		greekNumeral = str("H∆∆∆∆∆∆∆I")
	if (ranGreek == 172):
		greekNumeral = str("H∆∆∆∆∆∆∆II")
	if (ranGreek == 173):
		greekNumeral = str("H∆∆∆∆∆∆∆III")
	if (ranGreek == 174):
		greekNumeral = str("H∆∆∆∆∆∆∆IIII")
	if (ranGreek == 175):
		greekNumeral = str("H∆∆∆∆∆∆∆┌")
	if (ranGreek == 176):
		greekNumeral = str("H∆∆∆∆∆∆∆┌I")
	if (ranGreek == 177):
		greekNumeral = str("H∆∆∆∆∆∆∆┌II")
	if (ranGreek == 178):
		greekNumeral = str("H∆∆∆∆∆∆∆┌III")
	if (ranGreek == 179):
		greekNumeral = str("H∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 180):
		greekNumeral = str("H∆∆∆∆∆∆∆∆")
	if (ranGreek == 181):
		greekNumeral = str("H∆∆∆∆∆∆∆∆I")
	if (ranGreek == 182):
		greekNumeral = str("H∆∆∆∆∆∆∆∆II")
	if (ranGreek == 183):
		greekNumeral = str("H∆∆∆∆∆∆∆∆III")
	if (ranGreek == 184):
		greekNumeral = str("H∆∆∆∆∆∆∆∆IIII")
	if (ranGreek == 185):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌")
	if (ranGreek == 186):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌I")
	if (ranGreek == 187):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌II")
	if (ranGreek == 188):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌III")
	if (ranGreek == 189):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 190):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆")
	if (ranGreek == 191):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆I")
	if (ranGreek == 192):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆II")
	if (ranGreek == 193):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆III")
	if (ranGreek == 194):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆IIII")
	if (ranGreek == 195):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌")
	if (ranGreek == 196):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌I")
	if (ranGreek == 197):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌II")
	if (ranGreek == 198):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌III")
	if (ranGreek == 199):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌IIII")
	if (ranGreek == 200):
		greekNumeral = str("HH")
	if (ranGreek == 201):
		greekNumeral = str("HHI")
	if (ranGreek == 202):
		greekNumeral = str("HHII")
	if (ranGreek == 203):
		greekNumeral = str("HHIII")
	if (ranGreek == 204):
		greekNumeral = str("HHIIII")
	if (ranGreek == 205):
		greekNumeral = str("HH┌")
	if (ranGreek == 206):
		greekNumeral = str("HH┌I")
	if (ranGreek == 207):
		greekNumeral = str("HH┌II")
	if (ranGreek == 208):
		greekNumeral = str("HH┌III")
	if (ranGreek == 209):
		greekNumeral = str("HH┌IIII")
	if (ranGreek == 210):
		greekNumeral = str("HH∆")
	if (ranGreek == 211):
		greekNumeral = str("HH∆I")
	if (ranGreek == 212):
		greekNumeral = str("HH∆II")
	if (ranGreek == 213):
		greekNumeral = str("HH∆III")
	if (ranGreek == 214):
		greekNumeral = str("HH∆IIII")
	if (ranGreek == 215):
		greekNumeral = str("HH∆┌")
	if (ranGreek == 216):
		greekNumeral = str("HH∆┌I")
	if (ranGreek == 217):
		greekNumeral = str("HH∆┌II")
	if (ranGreek == 218):
		greekNumeral = str("HH∆┌III")
	if (ranGreek == 219):
		greekNumeral = str("HH∆┌IIII")
	if (ranGreek == 220):
		greekNumeral = str("HH∆∆")
	if (ranGreek == 221):
		greekNumeral = str("HH∆∆I")
	if (ranGreek == 222):
		greekNumeral = str("HH∆∆II")
	if (ranGreek == 223):
		greekNumeral = str("HH∆∆III")
	if (ranGreek == 224):
		greekNumeral = str("HH∆∆IIII")
	if (ranGreek == 225):
		greekNumeral = str("HH∆∆┌")
	if (ranGreek == 226):
		greekNumeral = str("HH∆∆┌I")
	if (ranGreek == 227):
		greekNumeral = str("HH∆∆┌II")
	if (ranGreek == 228):
		greekNumeral = str("HH∆∆┌III")
	if (ranGreek == 229):
		greekNumeral = str("HH∆∆┌IIII")
	if (ranGreek == 230):
		greekNumeral = str("HH∆∆∆")
	if (ranGreek == 231):
		greekNumeral = str("HH∆∆∆I")
	if (ranGreek == 232):
		greekNumeral = str("HH∆∆∆II")
	if (ranGreek == 233):
		greekNumeral = str("HH∆∆∆III")
	if (ranGreek == 234):
		greekNumeral = str("HH∆∆∆IIII")
	if (ranGreek == 235):
		greekNumeral = str("HH∆∆∆┌")
	if (ranGreek == 236):
		greekNumeral = str("HH∆∆∆┌I")
	if (ranGreek == 237):
		greekNumeral = str("HH∆∆∆┌II")
	if (ranGreek == 238):
		greekNumeral = str("HH∆∆∆┌III")
	if (ranGreek == 239):
		greekNumeral = str("HH∆∆∆┌IIII")
	if (ranGreek == 240):
		greekNumeral = str("HH∆∆∆∆")
	if (ranGreek == 241):
		greekNumeral = str("HH∆∆∆∆I")
	if (ranGreek == 242):
		greekNumeral = str("HH∆∆∆∆II")
	if (ranGreek == 243):
		greekNumeral = str("HH∆∆∆∆III")
	if (ranGreek == 244):
		greekNumeral = str("HH∆∆∆∆IIII")
	if (ranGreek == 245):
		greekNumeral = str("HH∆∆∆∆┌")
	if (ranGreek == 246):
		greekNumeral = str("HH∆∆∆∆┌I")
	if (ranGreek == 247):
		greekNumeral = str("HH∆∆∆∆┌II")
	if (ranGreek == 248):
		greekNumeral = str("HH∆∆∆∆┌III")
	if (ranGreek == 249):
		greekNumeral = str("HH∆∆∆∆┌IIII")
	if (ranGreek == 250):
		greekNumeral = str("HH∆∆∆∆∆")
	if (ranGreek == 251):
		greekNumeral = str("HH∆∆∆∆∆I")
	if (ranGreek == 252):
		greekNumeral = str("HH∆∆∆∆∆II")
	if (ranGreek == 253):
		greekNumeral = str("HH∆∆∆∆∆III")
	if (ranGreek == 254):
		greekNumeral = str("HH∆∆∆∆∆IIII")
	if (ranGreek == 255):
		greekNumeral = str("HH∆∆∆∆∆┌")
	if (ranGreek == 256):
		greekNumeral = str("HH∆∆∆∆∆┌I")
	print ("Translation: " + str(greekNumeral))
if (curanswer < 257):
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
	if (curanswer == 33):
		greekNumeral = str("∆∆∆III")
	if (curanswer == 34):
		greekNumeral = str("∆∆∆IIII")
	if (curanswer == 35):
		greekNumeral = str("∆∆∆┌")
	if (curanswer == 36):
		greekNumeral = str("∆∆∆┌I")
	if (curanswer == 37):
		greekNumeral = str("∆∆∆┌II")
	if (curanswer == 38):
		greekNumeral = str("∆∆∆┌III")
	if (curanswer == 39):
		greekNumeral = str("∆∆∆┌IIII")
	if (curanswer == 40):
		greekNumeral = str("∆∆∆∆")
	if (curanswer == 41):
		greekNumeral = str("∆∆∆∆I")
	if (curanswer == 42):
		greekNumeral = str("∆∆∆∆II")
	if (curanswer == 43):
		greekNumeral = str("∆∆∆∆III")
	if (curanswer == 44):
		greekNumeral = str("∆∆∆∆IIII")
	if (curanswer == 45):
		greekNumeral = str("∆∆∆∆┌")
	if (curanswer == 46):
		greekNumeral = str("∆∆∆∆┌I")
	if (curanswer == 47):
		greekNumeral = str("∆∆∆∆┌II")
	if (curanswer == 48):
		greekNumeral = str("∆∆∆∆┌III")
	if (curanswer == 49):
		greekNumeral = str("∆∆∆∆┌IIII")
	if (curanswer == 50):
		greekNumeral = str("∆∆∆∆∆")
	if (curanswer == 51):
		greekNumeral = str("∆∆∆∆∆I")
	if (curanswer == 52):
		greekNumeral = str("∆∆∆∆∆II")
	if (curanswer == 53):
		greekNumeral = str("∆∆∆∆∆III")
	if (curanswer == 54):
		greekNumeral = str("∆∆∆∆∆IIII")
	if (curanswer == 55):
		greekNumeral = str("∆∆∆∆∆┌")
	if (curanswer == 56):
		greekNumeral = str("∆∆∆∆∆┌I")
	if (curanswer == 57):
		greekNumeral = str("∆∆∆∆∆┌II")
	if (curanswer == 58):
		greekNumeral = str("∆∆∆∆∆┌III")
	if (curanswer == 59):
		greekNumeral = str("∆∆∆∆∆┌IIII")
	if (curanswer == 60):
		greekNumeral = str("∆∆∆∆∆∆")
	if (curanswer == 61):
		greekNumeral = str("∆∆∆∆∆∆I")
	if (curanswer == 62):
		greekNumeral = str("∆∆∆∆∆∆II")
	if (curanswer == 63):
		greekNumeral = str("∆∆∆∆∆∆III")
	if (curanswer == 64):
		greekNumeral = str("∆∆∆∆∆∆IIII")
	if (curanswer == 65):
		greekNumeral = str("∆∆∆∆∆∆┌")
	if (curanswer == 66):
		greekNumeral = str("∆∆∆∆∆∆┌I")
	if (curanswer == 67):
		greekNumeral = str("∆∆∆∆∆∆┌II")
	if (curanswer == 68):
		greekNumeral = str("∆∆∆∆∆∆┌III")
	if (curanswer == 69):
		greekNumeral = str("∆∆∆∆∆∆┌IIII")
	if (curanswer == 70):
		greekNumeral = str("∆∆∆∆∆∆∆")
	if (curanswer == 71):
		greekNumeral = str("∆∆∆∆∆∆∆I")
	if (curanswer == 72):
		greekNumeral = str("∆∆∆∆∆∆∆II")
	if (curanswer == 73):
		greekNumeral = str("∆∆∆∆∆∆∆III")
	if (curanswer == 74):
		greekNumeral = str("∆∆∆∆∆∆∆IIII")
	if (curanswer == 75):
		greekNumeral = str("∆∆∆∆∆∆∆┌")
	if (curanswer == 76):
		greekNumeral = str("∆∆∆∆∆∆∆┌I")
	if (curanswer == 77):
		greekNumeral = str("∆∆∆∆∆∆∆┌II")
	if (curanswer == 78):
		greekNumeral = str("∆∆∆∆∆∆∆┌III")
	if (curanswer == 79):
		greekNumeral = str("∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 80):
		greekNumeral = str("∆∆∆∆∆∆∆∆")
	if (curanswer == 81):
		greekNumeral = str("∆∆∆∆∆∆∆∆I")
	if (curanswer == 82):
		greekNumeral = str("∆∆∆∆∆∆∆∆II")
	if (curanswer == 83):
		greekNumeral = str("∆∆∆∆∆∆∆∆III")
	if (curanswer == 84):
		greekNumeral = str("∆∆∆∆∆∆∆∆IIII")
	if (curanswer == 85):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌")
	if (curanswer == 86):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌I")
	if (curanswer == 87):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌II")
	if (curanswer == 88):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌III")
	if (curanswer == 89):
		greekNumeral = str("∆∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 90):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆")
	if (curanswer == 91):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆I")
	if (curanswer == 92):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆II")
	if (curanswer == 93):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆III")
	if (curanswer == 94):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆IIII")
	if (curanswer == 95):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌")
	if (curanswer == 96):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌I")
	if (curanswer == 97):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌II")
	if (curanswer == 98):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌III")
	if (curanswer == 99):
		greekNumeral = str("∆∆∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 100):
		greekNumeral = str("H")
	if (curanswer == 101):
		greekNumeral = str("HI")
	if (curanswer == 102):
		greekNumeral = str("HII")
	if (curanswer == 103):
		greekNumeral = str("HIII")
	if (curanswer == 104):
		greekNumeral = str("HIIII")
	if (curanswer == 105):
		greekNumeral = str("H┌")
	if (curanswer == 106):
		greekNumeral = str("H┌I")
	if (curanswer == 107):
		greekNumeral = str("H┌II")
	if (curanswer == 108):
		greekNumeral = str("H┌III")
	if (curanswer == 109):
		greekNumeral = str("H┌IIII")
	if (curanswer == 110):
		greekNumeral = str("H∆")
	if (curanswer == 111):
		greekNumeral = str("H∆I")
	if (curanswer == 112):
		greekNumeral = str("H∆II")
	if (curanswer == 113):
		greekNumeral = str("H∆III")
	if (curanswer == 114):
		greekNumeral = str("H∆IIII")
	if (curanswer == 115):
		greekNumeral = str("H∆┌")
	if (curanswer == 116):
		greekNumeral = str("H∆┌I")
	if (curanswer == 117):
		greekNumeral = str("H∆┌II")
	if (curanswer == 118):
		greekNumeral = str("H∆┌III")
	if (curanswer == 119):
		greekNumeral = str("H∆┌IIII")
	if (curanswer == 120):
		greekNumeral = str("H∆∆")
	if (curanswer == 121):
		greekNumeral = str("H∆∆I")	
	if (curanswer == 122):
		greekNumeral = str("H∆∆II")	
	if (curanswer == 123):
		greekNumeral = str("H∆∆III")
	if (curanswer == 124):
		greekNumeral = str("H∆∆IIII")	
	if (curanswer == 125):
		greekNumeral = str("H∆∆┌")
	if (curanswer == 126):
		greekNumeral = str("H∆∆┌I")	
	if (curanswer == 127):
		greekNumeral = str("H∆∆┌II")
	if (curanswer == 128):
		greekNumeral = str("H∆∆┌III")		
	if (curanswer == 129):
		greekNumeral = str("H∆∆┌IIII")	
	if (curanswer == 130):
		greekNumeral = str("H∆∆∆")	
	if (curanswer == 131):
		greekNumeral = str("H∆∆∆I")
	if (curanswer == 132):
		greekNumeral = str("H∆∆∆II")
	if (curanswer == 133):
		greekNumeral = str("H∆∆∆III")
	if (curanswer == 134):
		greekNumeral = str("H∆∆∆IIII")
	if (curanswer == 135):
		greekNumeral = str("H∆∆∆┌")
	if (curanswer == 136):
		greekNumeral = str("H∆∆∆┌I")
	if (curanswer == 137):
		greekNumeral = str("H∆∆∆┌II")
	if (curanswer == 138):
		greekNumeral = str("H∆∆∆┌III")
	if (curanswer == 139):
		greekNumeral = str("H∆∆∆┌IIII")
	if (curanswer == 140):
		greekNumeral = str("H∆∆∆∆")
	if (curanswer == 141):
		greekNumeral = str("H∆∆∆∆I")
	if (curanswer == 142):
		greekNumeral = str("H∆∆∆∆II")
	if (curanswer == 143):
		greekNumeral = str("H∆∆∆∆III")
	if (curanswer == 144):
		greekNumeral = str("H∆∆∆∆IIII")
	if (curanswer == 145):
		greekNumeral = str("H∆∆∆∆┌")
	if (curanswer == 146):
		greekNumeral = str("H∆∆∆∆┌I")
	if (curanswer == 147):
		greekNumeral = str("H∆∆∆∆┌II")
	if (curanswer == 148):
		greekNumeral = str("H∆∆∆∆┌III")
	if (curanswer == 149):
		greekNumeral = str("H∆∆∆∆┌IIII")
	if (curanswer == 150):
		greekNumeral = str("H∆∆∆∆∆")
	if (curanswer == 151):
		greekNumeral = str("H∆∆∆∆∆I")
	if (curanswer == 152):
		greekNumeral = str("H∆∆∆∆∆II")	
	if (curanswer == 153):
		greekNumeral = str("H∆∆∆∆∆III")
	if (curanswer == 154):
		greekNumeral = str("H∆∆∆∆∆IIII")
	if (curanswer == 155):
		greekNumeral = str("H∆∆∆∆∆┌")		
	if (curanswer == 156):
		greekNumeral = str("H∆∆∆∆∆┌I")		
	if (curanswer == 157):
		greekNumeral = str("H∆∆∆∆∆┌II")	
	if (curanswer == 158):
		greekNumeral = str("H∆∆∆∆∆┌III")
	if (curanswer == 159):
		greekNumeral = str("H∆∆∆∆∆┌IIII")
	if (curanswer == 160):
		greekNumeral = str("H∆∆∆∆∆∆")
	if (curanswer == 161):
		greekNumeral = str("H∆∆∆∆∆∆I")
	if (curanswer == 162):
		greekNumeral = str("H∆∆∆∆∆∆II")
	if (curanswer == 163):
		greekNumeral = str("H∆∆∆∆∆∆III")
	if (curanswer == 164):
		greekNumeral = str("H∆∆∆∆∆∆IIII")
	if (curanswer == 165):
		greekNumeral = str("H∆∆∆∆∆∆┌")
	if (curanswer == 166):
		greekNumeral = str("H∆∆∆∆∆∆┌I")
	if (curanswer == 167):
		greekNumeral = str("H∆∆∆∆∆∆┌II")
	if (curanswer == 168):
		greekNumeral = str("H∆∆∆∆∆∆┌III")
	if (curanswer == 169):
		greekNumeral = str("H∆∆∆∆∆∆┌IIII")
	if (curanswer == 170):
		greekNumeral = str("H∆∆∆∆∆∆∆")
	if (curanswer == 171):
		greekNumeral = str("H∆∆∆∆∆∆∆I")
	if (curanswer == 172):
		greekNumeral = str("H∆∆∆∆∆∆∆II")
	if (curanswer == 173):
		greekNumeral = str("H∆∆∆∆∆∆∆III")
	if (curanswer == 174):
		greekNumeral = str("H∆∆∆∆∆∆∆IIII")
	if (curanswer == 175):
		greekNumeral = str("H∆∆∆∆∆∆∆┌")
	if (curanswer == 176):
		greekNumeral = str("H∆∆∆∆∆∆∆┌I")
	if (curanswer == 177):
		greekNumeral = str("H∆∆∆∆∆∆∆┌II")
	if (curanswer == 178):
		greekNumeral = str("H∆∆∆∆∆∆∆┌III")
	if (curanswer == 179):
		greekNumeral = str("H∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 180):
		greekNumeral = str("H∆∆∆∆∆∆∆∆")
	if (curanswer == 181):
		greekNumeral = str("H∆∆∆∆∆∆∆∆I")
	if (curanswer == 182):
		greekNumeral = str("H∆∆∆∆∆∆∆∆II")
	if (curanswer == 183):
		greekNumeral = str("H∆∆∆∆∆∆∆∆III")
	if (curanswer == 184):
		greekNumeral = str("H∆∆∆∆∆∆∆∆IIII")
	if (curanswer == 185):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌")
	if (curanswer == 186):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌I")
	if (curanswer == 187):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌II")
	if (curanswer == 188):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌III")
	if (curanswer == 189):
		greekNumeral = str("H∆∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 190):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆")
	if (curanswer == 191):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆I")
	if (curanswer == 192):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆II")
	if (curanswer == 193):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆III")
	if (curanswer == 194):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆IIII")
	if (curanswer == 195):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌")
	if (curanswer == 196):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌I")
	if (curanswer == 197):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌II")
	if (curanswer == 198):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌III")
	if (curanswer == 199):
		greekNumeral = str("H∆∆∆∆∆∆∆∆∆┌IIII")
	if (curanswer == 200):
		greekNumeral = str("HH")
	if (curanswer == 201):
		greekNumeral = str("HHI")
	if (curanswer == 202):
		greekNumeral = str("HHII")
	if (curanswer == 203):
		greekNumeral = str("HHIII")
	if (curanswer == 204):
		greekNumeral = str("HHIIII")
	if (curanswer == 205):
		greekNumeral = str("HH┌")
	if (curanswer == 206):
		greekNumeral = str("HH┌I")
	if (curanswer == 207):
		greekNumeral = str("HH┌II")
	if (curanswer == 208):
		greekNumeral = str("HH┌III")
	if (curanswer == 209):
		greekNumeral = str("HH┌IIII")
	if (curanswer == 210):
		greekNumeral = str("HH∆")
	if (curanswer == 211):
		greekNumeral = str("HH∆I")
	if (curanswer == 212):
		greekNumeral = str("HH∆II")
	if (curanswer == 213):
		greekNumeral = str("HH∆III")
	if (curanswer == 214):
		greekNumeral = str("HH∆IIII")
	if (curanswer == 215):
		greekNumeral = str("HH∆┌")
	if (curanswer == 216):
		greekNumeral = str("HH∆┌I")
	if (curanswer == 217):
		greekNumeral = str("HH∆┌II")
	if (curanswer == 218):
		greekNumeral = str("HH∆┌III")
	if (curanswer == 219):
		greekNumeral = str("HH∆┌IIII")
	if (curanswer == 220):
		greekNumeral = str("HH∆∆")
	if (curanswer == 221):
		greekNumeral = str("HH∆∆I")
	if (curanswer == 222):
		greekNumeral = str("HH∆∆II")
	if (curanswer == 223):
		greekNumeral = str("HH∆∆III")
	if (curanswer == 224):
		greekNumeral = str("HH∆∆IIII")
	if (curanswer == 225):
		greekNumeral = str("HH∆∆┌")
	if (curanswer == 226):
		greekNumeral = str("HH∆∆┌I")
	if (curanswer == 227):
		greekNumeral = str("HH∆∆┌II")
	if (curanswer == 228):
		greekNumeral = str("HH∆∆┌III")
	if (curanswer == 229):
		greekNumeral = str("HH∆∆┌IIII")
	if (curanswer == 230):
		greekNumeral = str("HH∆∆∆")
	if (curanswer == 231):
		greekNumeral = str("HH∆∆∆I")
	if (curanswer == 232):
		greekNumeral = str("HH∆∆∆II")
	if (curanswer == 233):
		greekNumeral = str("HH∆∆∆III")
	if (curanswer == 234):
		greekNumeral = str("HH∆∆∆IIII")
	if (curanswer == 235):
		greekNumeral = str("HH∆∆∆┌")
	if (curanswer == 236):
		greekNumeral = str("HH∆∆∆┌I")
	if (curanswer == 237):
		greekNumeral = str("HH∆∆∆┌II")
	if (curanswer == 238):
		greekNumeral = str("HH∆∆∆┌III")
	if (curanswer == 239):
		greekNumeral = str("HH∆∆∆┌IIII")
	if (curanswer == 240):
		greekNumeral = str("HH∆∆∆∆")
	if (curanswer == 241):
		greekNumeral = str("HH∆∆∆∆I")
	if (curanswer == 242):
		greekNumeral = str("HH∆∆∆∆II")
	if (curanswer == 243):
		greekNumeral = str("HH∆∆∆∆III")
	if (curanswer == 244):
		greekNumeral = str("HH∆∆∆∆IIII")
	if (curanswer == 245):
		greekNumeral = str("HH∆∆∆∆┌")
	if (curanswer == 246):
		greekNumeral = str("HH∆∆∆∆┌I")
	if (curanswer == 247):
		greekNumeral = str("HH∆∆∆∆┌II")
	if (curanswer == 248):
		greekNumeral = str("HH∆∆∆∆┌III")
	if (curanswer == 249):
		greekNumeral = str("HH∆∆∆∆┌IIII")
	if (curanswer == 250):
		greekNumeral = str("HH∆∆∆∆∆")
	if (curanswer == 251):
		greekNumeral = str("HH∆∆∆∆∆I")
	if (curanswer == 252):
		greekNumeral = str("HH∆∆∆∆∆II")
	if (curanswer == 253):
		greekNumeral = str("HH∆∆∆∆∆III")
	if (curanswer == 254):
		greekNumeral = str("HH∆∆∆∆∆IIII")
	if (curanswer == 255):
		greekNumeral = str("HH∆∆∆∆∆┌")
	if (curanswer == 256):
		greekNumeral = str("HH∆∆∆∆∆┌I")
	print ("| Translation in greek numerals: " + str(greekNumeral))
noMore = input("Press [ENTER] key to quit")
'''
print ("NOTICE! ")
print ("Sean was unable to find Unicode characters that match the Greek Numerals, so he chose some that look closest")
print ("Guide: ")
print ("1 = I")
print ("5 = ┌")
print ("10 = ∆")
print ("100 = H")
print ("1000 = X")
'''
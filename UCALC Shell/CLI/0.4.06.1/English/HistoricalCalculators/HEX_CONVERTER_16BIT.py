print (" ")
print (" ")
print (" _   _  ____  _  _    __    ____  ____  ___  ____  __  __    __    __    ")
print ("( )_( )( ___)( \\/ )  /__\\  (  _ \\( ___)/ __)(_  _)(  \\/  )  /__\\  (  )   ")
print (" ) _ (  )__)  )  (  /(__)\\  )(_) ))__)( (__  _)(_  )    (  /(__)\\  )(__  ")
print ("(_) (_)(____)(_/\\_)(__)(__)(____/(____)\\___)(____)(_/\\/\\_)(__)(__)(____)  ")
print ("  ___  _____  _  _  _  _  ____  ____  ____  ____  ____                 ")  
print (" / __)(  _  )( \\( )( \\/ )( ___)(  _ \\(_  _)( ___)(  _ \\        ")          
print ("( (__  )(_)(  )  (  \\  /  )__)  )   /  )(   )__)  )   /        ")          
print (" \\___)(_____)(_)\\_)  \\/  (____)(_)\\_) (__) (____)(_)\\_)          ")        
print (" ")
print ("(!) This program is locked in 8 bit mode")
newHex = int(input("Enter a number to convert to hexadecimal (NO DECIMALS): "))
if (newHex > 65336):
    print ("The number you entered is too high! Quitting...")
if (newHex < 1):
    print ("The value you entered is too low! Qutting...")
else:
	x = hex(newHex)
	print ("The answer is: " + x)
	addItQues = str(input("Do you want to add a number to that? (y/n): "))
	if (addItQues == "y"):
		print ("Calculation ID table")
		print ("Addition         | ID: 1 | Calculation type: + |")
		print ("Subtraction      | ID: 2 | Calculation type: - |")
		print ("Multiplication   | ID: 3 | Calculation type: * |")
		print ("Division         | ID: 4 | Calculation type: / |")
		print ("Modular division | ID: 5 | Calculation type: % |")
		newNumber = str(input("Enter an ID to continue: "))
		if (newNumber == "1"):
			newHex2 = int(input("Enter a second number: "))
			if (newHex2 > 65336):
				print ("The value you entered is too high! Qutting...")
			if (newHex2 < 1):
				print ("The value you entered is too low! Qutting...")
			else:
				z = int(newHex + newHex2)
				if (z > 65336):
					print ("Overflow error! Calculated number is too high")
				if (z < 1):
					print ("The calculated number is too low")
				else:
					if (z < 65336 and z > 1):
						y = hex(newHex + newHex2)
						print ("The answer is: " + y)
		if (newNumber == "2"):
			newHex2 = int(input("Enter a second number: "))
			if (newHex2 > 65336):
				print ("The value you entered is too high! Qutting...")
			if (newHex2 < 1):
				print ("The value you entered is too low! Qutting...")
			else:
				z = int(newHex + newHex2)
				if (z > 65336):
					print ("Overflow error! Calculated number is too high")
				if (z < 1):
					print ("The calculated number is too low")
				else:
					if (z < 65336 and z > 1):
						y = hex(newHex - newHex2)
						print ("The answer is: " + y)
		if (newNumber == "3"):
			newHex2 = int(input("Enter a second number: "))
			if (newHex2 > 65336):
				print ("The value you entered is too high! Qutting...")
			if (newHex2 < 1):
				print ("The value you entered is too low! Qutting...")
			else:
				z = int(newHex + newHex2)
				if (z > 65336):
					print ("Overflow error! Calculated number is too high")
				if (z < 1):
					print ("The calculated number is too low")
				else:
					if (z < 65336 and z > 1):
						y = hex(newHex * newHex2) 
						print ("The answer is: " + y) 
		if (newNumber == "4"):
			newHex2 = int(input("Enter a second number: "))
			if (newHex2 > 65336):
				print ("The value you entered is too high! Qutting...")
			if (newHex2 < 1):
				print ("The value you entered is too low! Qutting...")
			else:
				z = int(newHex + newHex2)
				if (z > 65336):
					print ("Overflow error! Calculated number is too high")
				if (z < 1):
					print ("The calculated number is too low")
				else:
					if (z < 65336 and z > 1):
						y = hex(newHex / newHex2) 
						print ("The answer is: " + y)
		if (newNumber == "5"):
			newHex2 = int(input("Enter a second number: "))
			if (newHex2 > 65336):
				print ("The value you entered is too high! Qutting...")
			if (newHex2 < 1):
				print ("The value you entered is too low! Qutting...")
			else:
				z = int(newHex + newHex2)
				if (z > 65336):
					print ("Overflow error! Calculated number is too high")
				if (z < 1):
					print ("The calculated number is too low")
				else:
					if (z < 65336 and z > 1):
						y = hex(newHex % newHex2)
						print ("The answer is: " + y)
		if not (newNumber == "1" or "2" or "3" or "4" or "5"):
			print ("Invalid ID entered!") 
noMore = input("Press [ENTER] key to quit")
'''

<*>This program is confirmed to be fully functional and understandable! :) - Sean Myrick on 11/25/2018

'''
# ASCII art that says "ROMAN NUMERAL CALCULATOR" #
print (" ____  _____  __  __    __    _  _    _  _  __  __  __  __  ____  ____    __    __   ")
print ("(  _ \\(  _  )(  \\/  )  /__\\  ( \\( )  ( \\( )(  )(  )(  \\/  )( ___)(  _ \\  /__\\  (  )  ")
print (" )   / )(_)(  )    (  /(__)\\  )  (    )  (  )(__)(  )    (  )__)  )   / /(__)\\  )(__ ")
print ("(_)\\_)(_____)(_/\\/\\_)(__)(__)(_)\\_)  (_)\\_)(______)(_/\\/\\_)(____)(_)\\_)(__)(__)(____)")
print ("  ___    __    __    ___  __  __  __      __   ____  _____  ____        ")             
print (" / __)  /__\\  (  )  / __)(  )(  )(  )    /__\\ (_  _)(  _  )(  _ \\     ")               
print ("( (__  /(__)\\  )(__( (__  )(__)(  )(__  /(__)\\  )(   )(_)(  )   /   ")                 
print (" \\___)(__)(__)(____)\\___)(______)(____)(__)(__)(__) (_____)(_)\\_) ")                   
print ("\n\n")
tripToRome = str(input("Press [ENTER] key to start"))
# this is branched off old source code. Extra junk was added so that it matched the old case #
if (tripToRome == ""):
	if (tripToRome == ""):
		if (tripToRome == ""):
			calcIDSes = int(55)
			if (tripToRome == ""):
				print ("\n\n\n\n\n\n\n\n\n\n\n\n")
				if calcIDSes == 55:
					# options table #
					print ("Roman numeral calculator")
					print ("NOTICE: this calculator is locked in 4 BIT MODE")
					print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
					print ("▒ Modes           ▒ ID LIST ▒")
					print ("▒ int -> numeral  ▒ ID: 1   ▒")
					print ("▒ numeral -> int  ▒ ID: 2   ▒")
					print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
					getInputForRomeA = int(input("Enter an ID to start >> "))
					# int to numeral mode #
					if getInputForRomeA == 1:
						getInputForRome1 = int(input("Enter a number to calculate: "))
						print ("Addition            [ID: 1]")
						print ("Subtraction         [ID: 2]")
						print ("Multiplication      [ID: 3]")
						print ("Division            [ID: 4]")
						print ("Modular division    [ID: 5]")
						getInputForRome2 = int(input("What type of calculation do you want to do out of the given options? Enter ID here: "))
						getInputForRome3 = int(input("Enter the second number to calculate: "))
						if getInputForRome2 == 1:
							preRome = int(getInputForRome1 + getInputForRome3)
						if getInputForRome2 == 2:
							preRome = int(getInputForRome1 - getInputForRome3)
						if getInputForRome2 == 3:
							preRome = int(getInputForRome1 * getInputForRome3)	
						if getInputForRome2 == 4:
							preRome = int(getInputForRome1 / getInputForRome3)	
						if getInputForRome2 == 5:
							preRome = int(getInputForRome1 % getInputForRome3)
						if preRome < 1:
							print ("Syntax error! The number you entered is too small to be transferred as a roman numeral")
						if preRome == 1:
							print ("The answer is I")
						if preRome == 2:
							print ("The answer is II")
						if preRome == 3:
							print ("The answer is III")
						if preRome == 4:
							print ("The answer is IV")
						if preRome == 5:
							print ("The answer is V")
						if preRome == 6:
							print ("The answer is VI")
						if preRome == 7:
							print ("The answer is VII")
						if preRome == 8:
							print ("The answer is VIII")
						if preRome == 9:
							print ("The answer is IX")
						if preRome == 10:
							print ("The answer is X")
						if preRome == 11:
							print ("The answer is XI")
						if preRome == 12:
							print ("The answer is XII")
						if preRome == 13:
							print ("The answer is XIII")
						if preRome == 14:
							print ("The answer is XIV")
						if preRome == 15:
							print ("The answer is XV")
						if preRome == 16:
							print ("The answer is XVI")	
						if preRome > 16:
							print ("Syntax error! The number you entered is too large to be transferred as a roman numeral")
						# numeral to int mode #
					if getInputForRomeA == 2:
						romeReversi = str(input("Enter a roman numeral to convert: "))
						# UPPERCASE
						if (romeReversi == "I"):
							print ("This is equal to 1")
						if (romeReversi == "II"):
							print ("This is equal to 2")
						if (romeReversi == "III"):
							print ("This is equal to 3")
						if (romeReversi == "IV"):
							print ("This is equal to 4")
						if (romeReversi == "IIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 4")
						if (romeReversi == "V"):
							print ("This is equal to 5")
						if (romeReversi == "VI"):
							print ("This is equal to 6")
						if (romeReversi == "VII"):
							print ("This is equal to 7")
						if (romeReversi == "VIII"):
							print ("This is equal to 8")
						if (romeReversi == "IX"):
							print ("This is equal to 9")
						if (romeReversi == "VIIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 9")
						if (romeReversi == "X"):
							print ("This is equal to 10")
						if (romeReversi == "XI"):
							print ("This is equal to 11")
						if (romeReversi == "XII"):
							print ("This is equal to 12")
						if (romeReversi == "XIII"):
							print ("This is equal to 13")
						if (romeReversi == "XIV"):
							print ("This is equal to 14")
						if (romeReversi == "XIIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 14")
						if (romeReversi == "XV"):
							print ("This is equal to 15")
						if (romeReversi == "XVI"):
							print ("This is equalk to 16")
						# lowercase
						if (romeReversi == "i"):
							print ("This is equal to 1")
						if (romeReversi == "ii"):
							print ("This is equal to 2")
						if (romeReversi == "iii"):
							print ("This is equal to 3")
						if (romeReversi == "iv"):
							print ("This is equal to 4")
						if (romeReversi == "iiii"):  # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 4")
						if (romeReversi == "v"):
							print ("This is equal to 5")
						if (romeReversi == "vi"):
							print ("This is equal to 6")
						if (romeReversi == "vii"):
							print ("This is equal to 7")
						if (romeReversi == "viii"):
							print ("This is equal to 8")
						if (romeReversi == "ix"):
							print ("This is equal to 9")
						if (romeReversi == "viiii"): # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 9")
						if (romeReversi == "x"):
							print ("This is equal to 10")
						if (romeReversi == "xi"):
							print ("This is equal to 11")
						if (romeReversi == "xii"):
							print ("This is equal to 12")
						if (romeReversi == "xiii"):
							print ("This is equal to 13")
						if (romeReversi == "xiv"):
							print ("This is equal to 14")
						if (romeReversi == "xiiii"): # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 14")
						if (romeReversi == "xv"):
							print ("This is equal to 15")
						if (romeReversi == "xvi"):
							print ("This is equal to 16")
						else:
							print ("Invalid numeral entered!")
# ends the program #
endRome = input("Press [ENTER] key to quit")
# end of script # 175 lines of code # 7530 bytes total #
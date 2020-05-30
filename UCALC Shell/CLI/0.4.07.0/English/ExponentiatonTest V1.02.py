# start of script
loopCon = int(1) # loop static variable (integer)
while (loopCon == 1): # loop confirmer, as loopCon will ALWAYS be 1 until changed 
	print ("Exponentiation Test") # title
	print ("Choose a calculation mode (or type 2 for help): ") # mode info
	print ("-----") # divider 
	exponchoice = str(input("Float (0) Int (1): ")) # mode string (for all 3 modes, only 2 listed on line)
	if (exponchoice == "0"): # option 1: float mode
		exponentiationTest = float(input("Enter the first number: ")) # gets the first float number
		exponentiationTest2 = float(input("Enter the second number: ")) # gets the second float number
		answer = float(exponentiationTest ** exponentiationTest2) # exponentiates the 2 numbers 
		noMore = input("The exponentiation of " + str(exponentiationTest) + " and " + str(exponentiationTest2) + " is " + str(answer) + ".") # prints out the sum (answer)
	if (exponchoice == "1"): # option 2: integer mode  
		exponentiationTest = int(input("Enter the first number: ")) # gets the first integer 
		exponentiationTest2 = int(input("Enter the second number: ")) # gets the second integer
		answer = int(exponentiationTest ** exponentiationTest2) # exponentiates the 2 numbers 
		noMore = input("The exponentiation of " + str(exponentiationTest) + " and " + str(exponentiationTest2) + " is " + str(answer) + ".") # prints out the sum (answer)
	if (exponchoice == "2"): # option 3: about mode
		print ("Exponentiation test for UCALC") # title
		print ("Help guide") # heading
		print ("\nLimits of the float calculator") # section 1
		# This program was written in Python. Because of this, in float mode, an integer overflow
		print ("The float calculation mode takes 2 float values (numbers with decimals) and powers them. Since decimals are involved, overflow is much easier, as it has a set limit for all 64 bit and 32 bit architectures") # sentence 1
		print ("FOR 32 BIT MACHINES") # sentence 2
		print ("This hasn't been documented yet") # sentence 3
		print ("FOR 64 BIT MACHINES") # sentence 4
		print ("Before you are met with E+[number] you can go through 53 different powers of 2 (on a 64 bit system) once you type in [2] then [54] you are met with the E+#") # sentence 5
		print ("<content missing>") # section 1 content 
		print ("\nLimits of the int calculator") # section 2
		# ??? (no description has been written. I need to do more research on these 2 subjects
		print ("<content missing>") # section 2 content
		noMore = input("\nPress [ENTER] key to exit help guide") # once the help guide is printed, just press [ENTER] to get out of it, and go back into the mode info
noMore = input("Thank you for testing this program! ") # if the loop is stopped, this is the last line that is printed in your session. Pressing [ENTER] will closer the Window
print ("Goodbye") # exit message (not readable, as the console closes so fast)
''' version 1.00 '''
# test of exponentiation in Python
# experimented 8:39 am on January 25th 2019
''' version 1.01 '''
# slight bloat with comments 
# added loop 
# replaced settings 'int' with 'str'
# added help panel (currently incomplete)
# added comment update log 
# added 6:00 pm on March 30th 2019
''' version 1.02 '''
# changes to comments (comments on every line, with updates to older comments
''' end of script '''
# end of comments (43 lines total) (less than 4 kilobytes in size for whole script)
# start of script
loopCon = int(1)
while (loopCon == 1):
	print ("Exponentiation Test")
	print ("Choose a calculation mode (or type 2 for help): ")
	print ("-----")
	exponchoice = str(input("Float (0) Int (1): "))
	if (exponchoice == "0"): # option 1: float mode
		exponentiationTest = float(input("Enter the first number: "))
		exponentiationTest2 = float(input("Enter the second number: "))
		answer = float(exponentiationTest ** exponentiationTest2)
		noMore = input("The exponentiation of " + str(exponentiationTest) + " and " + str(exponentiationTest2) + " is " + str(answer) + ".")
	if (exponchoice == "1"): # option 2: integer mode  
		exponentiationTest = int(input("Enter the first number: "))
		exponentiationTest2 = int(input("Enter the second number: "))
		answer = int(exponentiationTest ** exponentiationTest2)
		noMore = input("The exponentiation of " + str(exponentiationTest) + " and " + str(exponentiationTest2) + " is " + str(answer) + ".")
	if (exponchoice == "2"): # option 3: about mode
		print ("Exponentiation test for UCALC")
		print ("Help guide")
		print ("\nLimits of the float calculator")
		# This program was written in Python. Because of this, in float mode, an integer overflow
		print ("<content missing>")
		print ("\nLimits of the int calculator")
		# ??? (no description has been written. I need to do more research on these 2 subjects
		print ("<content missing>")
		noMore = input("\nPress [ENTER] key to exit help guide")
noMore = input("Thank you for testing this program! ")
print ("Goodbye")
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
''' end of script '''
# end of comments (41 lines total) (less than 2 kilobytes in size for whole script)
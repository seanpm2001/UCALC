import random 
print ("Random equation Calculator")
looforever = int(1)
enterToEnter = input("Press [ENTER] key to start")
while looforever == 1:
	print ("\n\n\nSelect a mode: ")
	print ("\nAddition (1)")
	print ("\nSubtraction (2) ")
	print ("\nMultiplication (3)")
	print ("\nDivision (4)")
	print ("\nModular division (5)")
	print ("\nSuprise me (6)")
	IDStart = int(input("Enter an ID to start: "))
	if (IDStart == 1):
		print ("Create a randomized addition equation")
		print ("Enter a length for the first number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p1 = int(random.randint(1, 9))
		if ranID == 2:
			p1 = int(random.randint(10, 99))
		if ranID == 3:
			p1 = int(random.randint(100, 999))
		if ranID == 4:
			p1 = int(random.randint(1000, 9999))
		if ranID == 5:
			p1 = int(random.randint(10000, 99999))
		if ranID == 6:
			p1 = int(random.randint(100000, 999999))
		if ranID == 7:
			p1 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p1 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p1 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p1 = int(random.randint(1000000000, 9999999999))
		print ("Enter a length for the second number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p2 = int(random.randint(1, 9))
		if ranID == 2:
			p2 = int(random.randint(10, 99))
		if ranID == 3:
			p2 = int(random.randint(100, 999))
		if ranID == 4:
			p2 = int(random.randint(1000, 9999))
		if ranID == 5:
			p2 = int(random.randint(10000, 99999))
		if ranID == 6:
			p2 = int(random.randint(100000, 999999))
		if ranID == 7:
			p2 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p2 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p2 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p2 = int(random.randint(1000000000, 9999999999))
		p3 = int(p1 + p2)
		print ("You generated this addition problem: ")
		print (str(p1)	+ " + " + str(p2) + " = " + str(p3))
		noMore = input("Press [ENTER] key to exit")
	if (IDStart == 2):
		print ("Create a randomized subtraction equation")
		print ("Enter a length for the first number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p1 = int(random.randint(1, 9))
		if ranID == 2:
			p1 = int(random.randint(10, 99))
		if ranID == 3:
			p1 = int(random.randint(100, 999))
		if ranID == 4:
			p1 = int(random.randint(1000, 9999))
		if ranID == 5:
			p1 = int(random.randint(10000, 99999))
		if ranID == 6:
			p1 = int(random.randint(100000, 999999))
		if ranID == 7:
			p1 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p1 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p1 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p1 = int(random.randint(1000000000, 9999999999))
		print ("Enter a length for the second number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p2 = int(random.randint(1, 9))
		if ranID == 2:
			p2 = int(random.randint(10, 99))
		if ranID == 3:
			p2 = int(random.randint(100, 999))
		if ranID == 4:
			p2 = int(random.randint(1000, 9999))
		if ranID == 5:
			p2 = int(random.randint(10000, 99999))
		if ranID == 6:
			p2 = int(random.randint(100000, 999999))
		if ranID == 7:
			p2 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p2 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p2 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p2 = int(random.randint(1000000000, 9999999999))
		p3 = int(p1 - p2)
		print ("You generated this subtraction problem: ")
		print (str(p1)	+ " - " + str(p2) + " = " + str(p3))
		noMore = input("Press [ENTER] key to exit")
	if (IDStart == 3):
		print ("Create a randomized multiplicatioi equation")
		print ("Enter a length for the first number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p1 = int(random.randint(1, 9))
		if ranID == 2:
			p1 = int(random.randint(10, 99))
		if ranID == 3:
			p1 = int(random.randint(100, 999))
		if ranID == 4:
			p1 = int(random.randint(1000, 9999))
		if ranID == 5:
			p1 = int(random.randint(10000, 99999))
		if ranID == 6:
			p1 = int(random.randint(100000, 999999))
		if ranID == 7:
			p1 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p1 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p1 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p1 = int(random.randint(1000000000, 9999999999))
		print ("Enter a length for the second number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p2 = int(random.randint(1, 9))
		if ranID == 2:
			p2 = int(random.randint(10, 99))
		if ranID == 3:
			p2 = int(random.randint(100, 999))
		if ranID == 4:
			p2 = int(random.randint(1000, 9999))
		if ranID == 5:
			p2 = int(random.randint(10000, 99999))
		if ranID == 6:
			p2 = int(random.randint(100000, 999999))
		if ranID == 7:
			p2 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p2 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p2 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p2 = int(random.randint(1000000000, 9999999999))
		p3 = int(p1 * p2)
		print ("You generated this multiplication problem: ")
		print (str(p1)	+ " * " + str(p2) + " = " + str(p3))
		noMore = input("Press [ENTER] key to exit")
	if (IDStart == 4):
		print ("Create a randomized division equation")
		print ("Enter a length for the first number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p1 = int(random.randint(1, 9))
		if ranID == 2:
			p1 = int(random.randint(10, 99))
		if ranID == 3:
			p1 = int(random.randint(100, 999))
		if ranID == 4:
			p1 = int(random.randint(1000, 9999))
		if ranID == 5:
			p1 = int(random.randint(10000, 99999))
		if ranID == 6:
			p1 = int(random.randint(100000, 999999))
		if ranID == 7:
			p1 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p1 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p1 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p1 = int(random.randint(1000000000, 9999999999))
		print ("Enter a length for the second number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p2 = int(random.randint(1, 9))
		if ranID == 2:
			p2 = int(random.randint(10, 99))
		if ranID == 3:
			p2 = int(random.randint(100, 999))
		if ranID == 4:
			p2 = int(random.randint(1000, 9999))
		if ranID == 5:
			p2 = int(random.randint(10000, 99999))
		if ranID == 6:
			p2 = int(random.randint(100000, 999999))
		if ranID == 7:
			p2 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p2 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p2 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p2 = int(random.randint(1000000000, 9999999999))
		p3 = int(p1 / p2)
		print ("You generated this division problem: ")
		print (str(p1)	+ " / " + str(p2) + " = " + str(p3))
		noMore = input("Press [ENTER] key to exit")
	if (IDStart == 5):
		print ("Create a randomized modular dvision equation")
		print ("Enter a length for the first number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p1 = int(random.randint(1, 9))
		if ranID == 2:
			p1 = int(random.randint(10, 99))
		if ranID == 3:
			p1 = int(random.randint(100, 999))
		if ranID == 4:
			p1 = int(random.randint(1000, 9999))
		if ranID == 5:
			p1 = int(random.randint(10000, 99999))
		if ranID == 6:
			p1 = int(random.randint(100000, 999999))
		if ranID == 7:
			p1 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p1 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p1 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p1 = int(random.randint(1000000000, 9999999999))
		print ("Enter a length for the second number")
		print ("length of 1 (1) ")
		print ("Length of 2 (2) ")
		print ("Length of 3 (3) ")
		print ("Length of 4 (4) ")
		print ("Length of 5 (5) ")
		print ("Length of 6 (6) ")
		print ("Length of 7 (7) ")
		print ("Length of 8 (8) ")
		print ("Length of 9 (9( ")
		print ("Length of 10 (0) ")
		ranID = int(input("Enter an ID to continue: "))
		if ranID == 1:
			p2 = int(random.randint(1, 9))
		if ranID == 2:
			p2 = int(random.randint(10, 99))
		if ranID == 3:
			p2 = int(random.randint(100, 999))
		if ranID == 4:
			p2 = int(random.randint(1000, 9999))
		if ranID == 5:
			p2 = int(random.randint(10000, 99999))
		if ranID == 6:
			p2 = int(random.randint(100000, 999999))
		if ranID == 7:
			p2 = int(random.randint(1000000, 9999999))
		if ranID == 8:
			p2 = int(random.randint(10000000, 99999999))
		if ranID == 9:
			p2 = int(random.randint(100000000, 999999999))
		if ranID == 0:
			p2 = int(random.randint(1000000000, 9999999999))
		p3 = int(p1 % p2)
		print ("You generated this modular division problem: ")
		print (str(p1)	+ " % " + str(p2) + " = " + str(p3))
		noMore = input("Press [ENTER] key to exit")
	if (IDStart == 6):
		print ("Generating a random equation")
		ranRange = int(random.randint(1, 9))
		if (ranRange == 1):
			p1 = int(random.randint(1, 9))
		if (ranRange == 2):
			p1 = int(random.randint(10, 99))
		if (ranRange == 3):
			p1 = int(random.randint(100, 999))
		if (ranRange == 4):
			p1 = int(random.randint(1000, 9999))
		if (ranRange == 5):
			p1 = int(random.randint(10000, 99999))
		if (ranRange == 6):
			p1 = int(random.randint(100000, 999999))
		if (ranRange == 7):
			p1 = int(random.randint(0000000, 9999999))
		if (ranRange == 8):
			p1 = int(random.randint(10000000, 99999999))
		if (ranRange == 9):
			p1 = int(random.randint(100000000, 999999999))
		ranExpo = int(random.randint(1, 5))
		ranRange2 = int(random.randint(1, 9))
		if (ranRange2 == 1):
			p2 = int(random.randint(1, 9))
		if (ranRange2 == 2):
			p2 = int(random.randint(10, 99))
		if (ranRange2 == 3):
			p2 = int(random.randint(100, 999))
		if (ranRange2 == 4):
			p2 = int(random.randint(1000, 9999))
		if (ranRange2 == 5):
			p2 = int(random.randint(10000, 99999))
		if (ranRange2 == 6):
			p2 = int(random.randint(100000, 999999))
		if (ranRange2 == 7):
			p2 = int(random.randint(0000000, 9999999))
		if (ranRange2 == 8):
			p2 = int(random.randint(10000000, 99999999))
		if (ranRange2 == 9):
			p2 = int(random.randint(100000000, 999999999))
		if (ranExpo == 1):
			answer = int(p1 + p2)
			print ("You generated this equation: ")
			print (str(p1) + " + " + str(p2) + " = " + str(answer))
		if (ranExpo == 2):
			answer = int(p1 - p2)
			print ("You generated this equation: ")
			print (str(p1) + " - " + str(p2) + " = " + str(answer))
		if (ranExpo == 3):
			answer = int(p1 * p2)
			print ("You generated this equation: ")
			print (str(p1) + " * " + str(p2) + " = " + str(answer))
		if (ranExpo == 4):
			answer = int(p1 / p2)
			print ("You generated this equation: ")
			print (str(p1) + " / " + str(p2) + " = " + str(answer))
		if (ranExpo == 5):
			answer = int(p1 % p2)
			print ("You generated this equation: ")
			print (str(p1) + " % " + str(p2) + " = " + str(answer))
		noMore = input("Press [ENTER] key to continue ")
noMore = input("Press [ENTER] key to exit")
# incomplete as of December 9th 2018 at 4:53 pm Pacific Time Zone
# I think this is pretty good, maybe some new ideas will come to mind - Sean Myrick on December 10th 2018 at 6:53 am Pacific Time Zone
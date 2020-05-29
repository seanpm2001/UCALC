		if calcIDSes == 17:
					print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
					print ("Temperature")
					fahOrCel = int(input("What do you want to start with? Fahrenheit (1) Celsius (2) "))
					if fahOrCel == 1:
						fahent = float(input("Enter the temperature in Fahrenheit: "))
					if fahOrCel == 2:
						celent = float(input("Enter the temperature in Celsius: "))
						fahent = (celent * 1.8 + 32)
						print ("The temperature in Fahrenheit is " + str(fahent))
					bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
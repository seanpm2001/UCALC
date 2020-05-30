calcIDSes = int(10)
if calcIDSes == 10:
	if calcIDSes == 10:
		if calcIDSes == 10:
			if calcIDSes == 10:
				if calcIDSes == 10:
					print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
					print ("Currency calculator")
					print ("Select a currency to get started")
					print ("$ - ID: 1")
					print ("¢ - ID: 2")
					print ("¥ - ID: 3")
					print ("£ - ID: 4")
					currencyID = int(input("Enter an ID (1-4): "))
					if (currencyID == 1 or 2 or 3 or 4):
						print ("Currency verified")
						currencystr = str
						if (currencyID == 1):
							currencystr == ("$")
							print ("Currency selected: $")
						if (currencyID == 2):
							currencystr == ("¢")
							print ("Currency selected: ¢")
						if (currencyID == 3):
							currencystr == ("¥")
							print ("Currency selected: ¥")
						if (currencyID == 4):
							currencystr == ("£")
							print ("Currency selected: £")
						print ("\n\n")
						currencycalc1 = float(input("Enter an amount: "))
						currencycalc2 = int(input("Select a calculation type:\n| + | ID = 1 | - | ID = 2 | * | ID = 3 | / | ID = 4 | % | ID = 5 | "))
						currencycalc3 = float(input("Enter second amount: "))
						if (currencycalc2 == 1 and currencyID == 1):
							currencytotal = float(currencycalc1 + currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "$")
						if (currencycalc2 == 1 and currencyID == 2):
							currencytotal = float(currencycalc1 + currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¢")
						if (currencycalc2 == 1 and currencyID == 3):
							currencytotal = float(currencycalc1 + currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¥")
						if (currencycalc2 == 1 and currencyID == 4):
							currencytotal = float(currencycalc1 + currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "£")
						if (currencycalc2 == 2 and currencyID == 1):
							currencytotal = float(currencycalc1 - currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "$")
						if (currencycalc2 == 2 and currencyID == 2):
							currencytotal = float(currencycalc1 - currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¢")
						if (currencycalc2 == 2 and currencyID == 3):
							currencytotal = float(currencycalc1 - currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¥")
						if (currencycalc2 == 2 and currencyID == 4):
							currencytotal = float(currencycalc1 - currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "£")
						if (currencycalc2 == 3 and currencyID == 1):
							currencytotal = float(currencycalc1 * currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "$")
						if (currencycalc2 == 3 and currencyID == 2):
							currencytotal = float(currencycalc1 * currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¢")
						if (currencycalc2 == 3 and currencyID == 3):
							currencytotal = float(currencycalc1 * currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¥")
						if (currencycalc2 == 3 and currencyID == 4):
							currencytotal = float(currencycalc1 * currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "£")
						if (currencycalc2 == 4 and currencyID == 1):
							currencytotal = float(currencycalc1 / currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "$")
						if (currencycalc2 == 4 and currencyID == 2):
							currencytotal = float(currencycalc1 / currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¢")
						if (currencycalc2 == 4 and currencyID == 3):
							currencytotal = float(currencycalc1 / currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¥")
						if (currencycalc2 == 4 and currencyID == 4):
							currencytotal = float(currencycalc1 / currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "£")
						if (currencycalc2 == 5 and currencyID == 1):
							currencytotal = float(currencycalc1 % currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "$")
						if (currencycalc2 == 5 and currencyID == 2):
							currencytotal = float(currencycalc1 % currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¢")
						if (currencycalc2 == 5 and currencyID == 3):
							currencytotal = float(currencycalc1 % currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "¥")
						if (currencycalc2 == 5 and currencyID == 4):
							currencytotal = float(currencycalc1 % currencycalc3)
							print ("The current amount is: " + str(currencytotal) + "£")
						bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
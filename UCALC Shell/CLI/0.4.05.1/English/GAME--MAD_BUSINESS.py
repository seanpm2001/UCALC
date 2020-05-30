print ("Mad Business game")
print ("\n\n\nNew game [1] ")
print ("\nResume game [unavailable] ")
mainMenuID = str(input("\n\n> "))
if (mainMenuID == "1"):
	print ("New game setup")
	print ("\nSelect a company type: ")
	print ("\nAgriculture")
	print ("Banking")
	print ("Car manufacturing")
	print ("Computer manufacturing")
	print ("Computer software")
	print ("Database management")
	print ("Fast food")
	print ("Hospital")
	print ("School")
	print ("Theme park")
	print ("Zoo")
	compType = str(input("Enter the type of company here: "))
	if (compType == "Agriculture" or compType == "agriculture" or compType == "AGRICULTURE"):
		custComp = str(input("Do you want to create a custom company? (Y/N): "))
		if (custComp == "Y" or custComp == "y"):
			print ("Preloaded company list: ")
			print ("\nWheat farm [1]")
			print ("Dairy farm [2]")
			custCompID = int(input("Enter an ID to continue: "))
			if (custCompID == 1):
				print ("Name your company: ")
				companyName = str(input(" "))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				wheatFieldBusLvl = float(1)
				while (startGame == 1):
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (" ")
					print ("Wheat fields [lvl " + str(wheatFieldBusLvl) + "] U1 [upgrade] S1 [sell]")
					actionCon1 = str(input("Enter an ID to continue: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						wheatFieldBusLvl = wheatFieldBusLvl + 1.0
						print ("You upgraded your wheat fields to level " + str(wheatFieldBusLvl) + "!")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S1" or actionCon1 == "s1"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						wheatFieldRev = float(wheatFieldBusLvl * 1.1)
						collect1 = float(wheatFieldRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					continue1 = input("Press [ENTER] key to continue")
			if (custCompID == 2):
				print ("Name your company: ")
				companyName = str(input(""))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				bBucks = float(0.0)
				dairyFarmLvl = int(0)
				dairyFarmXP = int(0)
				cowMilkBusLvl = float(1)
				goatMilkBusLvl = float(1)
				cheeseCakeBusLvl = float(1)
				creameryBusLvl = float(1)
				cheeseFactoryBusLvl = float(1)
				butterMillBusLvl = float(1)
				workerCount = int(1)
				dayCount = int(0)
				actionCount = int(0)
				xpCount = int(0)
				cowUpgradeCost = float(5.0)
				goatUpgradeCost = float(10.0)
				cheeseUpgradeCost = float(20.0)
				creamUpgradeCost = float(40.0)
				cheeseFUpgradeCost = float(80.0)
				butterUpgradeCost = float(160.0)
				dairyFarmLvlRequirement = int(100)
				while (startGame == 1):
					if (dairyFarmLvl == 0):
						dairyFarmLvlRequirement == 100
					if (dairyFarmLvl == 1):
						dairyFarmLvlRequirement == 1000
					if (dairyFarmLvl == 2):
						dairyFarmLvlRequirement == 10000
					if (dairyFarmLvl == 3):
						dairyFarmLvlRequirement == 100000
					if (dairyFarmLvl == 4):
						dairyFarmLvlRequirement == 1000000
					if (dairyFarmLvl == 5):
						dairyFarmLvlRequirement == 10000000
					if (dairyFarmLvl == 6):
						dairyFarmLvlRequirement == 100000000
					if (dairyFarmLvl == 7):
						dairyFarmLvlRequirement == 1000000000
					if (dairyFarmLvl == 8):
						dairyFarmLvlRequirement == 10000000000
					if (dairyFarmLvl == 9):
						dairyFarmLvlRequirement == 100000000000
					if (dairyFarmLvl == 10):
						dairyFarmLvlRequirement == 1000000000000
					if (dairyFarmLvl == 11):
						dairyFarmLvlRequirement == 10000000000000
					if (dairyFarmLvl == 12):
						dairyFarmLvlRequirement == 100000000000000
					if (xpCount == 100): # level 1
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 1")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 1000): # level 2
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 2")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 10000): # level 3
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 3")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 100000): # level 4
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 4")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 1000000): # level 5
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 5")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 10000000): # level 6
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 6")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 100000000): # level 7
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 7")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 1000000000): # level 8
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 8")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 10000000000): # level 9
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 9")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 100000000000): # level 10
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 10")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 1000000000000): # level 11
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 11")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (xpCount == 10000000000000): # level 12
						print ("L E V E L - U P ! ")	
						print ("==================")
						print ("Level 12")
						dairyFarmLvl = dairyFarmLvl + 1
						xpCount = xpCount + 1
					if (actionCount % 24 == 0): 
						dayCount = dayCount + 1
						actionCount = actionCount + 1
					if (dayCount % 30 == 0 and actionCount % 24 == 0 or actionCount % 25 == 0):
						print ("It's pay day! ")
						payDay = float(workerCount * 15.0)
						print (str(payDay) + str(curSymbol) + " has been given to your " + str(workerCount) + " workers!")
						moneyCount = moneyCount - payDay
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (str(bBucks) + " [-B-] " + " Level: " + str(dairyFarmLvl) + " " + str(xpCount) + "/" + str(dairyFarmLvlRequirement)) 
					print (str(actionCount) + " actions " + "Days: " + str(dayCount) + " Worker count: " + str(workerCount))
					print (" ")
					print ("Cow milk [lvl " + str(cowMilkBusLvl) + " ] U1 [upgrade " + str(cowUpgradeCost) + str(curSymbol) + " ] S1 [sell]")
					print ("\nGoat milk [lvl " + str(goatMilkBusLvl) + " ] U2 [upgrade " + str(goatUpgradeCost) + str(curSymbol) + " ] S2 [sell]")
					print ("\nCheesecake Factory [lvl " + str(cheeseCakeBusLvl) + " ] U3 [upgrade " + str(cheeseUpgradeCost) + str(curSymbol)  + " ] S3 [sell]")
					print ("\nCreamery [lvl " + str(creameryBusLvl) + " ] U4 [upgrade " + str(creamUpgradeCost) + str(curSymbol) + " ] S4 [sell]")
					print ("\nCheese factory [lvl " + str(cheeseFactoryBusLvl) + " ] U5 [upgrade " + str(cheeseFUpgradeCost) + str(curSymbol) + " ] S5 [sell]")
					print ("\nButter mill [lvl " + str(butterMillBusLvl) + " ] U6 [upgrade " + str(butterUpgradeCost) + str(curSymbol) + " ] S6 [sell]")
					actionCon1 = str(input("Enter an ID to start: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						if (moneyCount > cowUpgradeCost):
							moneyCount = moneyCount - cowUpgradeCost
							actionCount = actionCount + 1
							cowUpgradeCost = cowUpgradeCost * 2
							xpCount = xpCount + 10
							cowMilkBusLvl = cowMilkBusLvl + 1.0
							print ("You successfully upgraded your Cow Farm to level " + str(cowMilkBusLvl))
							print ("You upgraded your cow milk to level " + str(cowMilkBusLvl) + "!")
						if (moneyCount < cowUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S1" or actionCon1 == "s1"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						cowMilkRev = float(cowMilkBusLvl * 1.1)
						collect1 = float(cowMilkRev)
						xpCount = xpCount + 10
						actionCount = actionCount + 1
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "U2" or actionCon1 == "u2"):
						if (moneyCount > goatUpgradeCost):
							moneyCount = moneyCount - goatUpgradeCost
							actionCount = actionCount + 1
							goatUpgradeCost = goatUpgradeCost * 1.8
							goatMilkBusLvl = goatMilkBusLvl + 1.0
							print ("You upgraded your goat milk to level " + str(goatMilkBusLvl) + "!")
						if (moneyCount < goatUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S2" or actionCon1 == "s2"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						goatMilkRev = float(goatMilkBusLvl * 1.25)
						actionCount = actionCount + 1
						collect1 = float(goatMilkRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "U3" or actionCon1 == "u3"):
						if (moneyCount > cheeseUpgradeCost):
							moneyCount = moneyCount - cheeseUpgradeCost
							actionCount = actionCount + 1
							cheeseUpgradeCost = cheeseUpgradeCost * 1.5
							cheeseCakeBusLvl = cheeseCakeBusLvl + 1.0
							print ("You upgraded your Cheesecake factory to level " + str(cheeseCakeBusLvl) + "!")
						if (moneyCount < cheeseUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S3" or actionCon1 == "s3"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						cheeseCakeRev = float(cheeseCakeBusLvl * 2)
						collect1 = float(cheeseCakeRev)
						actionCount = actionCount + 1
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "U4" or actionCon1 == "u4"):
						if (moneyCount > creamUpgradeCost):
							moneyCount = moneyCount - creamUpgradeCost
							actionCount = actionCount + 1
							creamUpgradeCost = creamUpgradeCost * 3
							creameryBusLvl = creameryBusLvl + 1.0
							print ("You upgraded your creamery to level " + str(creameryBusLvl) + "!")
						if (moneyCount < creamUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S4" or actionCon1 == "s4"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						creameryRev = float(creameryBusLvl * 2.5)
						actionCount = actionCount + 1
						collect1 = float(creameryRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "U5" or actionCon1 == "u5"):
						if (moneyCount > cheeseFUpgradeCost):
							moneyCount = moneyCount - cheeseFUpgradeCost
							actionCount = actionCount + 1
							cheeseFUpgradeCost = cheeseFUpgradeCost * 2.8
							cheeseFactoryBusLvl = cheeseFactoryBusLvl + 1.0
							print ("You upgraded your cheese factory to level " + str(cheeseFactoryBusLvl) + "!")
						if (moneyCount < cheeseFUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S5" or actionCon1 == "s5"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						cheeseFactoryRev = float(cheeseFactoryBusLvl * 5.0)
						actionCount = actionCount + 1
						collect1 = float(cheeseFactoryRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "U6" or actionCon1 == "u6"):
						if (moneyCount > butterUpgradeCost):
							moneyCount = moneyCount - butterUpgradeCost
							actionCount = actionCount + 1
							butterUpgradeCost = butterUpgradeCost * 2.5
							butterMillBusLvl = butterMillBusLvl + 1.0
							print ("You upgraded your butter mill to level " + str(butterMillBusLvl) + "!")
						if (moneyCount < butterUpgradeCost):
							print ("You do not have enough money to perform this upgrade")
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					if (actionCon1 == "S6" or actionCon1 == "s6"): # this whole time, the error was that S1 wasn't "S1" # I am so disappointed in myself
						butterMillRev = float(butterMillBusLvl * 10.0)
						actionCount = actionCount + 1
						collect1 = butterMillRev
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
						print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					# continue1 = input("Press [ENTER] key to continue")
	if (compType == "Banking" or compType == "banking" or compType == "BANKING"):
		custComp = str(input("Do you want to create a custom company? (Y/N): "))
		if (custComp == "Y"):
			print ("Preloaded company list: ")
			print ("Bank [1]")
			print ("Vault [2]")
			custCompID = int(input("Enter an ID to continue: "))
			if (custCompID == 1):
				print ("Name your company: ")
				companyName = str(input(" "))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				while (startGame == 1):
					wheatFieldBusLvl = float(1)
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (" ")
					print ("Deposit Tax [lvl " + str(wheatFieldBusLvl) + "] U1 [upgrade] S1 [sell]")
					actionCon1 = str(input("Enter an ID to continue: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						wheatFieldBusLvl = wheatFieldBusLvl + 1.0
						print ("You upgraded your wheat fields to level " + str(wheatFieldBusLvl) + "!")
					if (actionCon1 == "S1" or actionCon1 == "s1"):
						wheatFieldRev = float(wheatFieldBusLvl * 1.1)
						collect1 = float(wheatFieldRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
					continue1 = input("Press [ENTER] key to continue")
		if (custComp == "N"):
			print ("Custom company mode de-activated")
			print ("=================================")
			print ("\nSelect a pre-loaded company to start: ")
			print ("\nBanner Bank [1]")
			print ("Bank of America [2]")
			print ("Wells fargo [3]")
			selectBusID = int(input("> "))
			if selectBusID == 1:
				employeeCount = int(4)
				print ("Banner Bank setup")
				print ("Employee count: " + str(employeeCount))
	if (compType == "Car manufacturing" or compType == "car manufacturing" or compType == "CAR MANUFACTURING"):
		custComp = str(input("Do you want to create a custom company? (Y/N): "))
		if (custComp == "Y"):
			print ("Preloaded company list: ")
			print ("Car dealer [1]")
			print ("Car factory [2]")
			custCompID = int(input("Enter an ID to continue: "))
			if (custCompID == 1):
				print ("Name your company: ")
				companyName = str(input(" "))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				while (startGame == 1):
					wheatFieldBusLvl = float(1)
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (" ")
					print ("Wheat fields [lvl " + str(wheatFieldBusLvl) + "] U1 [upgrade] S1 [sell]")
					actionCon1 = str(input("Enter an ID to continue: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						wheatFieldBusLvl = wheatFieldBusLvl + 1.0
						print ("You upgraded your wheat fields to level " + str(wheatFieldBusLvl) + "!")
					if (actionCon1 == "S1" or actionCon1 == "s1"):
						wheatFieldRev = float(wheatFieldBusLvl * 1.1)
						collect1 = float(wheatFieldRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
					continue1 = input("Press [ENTER] key to continue")
		if (custComp == "N"):
			print ("Custom company mode de-activated")
			print ("=================================")
			print ("\nSelect a pre-loaded company to start: ")
			print ("\nSubaru [1]")
			print ("Tesla [2]")
			print ("Mazda [3]")
			selectBusID = int(input("> "))
			if selectBusID == 1:
				employeeCount = int(12)
				print ("Subaru Setup")
				print ("Employee count: " + str(employeeCount))
	if (compType == "Computer manufacturing" or compType == "computer manufacturing" or compType == "COMPUTER MANUFACTURING"):
		custComp = str(input("Do you want to create a custom company? (Y/N): "))
		if (custComp == "Y"):
			print ("Preloaded company list: ")
			print ("Laptop factory [1]")
			print ("Desktop factory [2]")
			print ("Hard-drive factory [3]")
			print ("Phone factory [4]")
			print ("Console factory [5]")
			print ("Processor factory [6]")
			custCompID = int(input("Enter an ID to continue: "))
			if (custCompID == 1):
				print ("Name your company: ")
				companyName = str(input(" "))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				while (startGame == 1):
					wheatFieldBusLvl = float(1)
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (" ")
					print ("Wheat fields [lvl " + str(wheatFieldBusLvl) + "] U1 [upgrade] S1 [sell]")
					actionCon1 = str(input("Enter an ID to continue: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						wheatFieldBusLvl = wheatFieldBusLvl + 1.0
						print ("You upgraded your wheat fields to level " + str(wheatFieldBusLvl) + "!")
					if (actionCon1 == "S1" or actionCon1 == "s1"):
						wheatFieldRev = float(wheatFieldBusLvl * 1.1)
						collect1 = float(wheatFieldRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
					continue1 = input("Press [ENTER] key to continue")
		if (custComp == "N"):
			print ("Custom company mode de-activated")
			print ("=================================")
			print ("\nSelect a pre-loaded company to start: ")
			print ("\nAcer[1]")
			print ("Dell [2]")
			print ("Lenovo [3]")
			print ("Gateway [4]")
			print ("Toshiba [5]")
			selectBusID = int(input("> "))
			if selectBusID == 1:
				employeeCount = int(12)
				print ("Acer setup")
				print ("Employee count: " + str(employeeCount))
	if (compType == "Computer software" or compType == "computer software" or compType == "COMPUTER SOFTWARE"):
		custComp = str(input("Do you want to create a custom company? (Y/N): "))
		if (custComp == "Y"):
			print ("Preloaded company list: ")
			print ("Laptop factory [1]")
			print ("Desktop factory [2]")
			print ("Hard-drive factory [3]")
			print ("Phone factory [4]")
			print ("Console factory [5]")
			print ("Processor factory [6]")
			custCompID = int(input("Enter an ID to continue: "))
			if (custCompID == 1):
				print ("Name your company: ")
				companyName = str(input(" "))
				print ("How much money do you want to start with? ")
				moneyCount = float(input("- "))
				print ("What type of currency do you wish to use? ")
				print ("$ [1] ")
				print ("¢ [2] ")
				print ("¥ [3] ")
				print ("£ [4] ")
				print ("₱ [5] ")
				print ("₰ [6] ")
				print ("₹ [7] ")
				print ("€ [8] ")
				print ("₩ [9] ")
				curID = int(input("Enter an ID to start: "))
				if (curID == 1):
					curSymbol = str("$")
				if (curID == 2):
					curSymbol = str("¢")
				if (curID == 3):
					curSymbol = str("¥")
				if (curID == 4):
					curSymbol = str("£")
				if (curID == 5):
					curSymbol = str("₱")
				if (curID == 6):
					curSymbol = str("₰")
				if (curID == 7):
					curSymbol = str("₹")
				if (curID == 8):
					curSymbol = str("€")
				if (curID == 9):
					curSymbol = str("₩")
				print ("Let's get started")
				startGame = int(1)
				while (startGame == 1):
					wheatFieldBusLvl = float(1)
					print (str(companyName) + " | " + str(moneyCount) + " " + str(curSymbol))
					print (" ")
					print ("Wheat fields [lvl " + str(wheatFieldBusLvl) + "] U1 [upgrade] S1 [sell]")
					actionCon1 = str(input("Enter an ID to continue: "))
					if (actionCon1 == "U1" or actionCon1 == "u1"):
						wheatFieldBusLvl = wheatFieldBusLvl + 1.0
						print ("You upgraded your wheat fields to level " + str(wheatFieldBusLvl) + "!")
					if (actionCon1 == S1 or actionCon1 == "s1"):
						wheatFieldRev = float(wheatFieldBusLvl * 1.1)
						collect1 = float(wheatFieldRev)
						print ("You collected " + str(collect1) + "" + str(curSymbol) + "!")
						moneyCount = moneyCount + collect1
					continue1 = input("Press [ENTER] key to continue")
		if (custComp == "N"):
			print ("Custom company mode de-activated")
			print ("=================================")
			print ("\nSelect a pre-loaded company to start: ")
			print ("\nMicrosoft [1]")
			print ("Canonical [2]")
			print ("Apple [3]")
			print ("Adobe [4]")
			print ("Videolan [5]")
			selectBusID = int(input("> "))
			if selectBusID == 1:
				employeeCount = int(12)
				print ("Acer setup")
				print ("Employee count: " + str(employeeCount))
noMore = input("Press [ENTER] key to quit")
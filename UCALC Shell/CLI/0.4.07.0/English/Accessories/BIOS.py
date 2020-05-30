modID = str("UNKNOWN")
konlop = str("1")
adminusr = str("ADMIN")
adminpas = str("Password")
biospar = str("B3")
if (biospar == "B3"):
	if (biospar == "B3"):
		bioloop = int(0)
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		while (bioloop == 0):
			print ("====================================================================================>")
			print ("UCALC System Basic Input Output System")
			print ("Model ID: " + str(modID) + "\t\tLoop ID: " + str(konlop))
			print ("Administrator username: " + str(adminusr) + "\nType 'ADMU' to modify")
			print ("Administrator password: " + str(adminpas) + "\nType 'ADMP' to modify")	
			modibio = str(input("Enter a modification code\nType Q to exit: "))
			if (modibio == "ADMU"):
				print ("Administrator account")
				adminusr = str(input("Rename the administrator: "))
			if (modibio == "ADMP"):
				print ("Administrator password")
				adminpas = str(input("Change the password: "))
			if (modibio == "Q"):
				(bioloop == 1)
				if (bioloop == 1):
					if (bioloop == 1):
						print ("Cannot exit BIOS, Looping Error\nSorry :|")
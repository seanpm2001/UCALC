print ("Setup demo")
more1 = input("Press [ENTER] key to continue")
print ("Language ")
print ("English (1)")
print ("Spanish (2) (unavailable)")
print ("French (3) (unavailable")
languageID = str(input(">> "))
if (languageID == "1"):
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print ("Welcome to the Ultimate calculator all-in-one edition setup wizard! ")
	print ("\nThis wizard will help you through the installation of UCALC")
	print ("\n\n\n\n\n")
	start1 = input("Press [ENTER] key to begin")
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print (" ")
	print ("System requirement checking ")
	print ("\n\n\n1080 Megabytes (disk)")
	print ("100 Megabytes (processor)")
	print ("64 Megabytes (Random Access Memory)")
	print ("\n\n\nYour system is compatible with UCALC All-in-one edition!")
	start2 = input("Press [ENTER] key to continue")
	loopStep = int(1)
	while (loopStep == 1):
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print ("Feature select")
		print ("Select features you want: ")
		print ("\n[ABOUTPAGES] (1)")
		print ("[Accessories] (2)")
		print ("[Account] (3)")
		print ("[Chatbots] (4)")
		print ("[Old clients] (5)")
		print ("[Converters] (6)")
		print ("[Documentation] (7)")
		print ("[External links] (8)")
		print ("[Games] (9)")
		print ("[Historical calculators] (10)")
		print ("[Modes] (11)")
		print ("[Political] (12)")
		print ("[Primitive Calculators] (13)")
		print ("[PTOE Project] (14)")
		print ("[Research] (15)")
		print ("[Setup] (16)")
		print ("[Teacher Features] (17)")
		print ("[Quit] (18)")
		featureID = str(input("Enter an ID to continue, enter as many features as you want, then enter 18 to continue"))
		if (featureID == "1"):
			print ("Imported the [ABOUTPAGES] module to your installation")
		if (featureID == "18"):
			loopStep == loopStep + 1
		
noMore = input("Press [ENTER] key to quit")
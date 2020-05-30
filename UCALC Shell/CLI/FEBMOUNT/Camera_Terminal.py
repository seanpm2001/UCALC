# start of script
print ("UCALC Camera Terminal")
print ("=====================")
print ("Welcome to the camera terminal! Here, you can modify camera settings before you go into real-world solve mode")
print ("For help, type ./help")
loop1 = int(1)
while (loop1 == 1): # start of the loop
	term1con = str(input("UCALC>>"))
	if (term1con == "./help"):
		print ("Camera termina help")
		print ("./font")
		print ("./type")
		print ("./library")
		print ("./help")
		print ("./launch")
		print ("./quit")
		print ("./resolution")
		print ("./color")
		print ("./limit")
		print ("./rules")
		print ("Tip: Remember to clean your camera for accuracy when taking pictures")
	if (term1con == "./font"):
		print ("Font settings")
		print ("Auto detect [ID: AD]")
		print ("Agency FB [ID: A01]")
		print ("Arial [ID: A02]")
		print ("Arial Black [ID: A03]")
		print ("Bell MT [ID: A04]")
		print ("Broadway [ID: A05]")
		print ("Calibri [ID: A06]")
		print ("Cambria [ID: A07]")
		print ("Comic Sans MS [ID: A08]")
		print ("Consolas [ID: A09]")
		print ("Corbel [ID: A10]")
		print ("Courier [ID: A11]")
		print ("Courier new [ID: A12]")
		print ("Elephant [ID: A13]")
		print ("Impact [ID: A14]")
		print ("lucidia console [ID: A15]")
		print ("Minion Pro [ID: A16]")
		print ("System [ID: A17]")
		print ("Trebuchet MS [ID: A18]")
		print ("Vladimir script [ID: A19]")
		print ("Type an ID to continue")
		fontIDCon = str(input("FONT>>"))
		if (fontIDCon == "AD"):
			print ("You have enabled auto-detect")
			print ("This feature is in beta and may be inaccurate")
			enterNext = input("Press [ENTER] key to continue")
	if (term1con == "./type"):
		print ("Type of equations: ")
		print ("Addition [ID: 1]")
		print ("Subtraction [ID: 2]")
		print ("Multiplication [ID: 3]")
		print ("Division [ID: 4]")
		print ("Modular division [ID: 5]")
		print ("Powers [ID: 6]")
		print ("Type an ID to continue: ")
		mathTypeCon = str(input("TYPE>>"))
	if (term1con == "./library"):
		print ("Librayr settings")
		print ("Cancel [ID: 0]")
		print ("Save original image to gallery [ID: 1]")
		print ("Don't save original image to gallery [ID: 2]")
		print ("Save answered image to gallery [ID: 3]")
		print ("Don't save answered image to gallery [ID: 4]")
		print ("Save original images as JPG [ID: 5]")
		print ("Save original images as PNG [ID: 6]")
		print ("Save original images as HEIF [ID: 7]")
		print ("Save original images as GIF [ID: 8]")
		print ("Save original images as TIF [ID: 9]")
		print ("Save original images as BMP [ID: 10]")
		print ("Save answered images as JPG [ID: 11]")
		print ("Save answered images as PNG [ID: 12]")
		print ("Save answered images as HEIF [ID: 13]")
		print ("Save answered images as GIF [ID: 14]")
		print ("Save answered images as TIF [ID: 15]")
		print ("Save answered images as BMP [ID: 16]")
		print ("Type an ID to continue: ")
		libSettCon = str(input("LIB>>"))
		if (libSettCon == "0"):
			print ("Operation cancelled")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "1"):
			print ("Original images will now be saved to the gallery")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "2"):
			print ("Original images will now not be saved to the gallery")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "3"):
			print ("Answered images will now be saved to the gallery")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "4"):
			print ("Answered images will now not be saved to the gallery")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "5"):
			print ("Original images will now be saved as JPG files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "6"):
			print ("Original images will now be saved as PNG files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "7"):
			print ("Original images will now be saved as HEIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "8"):
			print ("Original images will now be saved as GIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "9"):
			print ("Original images will now be saved as TIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "10"):
			print ("Original images will now be saved as BMP files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "11"):
			print ("Answered images will now be saved as JPG files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "12"):
			print ("Answered images will now be saved as PNG files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "13"):
			print ("Answered images will now be saved as HEIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "14"):
			print ("Answered images will now be saved as GIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "15"):
			print ("Answered images will now be saved as TIF files")
			enterNext = input("Press [ENTER] key to continue")
		if (libSettCon == "16"):
			print ("Answered images will now be saved as BMP files")
			enterNext = input("Press [ENTER] key to continue")
	if (term1con == "./launch"):
		print ("Launching real-world solve mode...")
	if (term1con == "./quit"):
		print ("Confirm going back to the main calculator by typing Y")
		quit1 = str(input("Quit? (Y/N):"))
		if (quit1 == "Y" or quit1 == "y"):
			print ("Exiting... please wait (Press [ENTER] key to exit immediately)")
			loop1 += 1
	if (term1con == "./resolution"): # start of resolution list
		print ("Resolution setup")
		print ("Specify the resolution of the camera")
		print ("1280x720")
		print ("1336x730")
		print ("1400x720")
		print ("1450x800")
		print ("1600x720")
		print ("1920x1080")
		print ("2400x1080")
		print ("2560x1440")
		print ("3200x1440")
		print ("3840x2160")
		print ("Enter an ID to continue (the resolution is the ID)") # end of resolution list
		resCon1 = str(input("ID>>")) # beginning of resolution loop
		if (resCon1 == "1280x720"):
			print ("Your camera resolution for UCALC was set to 1280x720")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "1336x730"):
			print ("Your camera resolution for UCALC was set to 1336x730")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "1400x720"):
			print ("Your camera resolution for UCALC was set to 1400x720")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "1450x800"):
			print ("Your camera resolution for UCALC was set to 1450x800")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "1600x720"):
			print ("Your camera resolution for UCALC was set to 1600x720")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "1920x1080"):
			print ("Your camera resolution for UCALC was set to 1920x1080")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "2400x1080"):
			print ("Your camera resolution for UCALC was set to 2400x1080")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "2560xx1440"):
			print ("Your camera resolution for UCALC was set to 2560x1440")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "3200x1440"):
			print ("Your camera resolution for UCALC was set to 3200x1440")
			enterNext = input("Press [ENTER] key to continue")
		if (resCon1 == "3840x2160"):
			print ("Your camera resolution for UCALC was set to 3840x2160")
			enterNext = input("Press [ENTER] key to continue")
			# end of resolution loop
	if (term1con == "./color"):
		print ("Color settings")
		print ("Modify answer colors")
		print ("Select a color by typing its name")
		print ("Black")
		print ("White")
		print ("Silver")
		print ("Cyan")
		print ("Light green")
		print ("Dark green")
		print ("Light red")
		print ("Dark red")
		print ("Yellow")
		print ("Orange")
		print ("Magenta")
		print ("Gold")
		print ("Bronze")
		print ("Brown")
		print ("Pink")
		colorName1 = str(input("COLOR>>")) # beginning of color loop
		if (colorName1 == "black" or colorName1 == "Black" or colorName1 == "BLACK"): # Color 1
			print ("Answer font color changed to Black")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "white" or colorName1 == "White" or colorName1 == "WHITE"): # Color 2
			print ("Answer font color changed to white")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "silver" or colorName1 == "Silver" or colorName1 == "SILVER"): # Color 3
			print ("Answer font color changed to Silver")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "cyan" or colorName1 == "Cyan" or colorName1 == "CYAN"): # Color 4
			print ("Answer font color changed to Cyan")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "light green" or colorName1 == "Light green" or colorName1 == "Light Green" or colorName1 == "LIGHT GREEN"): # Color 5
			print ("Answer font color changed to Light Green")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "dark green" or colorName1 == "Dark green" or colorName1 == "Dark Green" or colorName1 == "DARK GREEN"): # Color 6
			print ("Answer font color changed to Dark Green")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "light red" or colorName1 == "Light red" or colorName1 == "Light Red" or colorName1 == "LIGHT RED"): # Color 7
			print ("Answer font color changed to Light Red")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "dark red" or colorName1 == "Dark red" or colorName1 == "Dark Red" or colorName1 == "DARK RED"): # Color 8
			print ("Answer font color changed to Dark Red")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "yellow" or colorName1 == "Yellow" or colorName1 == "YELLOW"): # Color 9
			print ("Answer font color changed to Yellow")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "orange" or colorName1 == "Orange" or colorName1 == "ORANGE"): # Color 10
			print ("Answer font color changed to Orange")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "magenta" or colorName1 == "Magenta" or colorName1 == "MAGENTA"): # Color 11
			print ("Answer font color changed to Magenta")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "gold" or colorName1 == "Gold" or colorName1 == "GOLD"): # Color 12
			print ("Answer font color changed to Gold")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "bronze" or colorName1 == "Bronze" or colorName1 == "BRONZE"): # Color 13
			print ("Answer font color changed to Bronze")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "brown" or colorName1 == "Brown" or colorName1 == "BROWN"): # Color 14
			print ("Answer font color changed to Brown")
			enterNext = input("Press [ENTER] key to continue")
		if (colorName1 == "pink" or colorName1 == "Pink" or colorName1 == "PINK"): # Color 15
			print ("Answer font color changed to Brown")
			enterNext = input("Press [ENTER] key to continue")
		# end of color loop
	if (term1con == "./limit"):
		print ("Set limits")
		print ("==================================================")
		print ("Maximum picture folder size settings [ID: 1]")
		print ("Maximum picture count [ID: 2]")
		print ("Daily uses [ID: 3]")
		print ("==================================================")
		print ("Enter an ID to continue setting limits")
		limID = str(input("LIMID>>")) # start of limit loop
		if (limID == "1"):
			print ("Picture folder size limits")
			print ("\nFolder location [Windows] C://Windows//Program Files//UCALC//Storage//RealTime//Pictures//Answers")
			print ("\nFolder location [MacOS] Unknown")
			print ("\nFolder location [Android] storage://UCALC")
			print ("==============================")
			print ("Until space runs out [ID: 0]")
			print ("10 Megabytes [ID: 1]")
			print ("15 Megabytes [ID: 2]")
			print ("20 Megabytes [ID: 3]")
			print ("25 Megabytes [ID: 4]")
			print ("30 Megabytes [ID: 5]")
			print ("40 Megabytes [ID: 6]")
			print ("50 Megabytes [ID: 7]")
			print ("60 Megabytes [ID: 8]")
			print ("75 Megabytes [ID: 9]")
			print ("80 Megabytes [ID: 10]")
			print ("90 Megabytes [ID: 11]")
			print ("95 Megabytes [ID: 12]")
			print ("100 Megabytes [ID: 13]")
			print ("110 Megabytes [ID; 14]")
			print ("120 Megabytes [ID: 15]")
			print ("125 Megabytes [ID: 16]")
			print ("130 Megabytes [ID: 17]")
			print ("140 Megabytes [ID: 18]")
			print ("150 Megabytes [ID: 19]")
			print ("Enter an ID to continue: ")
			limitMBID = str(input("MBID>>")) # start of size limit loop
			if (limitMBID == "0"):
				print ("Limit set to \"Until memory runs out\"!")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "1"):
				print ("Limit set to 10 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "2"):
				print ("Limit set to 15 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "3"):
				print ("Limit set to 20 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "4"):
				print ("Limit set to 25 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "5"):
				print ("Limit set to 30 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "6"):
				print ("Limit set to 40 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "7"):
				print ("Limit set to 50 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "8"):
				print ("Limit set to 60 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "9"):
				print ("Limit set to 75 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "10"):
				print ("Limit set to 80 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "11"):
				print ("Limit set to 90 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "12"):
				print ("Limit set to 95 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "13"):
				print ("Limit set to 100 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "14"):
				print ("Limit set to 110 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "15"):
				print ("Limit set to 120 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "16"):
				print ("Limit set to 125 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "17"):
				print ("Limit set to 130 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "18"):
				print ("Limit set to 140 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			if (limitMBID == "19"):
				print ("Limit set to 150 Megabytes")
				enterNext = input("Press [ENTER] key to continue")
			# end of size limit loop
		if (limID == "2"):
			print ("Set a picture count loop")
			print ("Type A to remove the limit")
			answerPicCountLimit = int(input("Answered picture limit: "))
			originalPicCountLimit = int(input("Original picture limit: "))
			overRide = str(input("Type A to remove limits"))
			if (overRide == "a" or overRide == "A"):
				answerPicCountLimit = int(999999999999)
				print ("Answered picture limit removed")
				originalPicCountLimit = int(999999999999)
				print ("Origonal picture limit removed")
			enterNext = input("Press [ENTER] key to continue")
		if (limID == "3"):
			print ("Daily use limit")
			yN = str(input("Do you want to set a daily usage limit? (Y/N)"))
			if (yN == "Y" or yN == "y"):
				picDayLimit = int(input("Set a daily limit: "))
				print ("Daily limit set to: " + str(picDayLimit))
			if (yN == "N" or yN == "n"):
				print ("Do you want to remove the limit?")
				remLim = str(input("(Y/N):"))
				if (remLim == "y" or remLim == "Y"):
				picDayLimit = int(99999999999999999999)
					print ("Limit removed")
				if (remLim == "n" or remLim == "N"):
					print ("Operation aborted")
			enterNext = input("Press [ENTER] key to continue")
	if (term1con == "./rules"):
		print ("Rules")
		print ("With great power comes great responsibility")
		print ("========================")
		print ("DO NOT USE THIS TO CHEAT")
		print ("This is a tool for personal work. This shouldn't be used to skip your way through math class. Math is very important in society, and you really should learn it, as it has to be used every day")
		print ("========================")
		print ("End of rule listing")
# end of the loop
noMore = input("Press [ENTER] key to quit")
# end of script
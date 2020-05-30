# start of script
print ("UCALC Camera Terminal")
print ("=====================")
print ("Welcome to the camera terminal! Here, you can modify camera settings before you go into real-world solve mode")
print ("For help, type ./help")
loop1 = int(1)
while (loop1 == 1):
	term1con = str(input("UCALC>>"))
	if (term1con == "./help"):
		print ("Camera termina help")
		print ("./font")
		print ("./type")
		print ("./library")
		print ("./help")
		print ("./launch")
		print ("./quit")
		print ("Tip: Remember to clean your camera for accuracy")
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
		if (libSettCon == "1"):
			print ("Original images will now be saved to the gallery")
		if (libSettCon == "2"):
			print ("Original images will now not be saved to the gallery")
		if (libSettCon == "3"):
			print ("Answered images will now be saved to the gallery")
		if (libSettCon == "4"):
			print ("Answered images will now not be saved to the gallery")
		if (libSettCon == "5"):
			print ("Original images will now be saved as JPG files")
		if (libSettCon == "6"):
			print ("Original images will now be saved as PNG files")
		if (libSettCon == "7"):
			print ("Original images will now be saved as HEIF files")
		if (libSettCon == "8"):
			print ("Original images will now be saved as GIF files")
		if (libSettCon == "9"):
			print ("Original images will now be saved as TIF files")
		if (libSettCon == "10"):
			print ("Original images will now be saved as BMP files")
		if (libSettCon == "11"):
			print ("Answered images will now be saved as JPG files")
		if (libSettCon == "12"):
			print ("Answered images will now be saved as PNG files")
		if (libSettCon == "13"):
			print ("Answered images will now be saved as HEIF files")
		if (libSettCon == "14"):
			print ("Answered images will now be saved as GIF files")
		if (libSettCon == "15"):
			print ("Answered images will now be saved as TIF files")
		if (libSettCon == "16"):
			print ("Answered images will now be saved as BMP files")
	if (term1con == "./launch"):
		print ("Launching real-world solve mode...")
	if (term1con == "./quit"):
		print ("Confirm going back to the main calculator by typing Y")
		quit1 = str(input("Quit? (Y/N):"))
		if (quit1 == "Y" or quit1 == "y"):
			print ("Exiting... please wait (Press [ENTER] key to exit immediately)")
			loop1 += 1
noMore = input("Press [ENTER] key to quit")
# end of script
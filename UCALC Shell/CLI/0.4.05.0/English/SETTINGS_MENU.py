adminPassword = str("Admin")
adminUsername = str("Username")
print (" ")
print (" ")
print (" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------. ")
print ("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
print ("| |    _______   | || |  _________   | || |  _________   | || |  _________   | || |     _____    | || | ____  _____  | || |    ______    | || |    _______   | |")
print ("| |   /  ___  |  | || | |_   ___  |  | || | |  _   _  |  | || | |  _   _  |  | || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | || |   /  ___  |  | |")
print ("| |  |  (__ \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | || | |_/ | | \_|  | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | || |  |  (__ \_|  | |")
print ("| |   '.___`-.   | || |   |  _|  _   | || |     | |      | || |     | |      | || |      | |     | || |  | |\ \| |   | || | | |    ____  | || |   '.___`-.   | |")
print ("| |  |`\____) |  | || |  _| |___/ |  | || |    _| |_     | || |    _| |_     | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | || |  |`\____) |  | |")
print ("| |  |_______.'  | || | |_________|  | || |   |_____|    | || |   |_____|    | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | || |  |_______.'  | |")
print ("| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
print ("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
print (" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
print (" ")
enterToEnter = input("Press [ENTER] key to start")
uCMainConsole = int(9)
if uCMainConsole == 9:
	if uCMainConsole == 9:	
		print ("UCalc settings")
		print ("\n[Display]       {ID: 1} ")
		print ("\n[Users]         {ID: 2} ")
		print ("\n[Administrator] {ID: 3} ")
		print ("\n[EXIT SETTINGS] {ID: 0}")
		settingsMainMenuCon = str(input("Enter an ID to continue >> "))
		if (settingsMainMenuCon == "1"):
			print ("Display settings")
			print ("\n[Font]                  {ID: 1}")
			print ("\n[Resolution]            {ID: 2}")
			print ("\n[Color type]            {ID: 3}")
			print ("\n[Text color]            {ID: 4}")
			print ("\n[EXIT DISPLAY SETTINGS] {ID: 0}")
			displaySettingsCon = str(input("Enter an ID to continue >> "))
			if (displaySettingsCon == "1"):
				loop1 = int(1)
				while loop1 == 1:
					print ("==============")
					print ("Font\n")
					print ("Calibri (body)")
					print ("Calibri (light)")
					print ("Courier (new)")
					print ("Comic Sans MS")
					print ("Scratch:")
					print ("==============")
					more1 = input("Press [ENTER] key to continue")
			if (displaySettingsCon == "2"):
				loop1 = int(1)
				while loop1 == 1:
					print ("==============")
					print ("Resolution\n")
					print ("Expandable ")
					print ("1280x720")
					print ("1700x800")
					print ("1920x1080")
					print ("2560x1080")
					print ("2560x1440")
					print ("3840x1440")
					print ("3840x2160")
					print ("==============")
					more1 = input("Press [ENTER] key to continue")
			if (displaySettingsCon == "3"):
				loop1 = int(1)
				while loop1 == 1:
					print ("===============")
					print ("Color type\n")
					print ("MONOCHROME (2 color) ")
					print ("16 color")
					print ("8 bit")
					print ("16 bit ")
					print ("24 bit ")
					print ("32 bit")
					print ("===============")
					more1 = input("Press [ENTER] key to continue")
			if (displaySettingsCon == "4"):
				loop1 = int(1)
				while loop1 == 1:
					print ("===============")
					print ("Text color\n")
					print ("Background: [Black]")
					print ("[White] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
					print ("Main text: [White]")
					print ("[Black] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
					print ("Answer text: [White]")
					print ("[Black] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
					print ("=============")
					more1 = input("Press [ENTER] key to continue")
		if (settingsMainMenuCon == "2"):
			print ("User settings")
			print ("\nAdd a user           {ID: 1}")
			print ("\nRemove a user        {ID: 2}")
			print ("\nPromote/demote user  {ID: 3}")
			print ("\nModify a user        {ID: 4}")
			print ("\nExit user settings   {ID: 5}")
			displaySettingsCon = str(input("Enter an ID to continue >> "))
			if (displaySettingsCon == "1"):
				print ("This setting required administrator access to edit/modify")
				entAdminUser = str(input("Enter an admin username: "))
				if (entAdminUser == adminUsername):
					entAdminPass ("Enter the password for " + str(adminUsername) + ": ")
				else:
					print ("Invalid username entered! Quitting...")
				if (entAdminPass == adminPassword):
					more1 = input("Successfully logged in as an administrator! ")
					print ("Add a new user wizard")
					print ("\nThis will guide you through the process of creating a new user")
					print ("\n\n\n")
					newUserName = str(input("Enter a username: "))
					newPassword = str(input("Enter a password: "))
				else:
					print ("Invalid password entered! Quitting...")
			if (displaySettingsCon == "2"):
				print ("Remove a user")
				print ("\n\n\n")
			if (displaySettingsCon == "0"):
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				loopf = int(2)
				while loopf == 2:
					print ("Failed to exit settings menu. Press [ENTER] to retry")
		if (settingsMainMenuCon == "2"):
			print ("Administrator settings")
			# insert admin confirmation here
			print ("\n\nAdmin settings")
			print ("\n[Add/block programs] {ID: 1}")
			print ("\n[Exit]               {ID: 0}")
			displaySettingsCon = str(input("Enter an ID to continue >> "))
			if (displaySettingsCon == "1"):
				print ("Add/block programs and features")
				print ("\n\nGames")
				print ("\n ")
				print ("\n\nDocumentation")
				print ("\n ")
				print ("\n\nModes")
				print ("\n ")
		if (settingsMainCon == "2"):
			print ("Internal error")
		if (settingsMainCon == "0"):
			loop1 = int(1)
			while loop1 == 1:
				noMore = input("Press [ENTER] key to quit")
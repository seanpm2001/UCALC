uCMainConsole = int(10)
if uCMainConsole == 10:
	if uCMainConsole == 10:
		print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
		print ("▓ U P D A T E | M A N A G E R                                 ▓")
		print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
		print ("▓ Check for updates online                           [ID: 01] ▓")
		print ("▓ Install update packages                            [ID: 02] ▓")
		print ("▓ Install updates individually                       [ID: 03] ▓")
		print ("▓ View local updates                                 [ID: 04] ▓")
		print ("▓ Check for updates through portable media devices   [ID: 05] ▓")
		print ("▓ Exit update manager                                [ID: 06] ▓")
		print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
		updateManID = int(input(">> Enter an ID to continue "))
		if updateManID == 1:
			print ("UCalc Web Identifier")
			print ("Checking for updates at www.ucalc.seanwallawalla.com/versions/history")
			print ("\n\nError! Could not connect to the internet. This version is incapable of receiving updates")
		if updateManID == 2:
			print ("Install updates through packages")
			print ("\nTest security package        0B")
			print ("\n\nError! This version is incapable of receiving updates")
		if updateManID == 3:
			print ("Install updates individually")
			print ("\nTest security update        0B")
			print ("\n\nError! This version is incapable of receiving updates")
		if updateManID == 4:
			print ("View local updates")
			print ("C://Desktop//")
			print ("\n\nError! This version is incapable of receiving updates")
		if updateManID == 5:
			print ("Check for updates thrugh portable media devices")
			print ("No devices were found")
			print ("Check to make sure the device is allowed to continue")
			print ("Compatible devices:")
			print ("\nSD card\tSolid State Hard Drive\tUSB drive\tHard Disk Drive")
			print ("\n\nError! This version is incapable of receiving updates")
		if updateManID == 6:
			print ("Exit update manager")
			print ("\n\nError! This version is incapable of receiving updates")
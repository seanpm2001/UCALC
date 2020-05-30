'''''''''''''''''''''''''''''''''''''''''''''''''''
| WARNING! NEVER MODIFY THE BUG/CRASH REPORTER!   |
| UNLESS YOU ARE A DEVELOPER, WE RECOMMEND TO     |
| NEVER MODIFY THIS SCRIPT. THIS CAN CAUSE SEVERE |
| ISSUES, AND CAN PREVENT THE SYSTEM FROM RUNNING |
| CORRECTLY. THANK YOU!                           |
|                               - Sean P. Myrick  |
| 12/01/02018 |                                   |
'''''''''''''''''''''''''''''''''''''''''''''''''''
reportErrorCount = int(0)
print ("Submit a bug report - Ucalc")
print ("---------------------------")
bugOrCrash = str(input("Are you submitting a bug report? (Y/N): "))
if (bugOrCrash == "Y"):
	print ("You are submitting a bug report. Let's continue! ")
else:
	print ("You are submitting a crash report. Let's continue! ")
print ("What type of account are you using? ")
acctype = str(input("| Local: ID = 1 | Web: ID = 2 |: "))
if (acctype == "1"):
	usernameForBug1 = str(input("Enter your username: "))
	passwordForBug1 = str(input("Enter your password: "))
if (acctype == "2"):
	usernameForBug1 = str(input("Enter your username: "))
	passwordForBug1 = str(input("Enter your password: "))
print ("===========================")
print ("What type of calculator processing mode did you use? ")
print ("| 4 bit | 8 bit | 12 bit | 16 bit | 18 bit | 24 bit | 31 bit | 32 bit | 48 bit | 64 bit | 128 bit |")
bitTypeForBug = int(input(">> "))
if bitTypeForBug == 4:
	print ("4 bit calculation mode selected")
if bitTypeForBug == 8:
	print ("8 bit calculation mode selected")
if bitTypeForBug == 12:
	print ("12 bit calculation mode selected")
if bitTypeForBug == 16:
	print ("16 bit calculation mode selected")
if bitTypeForBug == 24:
	print ("24 bit calculation mode selected")
if bitTypeForBug == 31:
	print ("31 bit calculation mode selected")
if bitTypeForBug == 32:
	print ("32 bit calculation mode selected")
if bitTypeForBug == 48:
	print ("48 bit calculation mode selected")
if bitTypeForBug == 64:
	print ("64 bit calculation mode selected")
if bitTypeForBug == 128:
	print ("128 bit calculation mode selected")
print ("What operating system are you using? ")
print ("Windows > | Windows Vista SP0, Windows Vista SP1, Windows Vista SP2, Windows Server 2008, Windows Server 2008 R2")
print ("Windows > | Windows XP x64 edition, Windows Server 2003, Windows Server 2003 R2, Windows 7 SP0, Windows 7 SP1")
print ("Windows > | Windows 8, Windows 8.1, Windows 10, Windows Server 2012, Windows Server 2016, Windows Server 2019")
print ("MacOS > | MacOS X 10.04, MacOS X 10.5, MacOS X 10.6, MacOS X 10.7, OS X 10.8, OS X 10.9, OS X 10.10, OS X 10.11")
print ("MacOS > | MacOS 10.12, MacOS 10.13, MacOS 10.14")
print ("Linux/Debian | Ubuntu 4.10, Ubuntu 5.04, Ubuntu 5.10, Ubuntu 6.04, Ubuntu 6.06, Ubuntu 6.10, Ubuntu 7.04, Ubuntu 7.10")
print ("Linux/Debian | Ubuntu 8.04, Ubuntu 8.10, Ubuntu 9.04, Ubuntu 9.10, Ubuntu 10.04, Ubuntu 10.10, Ubuntu 11.04, Ubuntu 11.10")
print ("Linux/Debian | Ubuntu 12.04, Ubuntu 12.10, Ubuntu 13.04, Ubuntu 13.10, Ubuntu 14.04, Ubuntu 14.10, Ubuntu 15.04, Ubuntu 15.10")
print ("Linux/Debian | Ubuntu 16.04, Ubuntu 16.10, Ubuntu 17.04, Ubuntu 17.10, Ubuntu 18.04, Ubuntu 18.10, Ubuntu 19.04")
print ("Linux/Debian | Lubuntu 10.04, Lubuntu 10.10, Lubuntu 11.04, Lubuntu 11.10, Lubuntu 12.04, Lubuntu 12.10, Lubuntu 13.04, Lubuntu 13.10")
print ("Linux/Debian | Lubuntu 14.04, Lubuntu 14.10, Lubuntu 15.04, Lubuntu 15.10, Lubuntu 16.04, Lubuntu 16.10, Lubuntu 17.04, Lubuntu 17.10")
print ("Linux/Debian | Lubuntu 18.04, Lubuntu 18.10, Lubuntu 19.04, Lubuntu 20.10")
print ("Linux/Debian | ")
print ("Linux/Android | Android 5.0, Android 5.1, Android 6.0, Android 6.1, Android 7.0, Android 7.1, Android 8.0, Android 8.1, Android 9.0")
print ("Linux/Android | Android 9.1, Android 10.0")
OSSelect = str(input("Enter the name of your operating system: "))
VMQues = str(input("Are you using a virtual machine? (Y/N)-: "))
if (VMQues == "Y"):
	print ("So you were using a virtual machine")
	print ("What is the virtualization software used? ")
	print ("Oracle VirtualBox | VMWare | Hyper-V | Bocs |")
	VMProType = str(input(">> "))
	if (VMProType == "Virtualbox"):
		print ("You selected 'Oracle Virtualbox' as your virtual machine host")
	if (VMProType == "VMWare"):
		print ("You selected 'VMWare' as your virtual machine host")
	if (VMProType == "Hyper-V"):
		print ("You selected 'Hyper-V' as your virtual machine host")
	if (VMProType == "Bocs"):
		print ("You selected 'Bocx' as your virtual machine host")
ramCount = float(input("How much RAM does your system have (in megabytes): "))
if (ramCount < 64.00):
	print ("Problem spotted: You do not have enough RAM to use this system")
	reportErrorCount + 1 
if (ramCount > 64.00):
	print ("You selected " + str(ramCount) + " Megabytes of RAM")
	print ("You meet the minimum system requirements")
modQues = str(input("Does your copy of UCalc contain any modifications? (Y/N): "))
if (modQues == "Y"):
	print ("So you modified UCalc")
	print ("Check the forums for information on modifications")
if (modQues == "N"):
	print ("You didn't use any mods")
print ("What type of processor are you using?")
print ("| AMD Radeon | Intel Pentium D | Itanium | IBM-based | Intel Celeron | Intel Optane |")
enterAProcessorType = str(input(">> "))
if (enterAProcessorType == "Pentium D"):
	print ("Problem spotted! You are using an outdated non-64 bit processor. UCalc is 64 bit software. Virtualized Pentiums are not capable with UCALC")
	reportErrorCount + 1 
print ("Write a description of your report: ")
print ("| Description |")
description = str(input(""))
print ("\n\n\n\n\nReport Summary")
print ("Report by: " + str(usernameForBug1))
print ("Problems with report: " + str(reportErrorCount))
print ("RAM in use: " + str(ramCount) + " Megabytes")
print ("Processor Type: " + str(enterAProcessorType))
if (VMQues == "Y"):
	print ("Virtualization software used: " + str(VMProType))
print ("Operating system used: " + str(OSSelect))
print ("Calculator processing operating bit mode: " + str(bitTypeForBug))
print ("Description: \n" + str(description))
print ("\n\n\nThank you for your report!")
finishReport = input("Press [ENTER] key to submit your report: ")
print ("Report sent successfully")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
'''''''''''''''''''''''''''''''''
|   End of bug/crash reporter   |
'''''''''''''''''''''''''''''''''
# written by Sean Myrick
# UCALC bug/crash reporter
# Version 0.1 Prototype - Alpha feature
# copyright 2018-2018 Sean Walla Walla
# modifications welcome while credit is given
# however we don't recommend a novice user modifying this script
# remixes should not modify this script without permission
'''''''''''''''''''''
| Modification days |
'''''''''''''''''''''
# 12/01/2018 
# no other days were used to modify this script
# end of program and script
# 133 lines total | 7112 characters total (7102 Bytes) (7.112 Kilobytes)
print ("Roman Numeral Calculator bootloader")
print ("Version 0.1 Alpha")
print ("\n\nSelect a mode: ")
print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print ("▒ 4 bit       MAX VALUE: 16 (XVI)      ▒ ID: 1 ▒")
print ("▒ 8 bit       MAX VALUE: 255 (CCLV)    ▒ ID: 2 ▒")
print ("▒ 12 bit      MAX VALUE: 4096 (???)    ▒ ID: 3 ▒")
print ("▒ 16 bit      MAX VALUE: 65535 (?????) ▒ ID: 4 ▒")
print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
file1 = int(1)
romeID = str(input("Enter an ID to start: "))
if romeID == ("1" or "one" or "ONE" or "One"):
	print ("\nPreparing to boot 4 bit Roman numeral calculator. Please wait...")
	if file1 == 1:
		print ("\nCould not load 4 bit roman Numeral calculator")
		print ("The following file is missing, modified, or corrupted:")
		print ("\nROMAN_NUMERAL_CALC_4BIT.py")
		print ("\nPlease repair or replace this file, then try again")
if romeID == ("2" or "two" or "TWO" or "Tweo"):
	print ("\nPreparing to boot 8 bit Roman numeral calculator. Please wait...")
	if file1 == 1:
		print ("\nCould not load 8 bit roman Numeral calculator")
		print ("The following file is missing, modified, or corrupted:")
		print ("\nROMAN_NUMERAL_CALC_8BIT.py")
		print ("\nPlease repair or replace this file, then try again")
if romeID == ("3" or "three" or "THREE" or "Three"):
	print ("\nPreparing to boot 12 bit Roman numeral calculator. Please wait...")
	if file1 == 1:
		print ("\nCould not load 12 bit roman Numeral calculator")
		print ("The following file is missing, modified, or corrupted:")
		print ("\nROMAN_NUMERAL_CALC_12BIT.py")
		print ("\nPlease repair or replace this file, then try again")
if romeID == ("4" or "four" or "FOUR" or "Four"):
	print ("\nPreparing to boot 12 bit Roman numeral calculator. Please wait...")
	if file1 == 1:
		print ("\nCould not load 12 bit roman Numeral calculator")
		print ("The following file is missing, modified, or corrupted:")
		print ("\nROMAN_NUMERAL_CALC_12BIT.py")
		print ("\nPlease repair or replace this file, then try again")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAn unexpected error has occured")
print ("Preparing to shut down the Roman Numeral Bootloader")
endRome = input("Press [ENTER] key to exit Roman Numeral Bootloader")
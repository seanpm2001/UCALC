print (" ")
print ("  ___  _____  __  __  _  _  ____  ____  _  _  ___ ")
print (" / __)(  _  )(  )(  )( \\( )(_  _)(_  _)( \\( )/ __)")
print ("( (__  )(_)(  )(__)(  )  (   )(   _)(_  )  (( (_-.")
print (" \___)(_____)(______)(_)\\_) (__) (____)(_)\_)\\___/")
print (" __  __    __    ___  _   _  ____  _  _  ____     ")
print ("(  \/  )  /__\\  / __)( )_( )(_  _)( \\( )( ___)    ")
print (" )    (  /(__)\\( (__  ) _ (  _)(_  )  (  )__)     ")
print ("(_/\/\_)(__)(__)\\___)(_) (_)(____)(_)\\_)(____)    ")
print ("  __  ___   ___      ")                             
print (" /  )(__ \\ ( _ )      ")                            
print ("  )(  / _/ / _ \\        ")                          
print (" (__)(____)\\___/          ")                        
print (" ")
enterToEnter = input("Press [ENTER] key to start")
print ("ABOUT")
print ("This is a quick program Sean wrote to exercise his ability on loops in python")
print ("You can count backwards or forwards to integers 4 to 128. It would take a VERY long time")
print ("(maybe a few milleniums) to go from the lowest value to the highest value")
enterToCont = input("Press [ENTER] key to continue")
print ("Integer limits")
print ("4 bit")
print ("Minimum: -16")
print ("Maximum: 16")
print ("8 bit")
print ("Minimum: -256")
print ("Maximum: 256")
print ("12 bit")
print ("Minimum: -4096")
print ("Maximum: 4096")
print ("16 bit")
print ("Minimum: -65536")
print ("Maximum: 65536")
print ("18 bit")
print ("Minimum: -262144")
print ("Maximum: 262144")
print ("24 bit")
print ("Minimum: -8388607")
print ("Maximum: 8388607")
print ("26 bit")
print ("Minimum: -33554428")
print ("Maximum: 33554428")
print ("31 bit")
print ("Minimum: -1073741696")
print ("Maximum: 1073741696")
print ("32 bit")
print ("Minimum: -2147483392")
print ("Maximum: 2147483392")
print ("36 bit")
print ("Minimum: -34359734272")
print ("Maximum: 34359734272")
print ("48 bit")
print ("Minimum: -140737488355327")
print ("Maximum: 140737488355327")
print ("60 bit")
print ("Minimum: -140737488355327")
print ("Maximum: 140737488355327")
print ("64 bit")
print ("Minimum: -9223372036854775807")
print ("Maximum: 9223372036854775807")
print ("128 bit")
print ("Minimum: -170141183460469231731687303715884105728")
print ("Maximum: 170141183460469231731687303715884105728")
enterToCont = input("Press [ENTER] key to continue")
print ("Modes\n| Integers (0) | Select numbers (1)")
modeStart = int(input("Enter a mode ID to launch a mode to start with: "))
if modeStart == 0:
    counter = int(input("Enter a starting number: "))
    print ("Forwards (1) | Backwards (0) ")
    countdirect = str(input("Which way do you want to count (+ or -) (0 or 1)? "))
    print ("4 bit | 8 bit | 12 bit | 16 bit | 18 bit | 24 bit | 26 bit | 31 bit | 32 bit | 36 bit | 48 bit | 60 bit | 64 bit | 128 bit |")
    countdec = str(input("What is the integer you want to use? "))
    if (countdec == "4"):
        if (countdirect == "0"):
            while (countdirect > -17 and not counter == -17):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 17 and not counter == 17):
                print (str(counter))
                counter = counter + 1
    if (countdec == "8"):
        if (countdirect == "0"):
            while (countdirect > -256 and not counter == -256):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 256 and not counter == 256):
                print (str(counter))
                counter = counter + 1
    if (countdec == "12"):
        if (countdirect == "0"):
            while (countdirect > -4097 and not counter == -4097):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 4097 and not counter == 4097):
                print (str(counter))
                counter = counter + 1
    if (countdec == "16"):
        if (countdirect == "0"):
            while (countdirect > -65536 and not counter == -65536):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 65536 and not counter == 65536):
                print (str(counter))
                counter = counter + 1
    if (countdec == "18"):
        if (countdirect == "0"):
            while (countdirect > -262144 and not counter == -262144):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 262144 and not counter == 262144):
                print (str(counter))
                counter = counter + 1
    if (countdec == "24"):
        if (countdirect == "0"):
            while (countdirect > -8388607 and not counter == -8388607):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 8388607 and not counter == 8388607):
                print (str(counter))
                counter = counter + 1
    if (countdec == "26"):
        if (countdirect == "0"):
            while (countdirect > -33554428 and not counter == 33554428):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 33554428 and not counter == 33554428):
                print (str(counter))
                counter = counter + 1
    if (countdec == "31"):
        if (countdirect == "0"):
            while (countdirect > -1073741696 and not counter == 1073741696):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 1073741696 and not counter == 1073741696):
                print (str(counter))
                counter = counter + 1
    if (countdec == "32"):
        if (countdirect == "0"):
            while (countdirect > -2147483392 and not counter == 2147483392):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 2147483392 and not counter == 2147483392):
                print (str(counter))
                counter = counter + 1
    if (countdec == "36"):
        if (countdirect == "0"):
            while (countdirect > -34359734272 and not counter == 34359734272):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 34359734272 and not counter == 34359734272):
                print (str(counter))
                counter = counter + 1
    if (countdec == "48"):
        if (countdirect == "0"):
            while (countdirect > -140737488355327 and not counter == 140737488355327):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 140737488355327 and not counter == 140737488355327):
                print (str(counter))
                counter = counter + 1
    if (countdec == "60"): # not complete
        if (countdirect == "0"):
            while (countdirect > -140737488355327 and not counter == 140737488355327):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 140737488355327 and not counter == 140737488355327):
                print (str(counter))
                counter = counter + 1
    if (countdec == "64"):
        if (countdirect == "0"):
            while (countdirect > -9223372036854775807 and not counter == 9223372036854775807):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 9223372036854775807 and not counter == 9223372036854775807):
                print (str(counter))
                counter = counter + 1
    if (countdec == "128"):
        if (countdirect == "0"):
            while (countdirect > -170141183460469231731687303715884105728 and not counter == 170141183460469231731687303715884105728):
                print (str(counter))
                counter = counter - 1
        if (countdirect == "1"):
            while (countdirect > 170141183460469231731687303715884105728 and not counter == 170141183460469231731687303715884105728):
                print (str(counter))
                counter = counter + 1
    print ("You have reached your destination!")
if modeStart == 1:
    print ("Make sure the sequence is correct. If the sequence range is set incorrectly, it will keep counting until it crashes")
    counter = int(input("Enter a starting number: "))
    countend = int(input("Enter a stopping number: "))
    forback = int(input("| Count backwards (0) | Count forwards (1) | "))
    while not (counter == countend):
        if forback == 0:
            print (counter)
            counter = counter - 1
        if forback == 1:
            print (counter)
            counter = counter + 1
    print ("You have reached your destination")
noMore = input("Press [ENTER] key to quit")
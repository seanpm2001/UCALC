# start of script
print ("=========================") # start of Splash dialog box
print ("| UCALC Camera Terminal |") # Title
print ("=========================") # end of Splash dialog box
print ("Welcome to the camera terminal! Here, you can modify camera settings before you go into real-world solve mode") # Brief description
print ("For help, type ./help") # or read the documentation
loop1 = float(1.0) # modify the loop to exit the terminal. Add anything but numbers or decimals to prevent the program from running
while (loop1 == 1.0): # start of the loop
    term1con = str(input("UCALC>>")) # Main console
    if (term1con == "./help"): # start of help command 
        print ("Camera terminaL help") # start of help dialog 
        print ("_____________________________________________________") # top of the dialog box 
        print ("./font        | Adjust font settings                |") # font command
        print ("./type        | Adjust equation types               |") # type command
        print ("./library     | Adjust saving settings              |") # library command
        print ("./help        | Get help with the image terminal    |") # help command (but you are already running it)
        print ("./launch      | Launch the calculator               |") # launch command
        print ("./quit        | Exit the camera terminal            |") # quit command
        print ("./resolution  | Adjust resolution settings          |") # resolution command
        print ("./color       | Adjust color settings               |") # color command
        print ("./limit       | Set library limits                  |") # limit command
        print ("./rules       | View rules                          |") # rules command 
        print ("./export      | Change document export settings     |") # export command
        print ("=====================================================") # bottom of the dialog box
        # end of help dialog
        print ("\nTip: Remember to clean your camera for accuracy when taking pictures") # out-of-place reminder
    if (term1con == "./font"): # start of font list 
        print ("Font settings") # title
        print ("Auto detect [ID: AD]") # auto-detect (recommended)
        print ("Agency FB [ID: A01]") # FONT1
        print ("Arial [ID: A02]") # FONT2
        print ("Arial Black [ID: A03]") # FONT3
        print ("Bell MT [ID: A04]") # FONT4
        print ("Broadway [ID: A05]") # FONT5
        print ("Calibri [ID: A06]") # FONT6
        print ("Cambria [ID: A07]") # FONT7
        print ("Comic Sans MS [ID: A08]") # FONT8
        print ("Consolas [ID: A09]") # FONT9
        print ("Corbel [ID: A10]") # FONT10
        print ("Courier [ID: A11]") # FONT11
        print ("Courier new [ID: A12]") # FONT12
        print ("Elephant [ID: A13]") # FONT13
        print ("Impact [ID: A14]") # FONT14
        print ("lucidia console [ID: A15]") # FONT15
        print ("Minion Pro [ID: A16]") # FONT16
        print ("System [ID: A17]") # FONT17
        print ("Trebuchet MS [ID: A18]") # FONT18
        print ("Vladimir script [ID: A19]")  # FONT19 
        # end of font list 
        print ("Type an ID to continue") # ID reminder (standard)
        fontIDCon = str(input("FONT>>")) # font terminal 
        if (fontIDCon == "AD"): # Auto-detect selected
            print ("You have enabled auto-detect") # heading 
            print ("This feature is in beta and may be inaccurate") # warning
            enterNext = input("Press [ENTER] key to continue") # pause 
    if (term1con == "./type"): # start of equation type list 
        print ("Type of equations: ")
        print ("Addition [ID: 1]")
        print ("Subtraction [ID: 2]")
        print ("Multiplication [ID: 3]")
        print ("Division [ID: 4]")
        print ("Modular division [ID: 5]")
        print ("Powers [ID: 6]") # end of equation type list
        print ("Type an ID to continue: ") # ID reminder (standard)
        mathTypeCon = str(input("TYPE>>")) # equation type terminal
    if (term1con == "./library"): # start of library command 
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
        print ("Type an ID to continue: ") # ID reminder (standard)
        libSettCon = str(input("LIB>>")) # Library settings console
        if (libSettCon == "0"):
            print ("Operation cancelled")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "1"):
            print ("Original images will now be saved to the gallery")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "2"):
            print ("Original images will now not be saved to the gallery")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "3"):
            print ("Answered images will now be saved to the gallery")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "4"):
            print ("Answered images will now not be saved to the gallery")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "5"):
            print ("Original images will now be saved as JPG files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "6"):
            print ("Original images will now be saved as PNG files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "7"):
            print ("Original images will now be saved as HEIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "8"):
            print ("Original images will now be saved as GIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "9"):
            print ("Original images will now be saved as TIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "10"):
            print ("Original images will now be saved as BMP files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "11"):
            print ("Answered images will now be saved as JPG files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "12"):
            print ("Answered images will now be saved as PNG files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "13"):
            print ("Answered images will now be saved as HEIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "14"):
            print ("Answered images will now be saved as GIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "15"):
            print ("Answered images will now be saved as TIF files")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (libSettCon == "16"):
            print ("Answered images will now be saved as BMP files")
            enterNext = input("Press [ENTER] key to continue") # pause 
    if (term1con == "./launch"):
        print ("Launching real-world solve mode...")
    if (term1con == "./quit"):
        print ("Confirm going back to the main calculator by typing Y") # Confirm Quit notice 
        quit1 = str(input("Quit? (Y/N):")) # Confirm quit 
        if (quit1 == "Y" or quit1 == "y"):
            print ("Exiting... please wait (Press [ENTER] key to exit immediately)") # Final pause
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
        # end of resolution list
        print ("Enter an ID to continue (the resolution is the ID)")  # ID reminder (standard)
        resCon1 = str(input("ID>>")) # beginning of resolution loop
        if (resCon1 == "1280x720"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1280x720") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "1336x730"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1336x730") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "1400x720"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1400x720") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "1450x800"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1450x800") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "1600x720"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1600x720") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "1920x1080"): # resolution change question
            print ("Your camera resolution for UCALC was set to 1920x1080") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "2400x1080"): # resolution change question
            print ("Your camera resolution for UCALC was set to 2400x1080") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "2560xx1440"): # resolution change question:
            print ("Your camera resolution for UCALC was set to 2560x1440") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "3200x1440"): # resolution change question
            print ("Your camera resolution for UCALC was set to 3200x1440") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (resCon1 == "3840x2160"): # resolution change question
            print ("Your camera resolution for UCALC was set to 3840x2160") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
            # end of resolution loop
    if (term1con == "./color"): # color command 
        print ("Color settings") # title
        print ("Modify answer colors") # heading 
        print ("Select a color by typing its name")  # ID reminder (standard)
        print ("Black") # color 1
        print ("White") # color 2
        print ("Silver") # color 3
        print ("Cyan") # color 4
        print ("Light green") # color 5
        print ("Dark green") # color 6
        print ("Light red") # color 7
        print ("Dark red") # color 8
        print ("Yellow") # color 9
        print ("Orange") # color 10
        print ("Magenta") # color 11
        print ("Gold") # color 12
        print ("Bronze") # color 13
        print ("Brown") # color 14
        print ("Pink") # color 15
        colorName1 = str(input("COLOR>>")) # beginning of color loop
        if (colorName1 == "black" or colorName1 == "Black" or colorName1 == "BLACK"): # Color 1
            print ("Answer font color changed to Black") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "white" or colorName1 == "White" or colorName1 == "WHITE"): # Color 2
            print ("Answer font color changed to white") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "silver" or colorName1 == "Silver" or colorName1 == "SILVER"): # Color 3
            print ("Answer font color changed to Silver") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "cyan" or colorName1 == "Cyan" or colorName1 == "CYAN"): # Color 4
            print ("Answer font color changed to Cyan") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "light green" or colorName1 == "Light green" or colorName1 == "Light Green" or colorName1 == "LIGHT GREEN"): # Color 5
            print ("Answer font color changed to Light Green") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "dark green" or colorName1 == "Dark green" or colorName1 == "Dark Green" or colorName1 == "DARK GREEN"): # Color 6
            print ("Answer font color changed to Dark Green") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "light red" or colorName1 == "Light red" or colorName1 == "Light Red" or colorName1 == "LIGHT RED"): # Color 7
            print ("Answer font color changed to Light Red") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "dark red" or colorName1 == "Dark red" or colorName1 == "Dark Red" or colorName1 == "DARK RED"): # Color 8
            print ("Answer font color changed to Dark Red") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "yellow" or colorName1 == "Yellow" or colorName1 == "YELLOW"): # Color 9
            print ("Answer font color changed to Yellow") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "orange" or colorName1 == "Orange" or colorName1 == "ORANGE"): # Color 10
            print ("Answer font color changed to Orange") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "magenta" or colorName1 == "Magenta" or colorName1 == "MAGENTA"): # Color 11
            print ("Answer font color changed to Magenta") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "gold" or colorName1 == "Gold" or colorName1 == "GOLD"): # Color 12
            print ("Answer font color changed to Gold") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "bronze" or colorName1 == "Bronze" or colorName1 == "BRONZE"): # Color 13
            print ("Answer font color changed to Bronze") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "brown" or colorName1 == "Brown" or colorName1 == "BROWN"): # Color 14
            print ("Answer font color changed to Brown") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (colorName1 == "pink" or colorName1 == "Pink" or colorName1 == "PINK"): # Color 15
            print ("Answer font color changed to Brown") # changes made
            enterNext = input("Press [ENTER] key to continue") # pause 
        # end of color loop
    if (term1con == "./limit"): # limit command 
        print ("Set limits") # title
        print ("==================================================") # top of dialog box
        print ("Maximum picture folder size settings [ID: 1]") # option 1
        print ("Maximum picture count [ID: 2]") # option 2
        print ("Daily uses [ID: 3]") # option 3
        print ("==================================================") # bottom of dialog box 
        print ("Enter an ID to continue setting limits") # ID reminder (ztandard)
        limID = str(input("LIMID>>"))  # Limit ID console
        # start of limit loop
        if (limID == "1"): # option 1 chosen 
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
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "1"):
                print ("Limit set to 10 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "2"):
                print ("Limit set to 15 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "3"):
                print ("Limit set to 20 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "4"):
                print ("Limit set to 25 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "5"):
                print ("Limit set to 30 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "6"):
                print ("Limit set to 40 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "7"):
                print ("Limit set to 50 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "8"):
                print ("Limit set to 60 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "9"):
                print ("Limit set to 75 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "10"):
                print ("Limit set to 80 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "11"):
                print ("Limit set to 90 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "12"):
                print ("Limit set to 95 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "13"):
                print ("Limit set to 100 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "14"):
                print ("Limit set to 110 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "15"):
                print ("Limit set to 120 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "16"):
                print ("Limit set to 125 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "17"):
                print ("Limit set to 130 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "18"):
                print ("Limit set to 140 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            if (limitMBID == "19"):
                print ("Limit set to 150 Megabytes")
                enterNext = input("Press [ENTER] key to continue") # pause 
            # end of size limit loop
        if (limID == "2"): # option 2 chosen 
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
        if (limID == "3"): # option 3 chosen 
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
            enterNext = input("Press [ENTER] key to continue") # pause 
    if (term1con == "./rules"): # rules command
        print ("Rules") # title
        print ("With great power comes great responsibility") # quote
        print ("========================") # top of dialog box
        print ("DO NOT USE THIS TO CHEAT")
        print ("This is a tool for personal work. This shouldn't be used to skip your way through math class. Math is very important in society, and you really should learn it, as it has to be used every day")
        print ("========================") # bottom of dialog box
        print ("End of rule listing") # footer 
        enterNext = input("Press [ENTER] key to continue") # pause 
    if (term1con == "./export"): # export command
        print ("Document exporting") # title
        print ("===============") # top of dialog box
        print ("Export types:") # heading 
        print ("Export as DOC (Word 1.0, 1.1, 2.0, 3.0, 4.0, 5.0, 6.0, 95, 97, 2000, XP, 2003 document)") # format 1
        print ("Export as DOCX (Word 2007, 2010, 2013, 2016, 2019 document)") # format 2
        print ("Export as RTF (Rich Text Format)") # format 3
        print ("Export as PDF (Portable Document Format)") # format 4
        print ("Export as EPUB 2.0") # format 5
        print ("Export as EPUB 3.0") # format 6
        print ("Export as XPS") # format 7
        print ("Export as ODT (Open Document Text)")  # format 8
        print ("Export as UOT (Unified Office Text)")  # format 9
        print ("Export as TXT ([Plain Text Document)")  # format 10
        print ("=====================================================") # bottom of dialog box
        print ("Export in multiple formats [ID: 0A]") # option 1
        print ("Don't export in multiple formats [ID: 0B]") # option 2
        # separation field
        print ("Export original as DOC [ID: 10]") # option 3
        print ("Export answers as DOC [ID: 11]") # option 4
        print ("Export original as DOCX [ID: 12]") # option 5
        print ("Export answers as DOCX [ID: 13]") # option 6
        print ("Export original as RTF [ID: 14]") # option 7
        print ("Export answers as RTF [ID: 15]") # option 8
        print ("Export original as PDF [ID: 16]") # option 9
        print ("Export answers as PDF [ID: 17]") # option 10
        print ("Export original as EPUB 2 [ID: 18]") # option 11
        print ("Export answers as EPUB 2 [ID: 19]") # option 12
        print ("Export original as EPUB 3 [ID: 20]") # option 13
        print ("Export answers as EPUB 3 [ID: 21]") # option 14
        print ("Export original as XPS [ID: 22]") # option 15
        print ("Export answers as XPS [ID: 23]") # option 16
        print ("Export original as ODT [ID: 24]") # option 17
        print ("Export answers as ODT [ID: 25]") # option 18
        print ("Export original as UOT [ID: 26]") # option 19
        print ("Export answers as UOT [ID: 27]") # option 20
        print ("Export original as TXT [ID: 27A]") # option 21
        print ("Export answers as TXT [ID: 27B]") # option 22
        # Separation field
        print ("Don't Export original as DOC [ID: 28]") # option 23
        print ("Don't Export answers as DOC [ID: 29]") # option 24
        print ("Don't Export original as DOCX [ID: 30]") # option 25
        print ("Don't Export answers as DOCX [ID: 31]") # option 26
        print ("Don't Export original as RTF [ID: 32]") # option 27
        print ("Don't Export answers as RTF [ID: 33]") # option 28
        print ("Don't Export original as PDF [ID: 34]") # option 29
        print ("Don't Export answers as PDF [ID: 35]") # option 30
        print ("Don't Export original as EPUB 2 [ID: 36]") # option 31
        print ("Don't Export answers as EPUB 2 [ID: 37]") # option 32
        print ("Don't Export original as EPUB 3 [ID: 38]") # option 33
        print ("Don't Export answers as EPUB 3 [ID: 39]") # option 34
        print ("Don't Export original as XPS [ID: 40]") # option 35
        print ("Don't Export answers as XPS [ID: 41]") # option 36
        print ("Don't Export original as ODT [ID: 42]") # option 37
        print ("Don't Export answers as ODT [ID: 43]") # option 38
        print ("Don't Export original as UOT [ID: 44]") # option 39
        print ("Don't Export answers as UOT [ID: 45]") # option 40
        print ("Don't Export original as TXT [ID: 46]") # option 41
        print ("Don't Export answers as TXT [ID: 47]") # option 42
        # separation field
        print ("Save separate merged copy [ID: 10A]") # option 43
        print ("Don't save separate merged copy [ID: 10B]") # option 44
        print ("Enter an ID to continue: ") # ID reminder (standard)
        docExCon = str(input("DOCEX>>")) # start of docExID loop
        if (docExCon == "0a" or docExCon == "0A" or docExCon == "a0" or docExCon == "A0"):
            print ("Exports will now save in multiple formats. Please rerun the command to select formats") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "0b" or docExCon == "0B" or docExCon == "b0" or docExCon == "B0"):
            print ("Exports will not save in multiple formats") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "10"):
            print ("The original copy will now be saved as a DOC file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "11"):
            print ("The answered copy will now be saved as a DOC file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "12"):
            print ("The original copy will now be saved as a DOCX file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "13"):
            print ("The answered copy will now be saved as a DOCX file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "14"):
            print ("The original copy will now be saved as a RTF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "15"):
            print ("The answered copy will now be saved as a RTF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "16"):
            print ("The original copy will now be saved as a PDF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "17"):
            print ("The answered copy will now be saved as a PDF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "18"):
            print ("The original copy will now be saved as a EPUB 2.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "19"):
            print ("The answered copy will now be saved as a EPUB 2.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "20"):
            print ("The original copy will now be saved as a EPUB 3.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "21"):
            print ("The answered copy will now be saved as a EPUB 3.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "22"):
            print ("The original copy will now be saved as a XPS file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "23"):
            print ("The answered copy will now be saved as a XPS file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "24"):
            print ("The original copy will now be saved as a ODT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "25"):
            print ("The answered copy will now be saved as a ODT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "26"):
            print ("The original copy will now be saved as a UOT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "27"):
            print ("The answered copy will now be saved as a UOT file")
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "27a" or docExCon == "27A" or docExCon == "a27" or docExCon == "A27"):
            print ("The original copy will now be saved as a TXT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "27b" or docExCon == "27B" or docExCon == "b27" or docExCon == "B27"):
            print ("The answered copy will now be saved as a TXT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        # separation field 
        if (docExCon == "28"):
            print ("The original copy will no longer be saved as a DOC file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "29"):
            print ("The answered copy will no longer be saved as a DOC file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "30"):
            print ("The original copy will no longer be saved as a DOCX file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "31"):
            print ("The answered copy will no longer be saved as a DOCX file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "32"):
            print ("The original copy will no longer be saved as a RTF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "33"):
            print ("The answered copy will no longer be saved as a RTF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "34"):
            print ("The original copy will no longer be saved as a PDF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "35"):
            print ("The answered copy will no longer be saved as a PDF file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "36"):
            print ("The original copy will no longer be saved as a EPUB 2.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "37"):
            print ("The answered copy will no longer be saved as a EPUB 2.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "38"):
            print ("The original copy will no longer be saved as a EPUB 3.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "39"):
            print ("The answered copy will no longer be saved as a EPUB 3.0 file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "40"):
            print ("The original copy will no longer be saved as a XPS file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "41"):
            print ("The answered copy will no longer be saved as a XPS file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "42"):
            print ("The original copy will no longer be saved as a ODT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "43"):
            print ("The answered copy will no longer be saved as a ODT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "44"):
            print ("The original copy will no longer be saved as a UOT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "45"):
            print ("The answered copy will no longer be saved as a UOT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "46"):
            print ("The original copy will no longer be saved as a TXT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        if (docExCon == "47"):
            print ("The answered copy will no longer be saved as a TXT file") # changes made 
            enterNext = input("Press [ENTER] key to continue") # pause 
        # end of docExID loop
# end of the loop
noMore = input("Press [ENTER] key to quit") # final pause (Might not activate)
# end of script
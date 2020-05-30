		if calcIDSes == 22:
					print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
					print ("RGB Calculator")
					red1 = int(input("[RED] Enter a number 0-255 "))
					green1 = int(input("[GREEN] Enter a number 0-255 "))
					blue1 = int(input("[BLUE] Enter a number 0-255 "))
					print ("r: " + str(red1) + " g: " + str(green1) + " b: " + str(blue1))
					if (red1 == 0) and (green1 == 0) and (blue1 == 0):
						print ("The current color is [BLACK]")
					if (red1 == 255) and (green1 == 255) and (blue1 == 255):
						print ("The current color is [WHITE]")
					if (red1 == 255) and (green1 == 0) and (blue1 == 0):
						print ("The current color is [RED]")
					if (red1 == 0) and (green1 == 255) and (blue1 == 0):
						print ("The current color is [GREEN]")
					if (red1 == 0) and (green1 == 0) and (blue1 == 255):
						print ("The current color is [BLUE]")
					if (red1 == 255) and (green1 == 255) and (blue1 == 0):
						print ("The current color is [YELLOW]")
					if (red1 == 255) and (green1 == 0) and (blue1 == 255):
						print ("The current color is [MAGENTA]")
					if (red1 == 0) and (green1 == 255) and (blue1 == 255):
						print ("The current color is [CYAN]")
					print ("Thank you for using the RGB calculator!")
					bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
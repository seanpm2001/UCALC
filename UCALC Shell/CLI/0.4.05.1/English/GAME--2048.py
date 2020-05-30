print (" ")
print (" ")
print ("  ___   ___  _  _   ___     ")  
print (" |__ \\ / _ \\| || | / _ \\   ")   
print ("    ) | | | | || || (_) |     ")
print ("   / /| | | |__   _> _ <      ")
print ("  / /_| |_| |  | || (_) |     ")
print (" |____|\\___/___|_|_\\___/_____ ")
print (" |______|______|______|______|")
print ("  / _` |/ _` | '_ ` _ \\ / _ \\ ")
print (" | (_| | (_| | | | | | |  __/ ")
print ("  \\__, |\\__,_|_| |_| |_|\\___|") 
print ("   __/ |                      ")
print ("  |___/                       ")
print (" ")
print (" ")
enterToEnter = input("Press [ENTER] key to start! ")
gameselectID = int(10)
if gameselectID == 10:
	if gameselectID == 10:
		if gameselectID == 10:
			if gameselectID == 10:
				if gameselectID == 10:
					if gameselectID == 10:
						print ("\n\n\n\n\n\n\n\n")
						print ("Welcome to 2048!")
						print ("Multiples of 2:")
						print ("2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 9192, 16384, 32768, x+")
						twoCount = int(2)
						count4 = int(0)
						count8 = int(0)
						count16 = int(0)
						count32 = int(0)
						count64 = int(0)
						count128 = int(0)
						count256 = int(0)
						count512 = int(0)
						count1024 = int(0)
						count2048 = int(0)
						count4096 = int(0)
						count8192 = int(0)
						count16384 = int(0)
						count32768 = int(0)
						count65536 = int(0)
						count131072 = int(0)
						count262144 = int(0)
						count524288 = int(0)
						count1048576 = int(0)
						count2097152 = int(0)
						count4194304 = int(0)
						score = int(0)
						moves = int(0)
						highScore = int(0)
						print ("Select a mode: ")
						print ("16 - Get to 16 to win")
						print ("32 - Get to 32 to win")
						print ("64 - Get to 64 to win")
						print ("128 - Get to 128 to win")
						print ("256 - Get to 256 to win")
						print ("512 - Get to 512 to win")
						print ("1024 - Get to 1024 to win")
						print ("2048 - Get to 2048 to win")
						print ("4096 - Get to 4096 to win")
						print ("8192 - Get to 8192 to win")
						print ("16384 - Get to 16384 to win")
						print ("32768 - Get to 32768 to win")
						print ("65535 - Get to 65536 to win")
						print ("131072 - Get to 131072 to win")
						print ("262144 - Get to 262144 to win")
						print ("524288 - Get to 524288 to win")
						print ("1048576 - Get to 1048576 to win")
						print ("2097152 - Get to 2097152 to win")
						print ("4194304 - Get to 4194304 to win")
						print ("=====================================")
						GameID = int(input("Enter an ID to start (the ID is the end goal number)"))
						if (GameID == 16): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count256 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 32): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count256 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 64): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count256 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 128): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count256 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 256): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 512): 
							while not (count512 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 0):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 1024):
							while not (count2048 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count2048 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)				
						if (GameID == 2048):
							while not (count2048 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)				
						if (GameID == 4096):
							while not (count8192 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count8192 > 1):
										print ("Error: cannot merge any higher")					
								if (score > highScore):
									(highScore == score)	
						if (GameID == 8192):
							while not (count8192 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										print ("Error: cannot merge any higher")					
								if (score > highScore):
									(highScore == score)
						if (GameID == 16384):									
							while not (count16384 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count262144 > 1):
										print ("Error. Cannot merge any higher than that")
								if (score > highScore):
									(highScore == score)
						if (GameID == 32768):
							while not (count32768 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										print ("Error. Cannot merge any higher than that")
								if (score > highScore):
									(highScore == score)					
						if (GameID == 65536):
							while not (count65536 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 131072):
							while not (count131072 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 262144):
							while not (count262144 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x" + "\t\t" + "[262144] " + str(count262144) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									if (count131072 > 1):
										count131072 = count131072 - 2
										count262144 = count262144 + 1
										score = score + 262144
										moves = moves + 1
								if mergecon == 262144:
									if (count262144 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 524288):
							while not (count524288 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x" + "\t\t" + "[262144] " + str(count262144) + "x")
								print ("[524288] " + str(count524288) + "x ")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									if (count131072 > 1):
										count131072 = count131072 - 2
										count262144 = count262144 + 1
										score = score + 262144
										moves = moves + 1
								if mergecon == 262144:
									if (count262144 > 1):
										count262144 = count262144 - 2
										count524288 = count524288 + 1
										score = score + 524288
										moves = moves + 1
								if mergecon == 524288:
									if (count524288 > 1):
										print ("Error: cannot merge any higher")
								if (score > highScore):
									(highScore == score)
						if (GameID == 1048576):
							while not (count1048576 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x" + "\t\t" + "[262144] " + str(count262144) + "x")
								print ("[524288] " + str(count524288) + "x" + "\t\t" + "[1048576] " + str(count1048576) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									if (count131072 > 1):
										count131072 = count131072 - 2
										count262144 = count262144 + 1
										score = score + 262144
										moves = moves + 1
								if mergecon == 262144:
									if (count262144 > 1):
										count262144 = count262144 - 2
										count524288 = count524288 + 1
										score = score + 524288
										moves = moves + 1
								if mergecon == 524288:
									if (count524288 > 1):
										count524288 = count524288 - 2
										count1048576 = count1048576 + 1
										score = score + 1048576
										moves = moves + 1
								if mergecon == 1048576:
									if (count1048576 > 1):
										print ("Error. Cannot merge any higher than that")
								if (score > highScore):
									(highScore == score)
						if (GameID == 2097152):
							while not (count2097152 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x" + "\t\t" + "[262144] " + str(count262144) + "x")
								print ("[524288] " + str(count524288) + "x" + "\t\t" + "[1048576] " + str(count1048576) + "x" + "\t\t" + "[2097152] " + str(count2097152) + "x")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									if (count131072 > 1):
										count131072 = count131072 - 2
										count262144 = count262144 + 1
										score = score + 262144
										moves = moves + 1
								if mergecon == 262144:
									if (count262144 > 1):
										count262144 = count262144 - 2
										count524288 = count524288 + 1
										score = score + 524288
										moves = moves + 1
								if mergecon == 524288:
									if (count524288 > 1):
										count524288 = count524288 - 2
										count1048576 = count1048576 + 1
										score = score + 1048576
										moves = moves + 1
								if mergecon == 1048576:
									if (count1048576 > 1):
										count1048576 = count1048576 - 2
										count2097152 = count2097152 + 1	
										score = score + 2097152
										moves = moves + 1
								if mergecon == 2097152:
									if (count262144 > 1):
										print ("Error. Cannot merge any higher than that")
								if (score > highScore):
									(highScore == score)
						if (GameID == 4194304):
							while not (count2097152 == 1):
								print ("░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓[2048]░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓░▒▓")
								print ("Score: " + str(score))
								print ("High score: " + str(highScore))
								print ("Total moves: " + str(moves))
								twoCount = twoCount + 2
								print ("Your current blocks: ")
								print ("[2] " + str(twoCount) + "x" + "\t\t" + "[4] " + str(count4) + "x" + "\t\t" + "[8] " + str(count8) + "x")
								print ("[16] " + str(count16) + "x" + "\t\t" + "[32] " + str(count32) + "x" + "\t\t" + "[64] " + str(count64) + "x")
								print ("[128] " + str(count128) + "x" + "\t\t" + "[256] " + str(count256) + "x" + "\t\t" + "[512] " + str(count512) + "x")
								print ("[1024] " + str(count1024) + "x" + "\t\t" + "[2048] " + str(count2048) + "x" + "\t\t" + "[4096] " + str(count4096) + "x")
								print ("[8192] " + str(count8192) + "x" + "\t\t" + "[16384] " + str(count16384) + "x" + "\t\t" + "[32768] " + str(count32768) + "x")
								print ("[65536] " + str(count65536) + "x" + "\t\t" + "[131072] " + str(count131072) + "x" + "\t\t" + "[262144] " + str(count262144) + "x")
								print ("[524288] " + str(count524288) + "x" + "\t\t" + "[1048576] " + str(count1048576) + "x" + "\t\t" + "[2097152] " + str(count2097152) + "x")
								print ("[4194304] " + str(count4194304) + "x ")
								mergecon = int(input("Enter a number to merge: "))
								if mergecon == 2:
									if (twoCount > 1):
										twoCount = twoCount - 2
										count4 = count4 + 1
										score = score + 4
										moves = moves + 1
								if mergecon == 4:
									if (count4 > 1):
										count4 = count4 - 2
										count8 = count8 + 1
										score = score + 8
										moves = moves + 1
								if mergecon == 8:
									if (count8 > 1):
										count8 = count8 - 2
										count16 = count16 + 1
										score = score + 16
										moves = moves + 1
								if mergecon == 16:
									if (count16 > 1):
										count16 = count16 - 2
										count32 = count32 + 1
										score = score + 32
										moves = moves + 1
								if mergecon == 32:
									if (count32 > 1):
										count32 = count32 - 2
										count64 = count64 + 1
										score = score + 64
										moves = moves + 1
								if mergecon == 64:
									if (count64 > 1):
										count64 = count64 - 2
										count128 = count128 + 1
										score = score + 128
										moves = moves + 1
								if mergecon == 128:
									if (count128 > 1):
										count128 = count128 - 2
										count256 = count256 + 1
										score = score + 256
										moves = moves + 1
								if mergecon == 256:
									if (count256 > 1):
										count256 = count256 - 2
										count512 = count512 + 1
										score = score + 512
										moves = moves + 1
								if mergecon == 512:
									if (count512 > 1):
										count512 = count512 - 2
										count1024 = count1024 + 1
										score = score + 1028
										moves = moves + 1
								if mergecon == 1024:
									if (count1024 > 1):
										count1024 = count1024 - 2
										count2048 = count2048 + 1
										score = score + 2048
										moves = moves + 1
								if mergecon == 2048:
									if (count2048 > 1):
										count2048 = count2048 - 2
										count4096 = count4096 + 1
										score = score + 4096
										moves = moves + 1
								if mergecon == 4096:
									if (count4096 > 1):
										count4096 = count4096 - 2
										count8192 = count8192 + 1
										score = score + 8192
										moves = moves + 1
								if mergecon == 8192:
									if (count8192 > 1):
										count8192 = count8192 - 2
										count16384 = count16384 + 1
										score = score + 16384
										moves = moves + 1
								if mergecon == 16384:
									if (count16384 > 1):
										count16384 = count16384 - 2
										count32768 = count32768 + 1
										score = score + 32768
										moves = moves + 1
								if mergecon == 32768:
									if (count32768 > 1):
										count32768 = count32768 - 2
										count65536 = count65536 + 1
										score = score + 63536
										moves = moves + 1
								if mergecon == 65536:
									if (count65536 > 1):
										count65536 = count65536 - 2
										count131072 = count131072 + 1
										score = score + 131072
										moves = moves + 1
								if mergecon == 131072:
									if (count131072 > 1):
										count131072 = count131072 - 2
										count262144 = count262144 + 1
										score = score + 262144
										moves = moves + 1
								if mergecon == 262144:
									if (count262144 > 1):
										count262144 = count262144 - 2
										count524288 = count524288 + 1
										score = score + 524288
										moves = moves + 1
								if mergecon == 524288:
									if (count524288 > 1):
										count524288 = count524288 - 2
										count1048576 = count1048576 + 1
										score = score + 1048576
										moves = moves + 1
								if mergecon == 1048576:
									if (count1048576 > 1):
										count1048576 = count1048576 - 2
										count2097152 = count2097152 + 1	
										score = score + 2097152
										moves = moves + 1
								if mergecon == 2097152:
									if (count2097152 > 1):
										count2097152 = count2097152 - 2
										count4194304 = count4194304 + 1	
										score = score + 2097152
										moves = moves + 1
								if mergecon == 4194304:
									if (count4194304 > 1):
										print ("Error. Cannot merge any higher than that")
								if (score > highScore):
									(highScore == score)
						print ("You win!")
						endgame1 = input("Exiting game, press [ENTER] key to continue")
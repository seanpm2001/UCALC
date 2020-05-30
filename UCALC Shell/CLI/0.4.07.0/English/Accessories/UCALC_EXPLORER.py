uCMainConsole = int(7)
if uCMainConsole == 7:
	if uCMainConsole == 7: # File explorer
		print ("UCALC Explorer") # layer 0
		print ("\n")
		exploreLayer1 = int(1)
		while exploreLayer1 == 1:
			print ("Contents of PY://Main") # layer 1
			print ("[-PA-] {DIR} Modes")
			print ("[-PB-] {DIR} Metadata")
			print ("[-PC-] {DIR} Games")
			print ("[-PD-] {DIR} System")
			explorer = input("PY://")
			if explorer == ("PA"):
				explorerLayer1 = int(0)
				explorerLayer2 = int(1)
				while explorerLayer2 == 1:
					print ("Contents of PY://Modes") # layer 2
					print (" ")
					explorer = input("PY://Modes//")
					if explorer == ("PA1"):
						explorerLayer2 == 0
						explorerLayer1 == 1
			if explorer == ("PB"): # layer 1
				explorerLayer1 = int(0)
				explorerLayer2 = int(1)
				while explorerLayer2 == 1:
					print ("Contents of PY://Metadata") # layer 2
					print (" ")
					explorer = input("PY://Metadata//")
					if explorer == ("PB1"):
						explorerLayer2 == 0
						explorerLayer1 == 1
			if explorer == ("PC"): # layer 1
				explorerLayer1 = int(0)
				explorerLayer2 = int(1)
				while explorerLayer2 == 1:
					print ("Contents of PY://Games") # layer 2
					print ("{PROG} 2048.py                |")
					print ("{PROG} Launch_The_X.py        |")
					print ("{PROG} Rock_Paper_Scissors.py | 2369 Bytes")
					print ("{PROG} Tic-Tac-Toe.y          |")
					print ("{PROG} Pig.py                 |")
					print ("{PROG} PiMun.py               |")
					print ("{PROG} X_cups.py              |")
					print ("{PROG} Yahtzee.py             |")
					print ("{PROG} Solitaire.py           |")
					print ("{PROG} Bingo.py               |")
					print ("{PROG} Minesweeper.py         |")				
					explorer = input("PY://Games//")
					if explorer == ("PC1"):
						explorerLayer2 == 0
						explorerLayer1 == 1
			if explorer == ("PD"):
				explorerLayer1 = int(0)
				explorerLayer2 = int(1)
				while explorerLayer2 == 1:
					print ("Contents of PY://System")
					print ("{PROG} Client.py | +394 KB")
					explorer = input("PY://System//")
					if explorer == ("PD1"):
						explorerLayer2 == 0
						explorerLayer1 == 1
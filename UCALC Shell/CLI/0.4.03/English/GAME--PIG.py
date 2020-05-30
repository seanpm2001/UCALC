					if gameselectID == 14:
						print ("Pig")
						print ("\nHow to play")
						print ("Roll random numbers. Get to the specified amount first")
						print ("\n\nStarting game")
						scoreMax = int(input("Enter a target score: "))
						print ("|---|")
						staGame = input("Press [ENTER] key to start")
						curscore = int(0)
						while (curscore < scoreMax):
							print ("Current score: " + str(curscore))
							print ("Target score: " + str(scoreMax))
							print ("\n==============")
							rollADice = input("Press [ENTER] key to roll your dice")
							ran1 = int(random.randint(1,6))
							curscore =+ ran1
							print ("You Win!")
							exit = input("Press [ENTER] key to quit")
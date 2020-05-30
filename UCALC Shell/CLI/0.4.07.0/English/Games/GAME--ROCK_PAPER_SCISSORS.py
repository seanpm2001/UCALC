					if gameselectID == 12:
						print ("Rock Paper Scissors")
						startGameIn = input("Press [ENTER] key to start")
						print ("You are playing against your calculator. Good luck!")
						calcrand = int(random.randint(1, 3))
						playerpos = int
						print ("Select your position:")
						rocpapsci = int(input("Rock (0) Paper (1) Scissors (2) "))
						calcwins = int(0)
						userwins = int(0)
						game1 = int(1)
						print ("Rock!")
						print ("Paper!")
						print ("Scissors!")
						while game1 == 1:
							if rocpapsci == 0:
								playerpos = str("Rock")
								if rocpapsci == 1:
									playerpos = str("Paper")
								if rocpapsci == 2:
									playerpos = str("Scissors")
								if calcrand == 1:
									if playerpos == ("Rock"):
										print ("It's a tie!")
										print ("Rock vs. Rock")
									if playerpos == ("Paper"):
										print ("Player loses!\nCalculator wins!")
										print ("Rock vs. paper = rock")
										calcwins += 1
									if playerpos == ("Scissors"):
										print ("Player wins!\nCalculator loses!")
										print ("Rock vs. scissors = scissors")
										userwins += 1
								if calcrand == 2:
									if playerpos == ("Rock"):
										print ("Player loses!\nCalculator wins!")
										print ("Rock vs. Paper = Paper")
										calcwins += 1
									if playerpos == ("Paper"):
										print ("It's a tie!")
										print ("Paper vs. paper")
									if playerpos == ("Scissors"):
										print ("Player wins!\nCalculator loses!")
										print ("Paper vs. scissors = scissors")
										userwins += 1
								if calcrand == 3:
									if playerpos == ("Rock"):
										print ("User wins!\bCalculator loses!")
										print ("Rock vs. Scissors = rock")
										userwins  += 1
									if playerpos == ("Paper"):	
										print ("User loses!\nCalculator wins!")
										print ("Paper vs. scissors = scissors")
										calcwins += 1
									if playerpos == ("Scissors"):
										print ("It's a tie!")
										print ("Scissors vs. Scissors")
								print ("Game results:")
								print ("User: " + str(userwins))
								print ("Calc: " + str(calcwins))
								calcrand = int(random.randint(1, 3))
								nexgame = input("Press [ENTER] key to start a new game")
								print ("Select your position:")
								rocpapsci = int(input("Rock (0) Paper (1) Scissors (2) "))
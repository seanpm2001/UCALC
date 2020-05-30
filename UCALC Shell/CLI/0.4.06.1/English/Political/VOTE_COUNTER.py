				if calcIDSes == 54:
					print ("Vote calculator")
					print ("\nSetting up")
					print ("Please set up the candidates")
					print ("Candidate One")
					cand1nam = str(input("Enter Candidate 1's name"))
					cand1pos = str(input("Enter Candidate 1's position (Ex: Governer, President, Mayor, etc"))
					cand1par = str(input("Enter Candidate 1's party"))
					print ("Candidate Two")
					cand2nam = str(input("Enter Candidate 2's name"))
					cand2pos = str(input("Enter Candidate 2's position (Ex: Governer, President, Mayor, etc"))
					cand2par = str(input("Enter Candidate 2's party"))
					votingSes = int(0)
					c1vote = int(0)
					c2vote = int(0)
					while votingSes == 0:
						print ("Candidate positions")
						print (str(cand1nam) + " | " + str(cand1pos) + " | " + str(cand1par) + " | Current vote count: " + str(c1vote))
						print (str(cand2nam) + " | " + str(cand2pos) + " | " + str(cand2par) + " | Current vote count: " + str(c2vote))
						voteTime = int(input("Who do you want to vote for? " + str(cand1nam) + " (0) " + str(cand2nam) + " (1) "))
						if voteTime == 0:
							# (c1vote == c1vote ++ 1)
							c1vote += 1
							print ("You voted for " + str(cand1nam))
						if voteTime == 1:
							# (c2vote == c2vote ++ 1)
							c2vote += 1
							print ("You voted for " + str(cand2nam))
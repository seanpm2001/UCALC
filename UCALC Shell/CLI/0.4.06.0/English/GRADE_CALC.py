				if calcIDSes == 56:
					print ("UCALC Grading Manager")
					print ("\nSelect a grading format:")
					print ("Pass/fail    | Possible grades: P/F                                   | ID: 1")
					print ("Numerals     | Possible grades: 1 2 3 4                               | ID: 2")
					print ("Standard     | Possible grades: A+ A A- B+ B B- C+ C C- D+ D D- F     | ID: 3")
					print ("================================================================================")
					print ("Grading rules ")
					print ("Pass/fail ")
					print ("0-50% = fail | 51%-100% = pass")
					print ("Numerals")
					print ("0-25% = 1 | 26-50% = 2 | 51-75% = 3 | 76-100% = 4 |")
					print ("Standard")
					print ("100% = A+ | 95-99% = A | 90-94% = A- | 85-89% = B+ | 80-84% = B | 77-79% = B- |")
					print ("70-76% = C+ | 65-69% = C | 62-64% = C- | 58-61% = D+ | 55-57% = D | 50-54 = D- | 0-49% = F")
					print ("=================================================================================================")
					gradTypeSe1 = int(input("Enter a grade format ID from above: "))
					if gradTypeSe1 == 1:
						className = str(input("Enter your class's name: "))
						Student1name = str(input("Enter the name of the student: "))
						assign1name = str(input("Enter the name of the assignment: "))
						student1assign1grade = float(input("How many points did the student score? "))
						maxassign1grade = float(input("Enter the maximum score for the assignment"))
						totalScore1 = float(student1assign1grade / maxassign1grade * 100)
						print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
						if totalScore1 > 50:
							gradeSymb1 = str("P")
						if totalScore1 < 50:
							gradeSymb1 = str("F")
						print ("Score: " + str(totalScore1) + " (" + str(gradeSymb1) + ")")
					if gradTypeSe1 == 2:
						className = str(input("Enter your class's name: "))
						Student1name = str(input("Enter the name of the student: "))
						assign1name = str(input("Enter the name of the assignment: "))
						student1assign1grade = float(input("How many points did the student score? "))
						maxassign1grade = float(input("Enter the maximum score for the assignment: "))
						totalScore1 = float(student1assign1grade / maxassign1grade * 100)
						print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
						if totalScore1 > 75:
							gradeSymb1 = str("4")
						if (totalScore1 < 75):
							if (totalScore1 > 50):
								gradeSymb1 = str("3")
						if (totalScore1 < 50):
							if (totalScore1 > 25):
								gradeSymb1 = str("2")
						if (totalScore1 < 25):
							if (totalScore1 > -1):
								gradeSymb1 = str("1")
					if gradTypeSe1 == 3:
						className = str(input("Enter your class's name: "))
						Student1name = str(input("Enter the name of the student: "))
						assign1name = str(input("Enter the name of the assignment: "))
						student1assign1grade = float(input("How many points did the student score? "))
						maxassign1grade = float(input("Enter the maximum score for the assignment: "))
						totalScore1 = float(student1assign1grade / maxassign1grade * 100)
						print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
						if totalScore1 == 100:
							gradeSymb1 = str("A+")
						if (totalScore1 < 95):
							if (totalScore1 > 100):
								gradeSymb1 = str("A")
						if (totalScore1 < 90):
							if (totalScore1 > 95):
								gradeSymb1 = str("A-")
						if (totalScore1 < 85):
							if (totalScore1 > 90):
								gradeSymb1 = str("B+")
						if (totalScore1 < 80):
							if (totalScore1 > 85):
								gradeSymb1 = str("B")
						if (totalScore1 < 77):
							if (totalScore1 > 80):
								gradeSymb1 = str("B-")
						if (totalScore1 < 70):
							if (totalScore1 > 77):
								gradeSymb1 = str("C+")
						if (totalScore1 < 65):
							if (totalScore1 > 70):
								gradeSymb = str("C")
						if (totalScore1 < 62):
							if (totalScore1 > 65):
								gradeSymb1 = str("C-")
						if (totalScore1 < 58):
							if (totalScore1 > 62):
								gradeSymb1 = str("D+")
						if (totalScore1 < 55):
							if (totalScore1 > 58):
								gradeSymb1 = str("D")
						if (totalScore1 < 50):
							if (totalScore1 > 55):
								gradeSymb1 = str("D-")
						if (totalScore1 < 49):
							gradeSymb1 = str("F")
						print ("Score: " + str(totalScore1) + " (" + str(gradeSymb1) + ")")
				if calcIDSes == 57:
					print ("IQ Calculator")
					print ("For more information, please read about IQ under the UCALC documentation")
					noMore = input("Press [ENTER] key to exit")
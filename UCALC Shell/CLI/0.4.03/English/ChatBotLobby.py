# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
print ("Chatbot Lobby")
print ("\nSelect a chatbot: ")
print ("\nSean Myrick      | ID: 1|")
print ("\nBonzi Buddy      | ID: 2|")
print ("\nStephen Hawking  | ID: 3|")
chatID = int(input("Enter a chatbot ID: "))
if (chatID == 1):
	print ("You are now talking with Sean Myrick")
	print ("|--------|")
	print ("This is the start of our conversation! Try to say a greeting")
	print ("SeanM > Hello! ")
	loopforever = int(1)
	while (loopforever == 1):
		console1 = str(input("You > "))
		if (console1 == "Hi" or console1 == "HI" or console1 == "hi" or console1 == "hI" or console1 == "Hello" or console1 == "hello" or console1 == "HELLO" or console1 == "Hello"):
			print ("SeanM > What should I refer to you as? ")
			name1 = str(input("You > "))
			print ("SeanM > Nice to meet you, " + str(name1))
		if (console1 == "Go away" or console1 == "go away" or console1 == "go Away" or console1 == "GO AWAY"):
			print ("SeanM > Wow that's a little rude")
		if (console1 == "LOL" or console1 == "lol" or console1 == "Lol" or console1 == "ROFL" or console1 == "rofl" or console1 == "Rofl" or console1 == "LMAO" or console1 == "lmao" or console1 == "Lmao" or console1 == "LMFAO" or console1 == "lmfao" or console1 == "Lmfao"):
			print ("SeanM > What's so funny?")
			theJoke = str(input("You > "))
			if (theJoke == "you" or "You" or "YOU"):
				print ("SeanM > Oh Ok")
			elif (theJoke == "nothing" or "Nothing" or "NOTHING"):
				print ("SeanM > Hmmmm...")
		if (console1 == "sauce" or console1 == "Sauce" or console1 == "SAUCE"):
			print ("SeanM > SuS?")
			suscon = str(input("You > "))
			if (suscon == "no" or suscon == "No" or suscon == "nO" or suscon == "NO"):
				print ("SeanM > Awwwwwww :(")
			elif (suscon == "Yee" or suscon == "yee" or suscon == "YEE" or suscon == "Yeet" or suscon == "yeet" or suscon == "YEET" or suscon == "yes" or suscon == "Yes" or suscon == "YES"):
				print ("SeanM > SuS") 
		if (console1 == "What" or console1 == "what" or console1 == "WHAT" or console1 == "What?" or console1 == "what?" or console1 == "WHAT?"):
			print ("SeanM > I didn't say anything")
		if (console1 == "test" or console1 == "Test" or console1 == "TEST"):
			print ("SeanM > Your testing has succeeded! I am functional!")
		if (console1 == "69" or console1 == "Rule 34" or console1 == "rule 34" or console1 == "RULE 34"):
			print ("SeanM > Pretty immature, aren't you?")
		if (console1 == "666" or console1 == "satan" or console1 == "Satan" or console1 == "SATAN"):
			print ("SeanM > BEGONE DEMON!")
		if (console1 == "420" or console1 == "Do you smoke weed" or console1 == "do you smoke weed" or console1 == "DO YOU SMOKE WEED" or console1 == "Do you smoke weed?" or console1 == "do you smoke weed?" or console1 == "DO YOU SMOKE WEED?"):
			print ("SeanM > No I do not smoke weed.")
		if (console1 == "Shawn" or console1 == "Shaun" or console1 == "Shean"):
			print ("SeanM > That is not how you spell my name ;-;")
		if (console1 == "$"):
			print ("SeanM > Consider donating to the UCALC organization! This is free software, but we require donations to continue thriving. Every penny counts, even if you were to just donate a penny, you could make a difference. If you enjoy our software, and have a penny or more to spare, consider donating")
		if (console1 == "who are you" or console1 == "WHO ARE YOU" or console1 == "Who are you" or console1 == "Who Are You" or console1 == "who are you" or console1 == "WHO ARE YOU?" or console1 == "Who are you?" or console1 == "Who Are You?"):
			print ("SeanM > I am the founder and creator of UCALC. You are talking to me through the UCALC Chatbot client.")
		if (console1 == "stfu" or console1 == "STFU" or console1 == "Stfu" or console1 == "StfU"):
			print ("SeanM > Fine, fine I will stop, you don't have to be so rude")
			(loopforever == loopforever - 10)
			noMore = input("Press [ENTER] key to quit")
		if (console1 == "bye" or console1 == "Bye" or console1 == "BYE" or console1 == "ByE"):
			print ("SeanM > Goodbye")
			print ("SeanM > Nevermind")
		else:
			print ("SeanM > I am sorry but I don't understand what you said")
if (chatID == 2):
    print ("You are now talking with Bonzi Buddy")
    print ("|--------|")
    print ("This is the start of our conversation! Try to say a greeting")
    more1 = input("Bonzi Buddy > Well, hello there")
    more1 = input("Bonzi Buddy > I don't think we have been properly introduced")
    more1 = input("Bonzi Buddy > I'm Bonzi")
    yourName = str(input("Bonzi Buddy > What is your name? "))
    more1 = input("Bonzi Buddy > Nice to meet you, " + str(yourName))
    more1 = input("Bonzi Buddy > Since this is the first time we have met, I would like to introduce myself")
if (chatID == 3):
	print ("You are now talking with Stephen Hawking")
	print ("|--------|")
	print ("This is the start of our conversation! Try to say a greeting")
	print ("Stephen Hawking > Hello there! ")
	loopforever3 = int(1)
	while (loopforever3 == 1):
		console1 = str(input("You > "))
		if (console1 == "sam" or "Sam" or "SAM"):
			print ("Stephen Hawking > Oh, how could you confuse me with Microsoft sam")
		if (console1 == "Why are you here" or console1 == "why Are You Here" or console1 == "Why Are You Here" or console1 == "why are you here" or console1 == "WHY ARE YOU HERE" or console1 == "Why are you here?" or console1 == "why Are You Here?" or console1 == "Why Are You Here?" or console1 == "why are you here?" or console1 == "WHY ARE YOU HERE?"):
			print ("Stephen Hawking > Sean has assigned me to continue being here to read out my famous quotes and guide users")
		if (console1 == "virus" or console1 == "VIRUS" or console1 == "Virus"):
			print ("Stephen Hawking > Quote currently unavailable ")
		if (console1 == "book" or console1 == "Book" or console1 == "BOOK"):
			print ("Stephen Hawking > The subject of this book is the structure of space-time on length-scales from 10-13cm, the radius of an ")
			print ("Stephen Hawking > elementary particle, up to 1028cm, the radius of the universe. ...we base our treatment on Einstein's ")
			print ("Stephen Hawking > General Theory of Relativity. This theory leads to two remarkable predictions about the universe: ")
			print ("Stephen Hawking > first, that the final fate of massive stars is to collapse behind an event horizon to form a 'black hole'") 
			print ("Stephen Hawking > which will contain a singularity; and secondly, that there is a singularity in our past which constitutes, ")
			print ("Stephen Hawking > in some sense, a beginning to the universe. ")
		if (console1 == "Quantum" or console1 == "quantum" or console1 == "QUANTUM"):
			print ("Stephen Hawking > I regard [the many worlds interpretation] as self-evidently correct. [T.F.: Yet some don't find it evident to ")
			print ("Stephen Hawking > themselves.] Yeah, well, there are some people who spend an awful lot of time talking about the interpretation ")
			print ("Stephen Hawking > of quantum mechanics. My attitude — I would paraphrase Goering—is that when I hear of Schrödinger's cat, ")
			print ("Stephen Hawking > I reach for my gun.")
		if (console1 == "boundary" or console1 == "Boundary" or console1 == "BOUNDARY"):
			print ("Stephen Hawking > Many people would claim that the boundary conditions are not part of physics but belong to metaphysics or religion. They would claim ")
			print ("Stephen Hawking > that nature had complete freedom to start the universe off any way it wanted. That may be so, but it could also have made it evolve ")
			print ("Stephen Hawking > in a completely arbitrary and random manner. Yet all the evidence is that it evolves in a regular way according to certain laws. It ")
			print ("Stephen Hawking > would therefore seem reasonable to suppose that there are also laws governing the boundary conditions.")
		if (console1 == "autism" or console1 == "Autism" or console1 == "AUTISM" or console1 == "Autistic" or console1 == "AUTISTIC" or console1 == "autistic" or console1 == "tourettes" or console1 == "TOURETTES" or console1 == "Tourettes"):
			print ("Stephen Hawking > If you are disabled, it is probably not your fault, but it is no good blaming the world or ")
			print ("Stephen Hawking > expecting it to take pity on you. One has to have a positive attitude and must make the best ")
			print ("Stephen Hawking > of the situation that one finds oneself in; if one is physically disabled, one cannot afford ")
			print ("Stephen Hawking > to be psychologically disabled as well. In my opinion, one should concentrate on activities ")
			print ("Stephen Hawking > in which one's physical disability will not present a serious handicap. I am afraid that ")
			print ("Stephen Hawking > Olympic Games for the disabled do not appeal to me, but it is easy for me to say that ")
			print ("Stephen Hawking > because I never liked athletics anyway. On the other hand, science is a very good area")
			print ("Stephen Hawking > for disabled people because it goes on mainly in the mind. Of course, most kinds of experimental")
			print ("Stephen Hawking > work are probably ruled out for most such people, but theoretical work is almost ideal. My ")
			print ("Stephen Hawking > disabilities have not been a significant handicap in my field, which is theoretical physics. ")
			print ("Stephen Hawking > Indeed, they have helped me in a way by shielding me from lecturing and administrative work ")
			print ("Stephen Hawking > that I would otherwise have been involved in. I have managed, however, only because of the ")
			print ("Stephen Hawking > large amount of help I have received from my wife, children, colleagues and students. I ")
			print ("Stephen Hawking > find that people in general are very ready to help, but you should encourage them to feel ")
			print ("Stephen Hawking > that their efforts to aid you are worthwhile by doing as well as you possibly can. ")
		if (console1 == "goal" or console1 == "Goal" or console1 == "GOAL"):
			print ("Stephen Hawking > My goal is simple. It is a complete understanding of the universe, why it is as it is and why it exists at all.")
		if (console1 == "special boundary" or console1 == "Special boundary" or console1 == "Special Boundary" or console1 == "SPECIAL boundary" or console1 == "special BOUNDARY" or console1 == "SPECIAL BOUNDARY"):
			print ("Stephen Hawking > There ought to be something very special about the boundary conditions of the universe and what can be more special than that there is no boundary?")
		if (console1 == "newton" or console1 == "Newton" or console1 == "NEWTON"):
			print ("Stephen Hawking > Einstein is the only figure in the physical sciences with a stature that can be compared with Newton. Newton is reported to ")
			print ("Stephen Hawking > have said ''If I have seen further than other men, it is because I stood on the shoulders of giants.'' This remark is even ")
			print ("Stephen Hawking > more true of Einstein who stood on the shoulders of Newton. Both Newton and Einstein put forward a theory of mechanics ")
			print ("Stephen Hawking > and a theory of gravity but Einstein was able to base General Relativity on the mathematical theory of curved spaces ")
			print ("Stephen Hawking > that had been constructed by Riemann while Newton had to develop his own mathematical machinery. It is therefore appropriate") 
			print ("Stephen Hawking > to acclaim Newton as the greatest figure in mathematical physics and the Principia is his greatest achievement. ")
		if (console1 == "is god real" or console1 == "Is god real" or console1 == "Is God real" or console1 == "Is God Real" or console1 == "IS GOD REAL" or console1 == "is god real?" or console1 == "Is god real?" or console1 == "Is God real?" or console1 == "Is God Real?" or console1 == "IS GOD REAL?"):
			print ("Stephen Hawking > What I have done is to show that it is possible for the way the universe began to be determined by the laws of science. ")
			print ("Stephen Hawking > In that case, it would not be necessary to appeal to God to decide how the universe began. This doesn't prove that there ")
			print ("Stephen Hawking > is no God, only that God is not necessary. ")
		if (console1 == "Monkey" or console1 == "monkey" or console1 == "MONKEY"):
			print ("Stephen Hawking > We are just an advanced breed of monkeys on a minor planet of a very average star. But we can understand the Universe. ")
			print ("Stephen Hawking > That makes us something very special. ")
		if (console1 == "Enterprise" or console1 == "enterprise" or console1 == "ENTERPRISE"):
			print ("Stephen Hawking > On seeing the Enterprise's warp engine while visiting the set of Star Trek: The Next Generation (where he would")
			print ("Stephen Hawking > briefly play himself in the 1993 episode Descent, Part I), Hawking smiled and said: I'm working on that.")
		if (console1 == "Animal" or console1 == "animal" or console1 == "ANIMAL" or console1 == "animals" or console1 == "Animals" or console1 == "ANIMALS"):
			print ("Stephen Hawking > For millions of years, mankind lived just like the animals. Then something happened which unleashed the power of our ")
			print ("Stephen Hawking > imagination. We learned to talk and we learned to listen. Speech has allowed the communication of ideas, enabling ")
			print ("Stephen Hawking > human beings to work together to build the impossible. Mankind's greatest achievements have come about by talking, ")
			print ("Stephen Hawking > and its greatest failures by not talking. It doesn't have to be like this. Our greatest hopes could become reality in the ")
			print ("Stephen Hawking > future. With the technology at our disposal, the possibilities are unbounded. All we need to do is make sure we keep talking.") 
		#else:
			#print ("Stephen Hawking > Sorry I didn't understand what you said. Please check your syntax and try again")
# noMore = input("An unknown error has occurred. Press [ENTER] key to quit")
'''
Find a way to use all these

Stephen hawking quotes

# On seeing the Enterprise's warp engine while visiting the set of Star Trek: The Next Generation (where he would briefly play himself in the 1993 episode Descent, Part I), Hawking smiled and said: I'm working on that.
# For millions of years, mankind lived just like the animals. Then something happened which unleashed the power of our imagination. We learned to talk and we learned to listen. Speech has allowed the communication of ideas, enabling human beings to work together to build the impossible. Mankind's greatest achievements have come about by talking, and its greatest failures by not talking. It doesn't have to be like this. Our greatest hopes could become reality in the future. With the technology at our disposal, the possibilities are unbounded. All we need to do is make sure we keep talking. 

[discussing Roger Penrose] These lectures have shown very clearly the difference between Roger and me. He's a Platonist and I'm a positivist. He's worried that Schrödinger's cat is in a quantum state, where it is half alive and half dead. He feels that can't correspond to reality. But that doesn't bother me. I don't demand that a theory correspond to reality because I don't know what it is. Reality is not a quality you can test with litmus paper. All I'm concerned with is that the theory should predict the results of measurements. Quantum theory does this very successfully. It predicts that the result of an observation is either that the cat is alive or that it is dead. It is like you can't be slightly pregnant: you either are or you aren't. 

So Einstein was wrong when he said, "God does not play dice." Consideration of black holes suggests, not only that God does play dice, but that he sometimes confuses us by throwing them where they can't be seen.

I don't believe that the ultimate theory will come by steady work along existing lines. We need something new. We can't predict what that will be or when we will find it because if we knew that, we would have found it already! It could come in the next 20 years, but we might never find it. 

The human race is just a chemical scum on a moderate-sized planet, orbiting around a very average star in the outer suburb of one among a hundred billion galaxies. We are so insignificant that I can't believe the whole universe exists for our benefit. That would be like saying that you would disappear if I closed my eyes. 

I think computer viruses should count as life … I think it says something about human nature that the only form of life we have created so far is purely destructive. We've created life in our own image. 

It is not clear that intelligence has any long-term survival value. 

Einstein was confused, not the quantum theory.

All my life, I have been fascinated by the big questions that face us, and have tried to find scientific answers to them. 

Unsourced variant: All of my life, I have been fascinated by the big questions that face us, and have tried to find scientific answers to them. Perhaps that is why I have sold more books on physics than Madonna has on sex. This quote seems to combine the above sentence from Stephen Hawking's Universe with a statement from the Foreword to The Illustrated Brief History of Time: As Nathan Myhrvold of Microsoft (a former post-doc of mine) remarked: I have sold more books on physics than Madonna has on sex.

The world has changed far more in the past 100 years than in any other century in history. The reason is not political or economic but technological — technologies that flowed directly from advances in basic science

One might think this means that imaginary numbers are just a mathematical game having nothing to do with the real world. From the viewpoint of positivist philosophy, however, one cannot determine what is real. All one can do is find which mathematical models describe the universe we live in. It turns out that a mathematical model involving imaginary time predicts not only effects we have already observed but also effects we have not been able to measure yet nevertheless believe in for other reasons. So what is real and what is imaginary? Is the distinction just in our minds?

Although September 11 was horrible, it didn't threaten the survival of the human race, like nuclear weapons do.

I don't think the human race will survive the next thousand years, unless we spread into space. There are too many accidents that can befall life on a single planet. But I'm an optimist. We will reach out to the stars.

We shouldn't be surprised that conditions in the universe are suitable for life, but this is not evidence that the universe was designed to allow for life. We could call order by the name of God, but it would be an impersonal God. There's not much personal about the laws of physics. 

I have no idea. People who boast about their IQ are losers.

Life would be tragic if it weren't funny.

I am discounting reports of UFOs. Why would they appear only to cranks and weirdos? 

My expectations were reduced to zero when I was 21. Everything since then has been a bonus.

The life we have on Earth must have spontaneously generated itself. It must therefore be possible for life to generate spontaneously elsewhere in the universe. 

I'm sorry to disappoint science fiction fans, but if information is preserved, there is no possibility of using black holes to travel to other universes. If you jump into a black hole, your mass energy will be returned to our universe but in a mangled form which contains the information about what you were like but in a state where it can not be easily recognized. It is like burning an encyclopedia. Information is not lost, if one keeps the smoke and the ashes. But it is difficult to read. In practice, it would be too difficult to re-build a macroscopic object like an encyclopedia that fell inside a black hole from information in the radiation, but the information preserving result is important for microscopic processes involving virtual black holes. 

Evolution has ensured that our brains just aren't equipped to visualise 11 dimensions directly. However, from a purely mathematical point of view it's just as easy to think in 11 dimensions, as it is to think in three or four. 

I think that it's important for scientists to explain their work, particularly in cosmology. This now answers many questions once asked of religion. 

It is a waste of time to be angry about my disability. One has to get on with life and I haven't done badly. People won't have time for you if you are always angry or complaining.

Equations are just the boring part of mathematics. I attempt to see things in terms of geometry.

The victim should have the right to end his life, if he wants. But I think it would be a great mistake. However bad life may seem, there is always something you can do, and succeed at. While there's life, there is hope.

The danger is that global warming may become self-sustaining, if it has not done so already. The melting of the Arctic and Antarctic ice caps reduces the fraction of solar energy reflected back into space, and so increases the temperature further. Climate change may kill off the Amazon and other rain forests, and so eliminate once one of the main ways in which carbon dioxide is removed from the atmosphere. The rise in sea temperature may trigger the release of large quantities of carbon dioxide, trapped as hydrides on the ocean floor. Both these phenomena would increase the greenhouse effect, and so global warming further. We have to reverse global warming urgently, if we still can. 

As scientists, we understand the dangers of nuclear weapons and their devastating effects, and we are learning how human activities and technologies are affecting climate systems in ways that may forever change life on Earth. As citizens of the world, we have a duty to alert the public to the unnecessary risks that we live with every day, and to the perils we foresee if governments and societies do not take action now to render nuclear weapons obsolete and to prevent further climate change... There’s a realization that we are changing our climate for the worse. That would have catastrophic effects. Although the threat is not as dire as that of nuclear weapons right now, in the long term we are looking at a serious threat. 

The downside of my celebrity is that I cannot go anywhere in the world without being recognized. It is not enough for me to wear dark sunglasses and a wig. The wheelchair gives me away.

I'm not religious in the normal sense. I believe the universe is governed by the laws of science. The laws may have been decreed by God, but God does not intervene to break the laws. 

The zero-G part was wonderful and the higher-G part was no problem. I could have gone on and on. Space, here I come! 

In a world that is in chaos politically, socially and environmentally, how can the human race sustain another 100 years? 

To confine our attention to terrestrial matters would be to limit the human spirit.

There is a fundamental difference between religion, which is based on authority and science, which is based on observation and reason. Science will win, because it works.

I have lived with the prospect of an early death for the last 49 years. I'm not afraid of death, but I'm in no hurry to die. I have so much I want to do first ... I regard the brain as a computer which will stop working when its components fail. There is no heaven or afterlife for broken down computers; that is a fairy story for people afraid of the dark. 

We should seek the greatest value of our action. 

Science predicts that many different kinds of universe will be spontaneously created out of nothing. It is a matter of chance which we are in.

I used to think that information was destroyed in black holes. But the AdS/CFT correspondence led me to change my mind. This was my biggest blunder, or at least my biggest blunder in science. 

I believe that disabled people should concentrate on things that their handicap doesn’t prevent them from doing and not regret those they can’t do … I visited the Soviet Union seven times. The first time I went with a student party in which one member, a Baptist, wished to distribute Russian-language Bibles and asked us to smuggle them in. We managed this undetected, but by the time we were on our way out the authorities had discovered what we had done and detained us for a while. However, to charge us with smuggling Bibles would have caused an international incident and unfavorable publicity, so they let us go after a few hours.

The development of full artificial intelligence could spell the end of the human race. We cannot quite know what will happen if a machine exceeds our own intelligence, so we can't know if we'll be infinitely helped by it, or ignored by it and sidelined, or conceivably destroyed by it. 

If machines produce everything we need, the outcome will depend on how things are distributed. Everyone can enjoy a life of luxurious leisure if the machine-produced wealth is shared, or most people can end up miserably poor if the machine-owners successfully lobby against wealth redistribution. So far, the trend seems to be toward the second option, with technology driving ever-increasing inequality. 

Someone told me that each equation I included in the book would halve the sales. I therefore resolved not to have any equations at all. In the end, however, I did put in one equation, Einstein's famous equation, E = m c 2 {\displaystyle E=mc^{2}} {\displaystyle E=mc^{2}}. I hope that this will not scare off half of my potential readers.

Any physical theory is always provisional, in the sense that it is only a hypothesis: you can never prove it. No matter how many times the results of experiments agree with some theory, you can never be sure that the next time the result will not contradict the theory. On the other hand, you can disprove a theory by finding even a single observation that disagrees with the predictions of the theory. As philosopher of science Karl Popper has emphasized, a good theory is characterized by the fact that it makes a number of predictions that could in principle be disproved or falsified by observation. Each time new experiments are observed to agree with the predictions the theory survives, and our confidence in it is increased; but if ever a new observation is found to disagree, we have to abandon or modify the theory.

It has certainly been true in the past that what we call intelligence and scientific discovery have conveyed a survival advantage. It is not so clear that this is still the case: our scientific discoveries may well destroy us all, and even if they don’t, a complete unified theory may not make much difference to our chances of survival. However, provided the universe has evolved in a regular way, we might expect that the reasoning abilities that natural selection has given us would be valid also in our search for a complete unified theory, and so would not lead us to the wrong conclusions. 

Bodies like the earth are not made to move on curved orbits by a force called gravity; instead, they follow the nearest thing to a straight path in a curved space, which is called a geodesic. A geodesic is the shortest (or longest) path between two nearby points. 

The whole history of science has been the gradual realization that events do not happen in an arbitrary manner, but that they reflect a certain underlying order, which may or may not be divinely inspired.

Galileo, perhaps more than any other single person, was responsible for the birth of modern science.

One could say: "The boundary condition of the universe is that it has no boundary." The universe would be completely self-contained and not affected by anything outside itself. It would neither be created nor destroyed. It would just BE. 

Just like a computer, we must remember things in the order in which entropy increases. This makes the second law of thermodynamics almost trivial. Disorder increases with time because we measure time in the direction in which disorder increases. You can’t have a safer bet than that! 

As I shall describe, the prospects for finding such a theory seem to be much better now because we know so much more about the universe. But we must beware of overconfidence - we have had false dawns before! At the beginning of this century, for example, it was thought that everything could be explained in terms of the properties of continuous matter, such as elasticity and heat conduction. The discovery of atomic structure and the uncertainty principle put an emphatic end to that. Then again, in 1928, physicist and Nobel Prize winner Max Born told a group of visitors to Gottingen University, "Physics, as we know it, will be over in six months." His confidence was based on the recent discovery by Dirac of the equation that governed the electron. It was thought that a similar equation would govern the proton, which was the only other particle known at the time, and that would be the end of theoretical physics. However, the discovery of the neutron and of nuclear forces knocked that one on the head too. Having said this, I still believe there are grounds for cautious optimism that we may now be near the end of the search for the ultimate laws of nature.

Maybe that is our mistake: maybe there are no particle positions and velocities, but only waves. It is just that we try to fit the waves to our preconceived ideas of positions and velocities.The resulting mismatch is the cause of the apparent unpredictability. 

Even if there is only one possible unified theory, it is just a set of rules and equations. What is it that breathes fire into the equations and makes a universe for them to describe? The usual approach of science of constructing a mathematical model cannot answer the questions of why there should be a universe for the model to describe. Why does the universe go to all the bother of existing? 

The ultimate objective test of free will would seem to be: Can one predict the behavior of the organism? If one can, then it clearly doesn't have free will but is predetermined. On the other hand, if one cannot predict the behavior, one could take that as an operational definition that the organism has free will … The real reason why we cannot predict human behavior is that it is just too difficult. We already know the basic physical laws that govern the activity of the brain, and they are comparatively simple. But it is just too hard to solve the equations when there are more than a few particles involved … So although we know the fundamental equations that govern the brain, we are quite unable to use them to predict human behavior. This situation arises in science whenever we deal with the macroscopic system, because the number of particles is always too large for there to be any chance of solving the fundamental equations. What we do instead is use effective theories. These are approximations in which the very large number of particles are replaced by a few quantities. An example is fluid mechanics … I want to suggest that the concept of free will and moral responsibility for our actions are really an effective theory in the sense of fluid mechanics. It may be that everything we do is determined by some grand unified theory. If that theory has determined that we shall die by hanging, then we shall not drown. But you would have to be awfully sure that you were destined for the gallows to put to sea in a small boat during a storm. I have noticed that even people who claim everything is predetermined and that we can do nothing to change it, look before they cross the road. … One cannot base one's conduct on the idea that everything is determined, because one does not know what has been determined. Instead, one has to adopt the effective theory that one has free will and that one is responsible for one's actions. This theory is not very good at predicting human behavior, but we adopt it because there is no chance of solving the equations arising from the fundamental laws. There is also a Darwinian reason that we believe in free will: A society in which the individual feels responsible for his or her actions is more likely to work together and survive to spread its values. 

    When I gave a lecture in Japan, I was asked not to mention the possible re-collapse of the universe, because it might affect the stock market. However, I can re-assure anyone who is nervous about their investments that it is a bit early to sell: even if the universe does come to an end, it won't be for at least twenty billion years. By that time, maybe the GATT trade agreement will have come into effect.

    The Steady State theory was what Karl Popper would call a good scientific theory: it made definite predictions, which could be tested by observation, and possibly falsified. Unfortunately for the theory, they were falsified.

    To show this diagram properly, I would really need a four dimensional screen. However, because of government cuts, we could manage to provide only a two dimensional screen.

    The universe would have expanded in a smooth way from a single point. As it expanded, it would have borrowed energy from the gravitational field, to create matter. As any economist could have predicted, the result of all that borrowing, was inflation. The universe expanded and borrowed at an ever-increasing rate. Fortunately, the debt of gravitational energy will not have to be repaid until the end of the universe.
	
	    When I gave a lecture in Japan, I was asked not to mention the possible re-collapse of the universe, because it might affect the stock market. However, I can re-assure anyone who is nervous about their investments that it is a bit early to sell: even if the universe does come to an end, it won't be for at least twenty billion years. By that time, maybe the GATT trade agreement will have come into effect.

    The Steady State theory was what Karl Popper would call a good scientific theory: it made definite predictions, which could be tested by observation, and possibly falsified. Unfortunately for the theory, they were falsified.

    To show this diagram properly, I would really need a four dimensional screen. However, because of government cuts, we could manage to provide only a two dimensional screen.

    The universe would have expanded in a smooth way from a single point. As it expanded, it would have borrowed energy from the gravitational field, to create matter. As any economist could have predicted, the result of all that borrowing, was inflation. The universe expanded and borrowed at an ever-increasing rate. Fortunately, the debt of gravitational energy will not have to be repaid until the end of the universe.
	
We hold these truths to be self-evident that all P-brains are created equal.\

Mathematics is more than a tool and language for science. It is also an end in itself, and as such, it has, over the centuries, affected our worldview in its own right. 

    So next time someone complains that you have made a mistake, tell him that may be a good thing. Because without imperfection, neither you nor I would exist.

    If aliens visit us, the outcome would be much as when Columbus landed in America, which didn't turn out well for the Native Americans. … We only have to look at ourselves to see how intelligent life might develop into something we wouldn't want to meet.

Because there is a law such as gravity, the universe can and will create itself from nothing. Spontaneous creation is the reason there is something rather than nothing, why the universe exists, why we exist. It is not necessary to invoke God to light the blue touch paper and set the universe going.

We are each free to believe what we want and it is my view that the simplest explanation is there is no God. No one created the universe and no one directs our fate. This leads me to a profound realization. There is probably no heaven, and no afterlife either. We have this one life to appreciate the grand design of the universe, and for that, I am extremely grateful.

We are all different — but we share the same human spirit. Perhaps it's human nature that we adapt — and survive.

'''

'''
used quotes

12/11/2018 5:15 am Pacific Time Zone
# The subject of this book is the structure of space-time on length-scales from 10-13cm, the radius of an elementary particle, up to 1028cm, the radius of the universe. ...we base our treatment on Einstein's General Theory of Relativity. This theory leads to two remarkable predictions about the universe: first, that the final fate of massive stars is to collapse behind an event horizon to form a 'black hole' which will contain a singularity; and secondly, that there is a singularity in our past which constitutes, in some sense, a beginning to the universe. 
# I regard [the many worlds interpretation] as self-evidently correct. [T.F.: Yet some don't find it evident to themselves.] Yeah, well, there are some people who spend an awful lot of time talking about the interpretation of quantum mechanics. My attitude — I would paraphrase Goering—is that when I hear of Schrödinger's cat, I reach for my gun.
#  Many people would claim that the boundary conditions are not part of physics but belong to metaphysics or religion. They would claim that nature had complete freedom to start the universe off any way it wanted. That may be so, but it could also have made it evolve in a completely arbitrary and random manner. Yet all the evidence is that it evolves in a regular way according to certain laws. It would therefore seem reasonable to suppose that there are also laws governing the boundary conditions.
# If you are disabled, it is probably not your fault, but it is no good blaming the world or expecting it to take pity on you. One has to have a positive attitude and must make the best of the situation that one finds oneself in; if one is physically disabled, one cannot afford to be psychologically disabled as well. In my opinion, one should concentrate on activities in which one's physical disability will not present a serious handicap. I am afraid that Olympic Games for the disabled do not appeal to me, but it is easy for me to say that because I never liked athletics anyway. On the other hand, science is a very good area for disabled people because it goes on mainly in the mind. Of course, most kinds of experimental work are probably ruled out for most such people, but theoretical work is almost ideal. My disabilities have not been a significant handicap in my field, which is theoretical physics. Indeed, they have helped me in a way by shielding me from lecturing and administrative work that I would otherwise have been involved in. I have managed, however, only because of the large amount of help I have received from my wife, children, colleagues and students. I find that people in general are very ready to help, but you should encourage them to feel that their efforts to aid you are worthwhile by doing as well as you possibly can. 
# My goal is simple. It is a complete understanding of the universe, why it is as it is and why it exists at all.
# There ought to be something very special about the boundary conditions of the universe and what can be more special than that there is no boundary?
# Einstein is the only figure in the physical sciences with a stature that can be compared with Newton. Newton is reported to have said "If I have seen further than other men, it is because I stood on the shoulders of giants." This remark is even more true of Einstein who stood on the shoulders of Newton. Both Newton and Einstein put forward a theory of mechanics and a theory of gravity but Einstein was able to base General Relativity on the mathematical theory of curved spaces that had been constructed by Riemann while Newton had to develop his own mathematical machinery. It is therefore appropriate to acclaim Newton as the greatest figure in mathematical physics and the Principia is his greatest achievement. 
# What I have done is to show that it is possible for the way the universe began to be determined by the laws of science. In that case, it would not be necessary to appeal to God to decide how the universe began. This doesn't prove that there is no God, only that God is not necessary. 
# We are just an advanced breed of monkeys on a minor planet of a very average star. But we can understand the Universe. That makes us something very special. 
'''
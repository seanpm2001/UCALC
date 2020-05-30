print ("The periodic table of elements")
print (" ")
enterToEnter = input("Press [ENTER] key to start")
loopForever = int(1)
while (loopForever == 1):
	print ("============================================================================\\")
	print ("Note: Table ID is the atomic number | Periodic table tool for UCALC V0.18   |")
	print ("============================================================================|")
	print ("| | 01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  |")
	print ("                                                                            |")
	print (" 1  H   [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] HE  |")
	print ("    1                                                                   2   |")
	print ("                                                                            |")
	print (" 2 LI   BE  [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] B   C   N   O   F   NE  |")
	print ("   3    4                                           5   6   7   8   9   10  |")
	print ("                                                                            |")
	print (" 3 NA   MG  [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] AL  Si  P   S   CL  AR  |")
	print ("   11   12                                          13  14  15  16  17  18  |")
	print ("                                                                            |")
	print (" 4 K    CA  SC  Ti  V   CR  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  |")
	print ("   19   20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  |")
	print ("                                                                            |")
	print (" 5 RB   SR  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe  |")
	print ("   37   38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  |")
	print ("                                                                            |")
	print (" 6 CS   BA  LA  Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  |")
	print ("   55   56  57  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  |")
	print ("                                                                            |")
	print (" 7 FR   RA  AC  RF  DB  SG  BH  HS  MT  DS  RG  CN  NH  FL  MC  LV  TS  OG  |")
	print ("   87   88  89  104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 |")
	print ("                                                                            |")
	print (" * [x]  [x] [x] Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  [x] |")
	print ("                58  59  60  61  62  63  64  65  66  67  68  69  70  71      |")
	print ("                                                                            |")
	print (" * [x]  [x] [x] Th  Pa  U   Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr  [x] |")
	print ("                90  91  92  93  94  95  96  97  98  99  100 101 102 103     |")
	print ("                                                                            |")
	print ("============================================================================|")
	print ("| 118 elements | Periodic Table Of Elements December 2018 edition | TABLE   |")
	print ("============================================================================/")
	print ("Type in an ID to start, either the number or the atomic symbol (example: FE)")
	print ("Type 'exit' to quit")
	PTOECon = str(input(">> "))
	if (PTOECon == "h" or PTOECon == "H" or PTOECon == "1"):
		print ("[H]")
		print ("Hydrogen")
		print ("Table ID: 1")
		print ("Excerpt from https://www.wikipedia.org/wiki/Hydrogen")
		print ("Hydrogen is a chemical element with symbol H and atomic number 1. With a standard atomic weight of 1.008, hydrogen is the lightest element on the periodic table. Its monatomic form (H) is the most abundant chemical substance in the Universe, constituting roughly 75% of all baryonic mass.[7][note 1] Non-remnant stars are mainly composed of hydrogen in the plasma state. The most common isotope of hydrogen, termed protium (name rarely used, symbol 1H), has one proton and no neutrons. ")
	if (PTOECon == "he" or PTOECon == "HE" or PTOECon == "He" or PTOECon == "2"):
		print ("[HE]")
		print ("Helium")
		print ("Table ID: 2")
		print ("Excerpt from https://www.wikipedia.org/wiki/Helium")
		print ("Helium (from Greek: ἥλιος, translit. Helios, lit. 'Sun') is a chemical element with symbol He and atomic number 2. It is a colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas group in the periodic table. Its boiling point is the lowest among all the elements. After hydrogen, helium is the second lightest and second most abundant element in the observable universe, being present at about 24% of the total elemental mass, which is more than 12 times the mass of all the heavier elements combined. Its abundance is similar to this figure in the Sun and in Jupiter. This is due to the very high nuclear binding energy (per nucleon) of helium-4 with respect to the next three elements after helium. This helium-4 binding energy also accounts for why it is a product of both nuclear fusion and radioactive decay. Most helium in the universe is helium-4, the vast majority of which was formed during the Big Bang. Large amounts of new helium are being created by nuclear fusion of hydrogen in stars. ")
	if (PTOECon == "li" or PTOECon == "LI" or PTOECon == "Li" or PTOECon == "3"):
		print ("[LI]")
		print ("Lithium")
		print ("Table ID: 3")
		print ("Excerpt from https://www.wikipedia.org/wiki/Lithium")
		print ("Lithium (from Greek: λίθος, translit. lithos, lit. 'stone') is a chemical element with symbol Li and atomic number 3. It is a soft, silvery-white alkali metal. Under standard conditions, it is the lightest metal and the lightest solid element. Like all alkali metals, lithium is highly reactive and flammable, and is stored in mineral oil. When cut, it exhibits a metallic luster, but moist air corrodes it quickly to a dull silvery gray, then black tarnish. It never occurs freely in nature, but only in (usually ionic) compounds, such as pegmatitic minerals which were once the main source of lithium. Due to its solubility as an ion, it is present in ocean water and is commonly obtained from brines. Lithium metal is isolated electrolytically from a mixture of lithium chloride and potassium chloride. ")
	if (PTOECon == "be" or PTOECon == "BE" or PTOECon == "Be" or PTOECon == "4"):
		print ("[BE]")
		print ("Beryllium")
		print ("Table ID: 4")
		print ("Excerpt from https://www.wikipedia.org/wiki/Beryllium")
		print ("Beryllium is a chemical element with symbol Be and atomic number 4. It is a relatively rare element in the universe, usually occurring as a product of the spallation of larger atomic nuclei that have collided with cosmic rays. Within the cores of stars beryllium is depleted as it is fused and creates larger elements. It is a divalent element which occurs naturally only in combination with other elements in minerals. Notable gemstones which contain beryllium include beryl (aquamarine, emerald) and chrysoberyl. As a free element it is a steel-gray, strong, lightweight and brittle alkaline earth metal. ")
	if (PTOECon == "b" or PTOECon == "B" or PTOECon == "5"):
		print ("[B]")
		print ("Boron")
		print ("Table ID: 5")
		print ("Excerpt from https://www.wikipedia.org/wiki/Boron")
		print ("Boron is a chemical element with symbol B and atomic number 5. Produced entirely by cosmic ray spallation and supernovae and not by stellar nucleosynthesis, it is a low-abundance element in the Solar system and in the Earth's crust.[12] Boron is concentrated on Earth by the water-solubility of its more common naturally occurring compounds, the borate minerals. These are mined industrially as evaporites, such as borax and kernite. The largest known boron deposits are in Turkey, the largest producer of boron minerals. ")
	if (PTOECon == "c" or PTOECon == "C" or PTOECon == "6"):
		print ("[C]")
		print ("Carbon")
		print ("Table ID: 6")
		print ("Excerpt from https://www.wikipedia.org/wiki/Carbon")
		print ("Carbon (from Latin: carbo ''coal'') is a chemical element with symbol C and atomic number 6. It is nonmetallic and tetravalent—making four electrons available to form covalent chemical bonds. It belongs to group 14 of the periodic table.[16] Three isotopes occur naturally, 12C and 13C being stable, while 14C is a radionuclide, decaying with a half-life of about 5,730 years.[17] Carbon is one of the few elements known since antiquity.[18] ")
	if (PTOECon == "n" or PTOECon == "N" or PTOECon == "7"):
		print ("[N]")
		print ("Nitrogen")
		print ("Table ID: 7")
		print ("Excerpt from https://www.wikipedia.org/wiki/Nitrogen")
		print ("Nitrogen is a chemical element with symbol N and atomic number 7. It was first discovered and isolated by Scottish physician Daniel Rutherford in 1772. Although Carl Wilhelm Scheele and Henry Cavendish had independently done so at about the same time, Rutherford is generally accorded the credit because his work was published first. The name nitrogène was suggested by French chemist Jean-Antoine-Claude Chaptal in 1790, when it was found that nitrogen was present in nitric acid and nitrates. Antoine Lavoisier suggested instead the name azote, from the Greek άζωτικός ''no life'', as it is an asphyxiant gas; this name is instead used in many languages, such as French, Russian, and Turkish, and appears in the English names of some nitrogen compounds such as hydrazine, azides and azo compounds. ")
	if (PTOECon == "o" or PTOECon == "O" or PTOECon == "8"):
		print ("[O]")
		print ("Oxygen")
		print ("Table ID: 8")
		print ("Excerpt from https://www.wikipedia.org/wiki/Oxygen")
		print ("Oxygen is a chemical element with symbol O and atomic number 8. It is a member of the chalcogen group on the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.8% of the Earth's atmosphere. As compounds including oxides, the element makes up almost half of the Earth's crust. ")
	if (PTOECon == "f" or PTOECon == "F" or PTOECon == "9"):
		print ("[F]")
		print ("Fluorine")
		print ("Table ID: 9")
		print ("Excerpt from https://www.wikipedia.org/wiki/Fluorine")
		print ("Fluorine is a chemical element with symbol F and atomic number 9. It is the lightest halogen and exists as a highly toxic pale yellow diatomic gas at standard conditions. As the most electronegative element, it is extremely reactive, as it reacts with almost all other elements, except for helium and neon. ")
	if (PTOECon == "ne" or PTOECon == "NE" or PTOECon == "Ne" or PTOECon == "10"):
		print ("[NE]")
		print ("Neon")
		print ("Table ID: 10")
		print ("Excerpt from https://www.wikipedia.org/wiki/Neon")
		print ("Neon is a chemical element with symbol Ne and atomic number 10. It is a noble gas.[10] Neon is a colorless, odorless, inert monatomic gas under standard conditions, with about two-thirds the density of air. It was discovered (along with krypton and xenon) in 1898 as one of the three residual rare inert elements remaining in dry air, after nitrogen, oxygen, argon and carbon dioxide were removed. Neon was the second of these three rare gases to be discovered and was immediately recognized as a new element from its bright red emission spectrum. The name neon is derived from the Greek word, νέον, neuter singular form of νέος (neos), meaning new. Neon is chemically inert, and no uncharged neon compounds are known. The compounds of neon currently known include ionic molecules, molecules held together by van der Waals forces and clathrates. ")
	if (PTOECon == "na" or PTOECon == "NA" or PTOECon == "Na" or PTOECon == "11"):
		print ("[NA]")
		print ("Sodium")
		print ("Table ID: 11")
		print ("Excerpt from https://www.wikipedia.org/wiki/Sodium")
		print ("Sodium is a chemical element with symbol Na (from Latin natrium) and atomic number 11. It is a soft, silvery-white, highly reactive metal. Sodium is an alkali metal, being in group 1 of the periodic table, because it has a single electron in its outer shell that it readily donates, creating a positively charged ion—the Na+ cation. Its only stable isotope is 23Na. The free metal does not occur in nature, but must be prepared from compounds. Sodium is the sixth most abundant element in the Earth's crust and exists in numerous minerals such as feldspars, sodalite, and rock salt (NaCl). Many salts of sodium are highly water-soluble: sodium ions have been leached by the action of water from the Earth's minerals over eons, and thus sodium and chlorine are the most common dissolved elements by weight in the oceans. ")
	if (PTOECon == "mg" or PTOECon == "MG" or PTOECon == "Mg" or PTOECon == "12"):
		print ("[MG]")
		print ("Magnesium")
		print ("Table ID: 12")
		print ("Excerpt from https://www.wikipedia.org/wiki/Magnesium")
		print ("Magnesium is a chemical element with symbol Mg and atomic number 12. It is a shiny gray solid which bears a close physical resemblance to the other five elements in the second column (group 2, or alkaline earth metals) of the periodic table: all group 2 elements have the same electron configuration in the outer electron shell and a similar crystal structure. ")
	if (PTOECon == "al" or PTOECon == "AL" or PTOECon == "Al" or PTOECon == "13"):
		print ("[AL]")
		print ("Alluminium")
		print ("Table ID: 13")
		print ("Excerpt from https://www.wikipedia.org/wiki/Alluminium")
		print ("Aluminium or aluminum is a chemical element with symbol Al and atomic number 13. It is a silvery-white, soft, nonmagnetic and ductile metal in the boron group. By mass, aluminium makes up about 8% of the Earth's crust; it is the third most abundant element after oxygen and silicon and the most abundant metal in the crust, though it is less common in the mantle below. The chief ore of aluminium is bauxite. Aluminium metal is so chemically reactive that native specimens are rare and limited to extreme reducing environments. Instead, it is found combined in over 270 different minerals.[7] ")
	if (PTOECon == "si" or PTOECon == "SI" or PTOECon == "Si" or PTOECon == "14"):
		print ("[SI]")
		print ("Silicon")
		print ("Table ID: 14")
		print ("Excerpt from https://www.wikipedia.org/wiki/Silicon")
		print ("Silicon is a chemical element with symbol Si and atomic number 14. It is a hard and brittle crystalline solid with a blue-grey metallic lustre; and it is a tetravalent metalloid and semiconductor. It is a member of group 14 in the periodic table: carbon is above it; and germanium, tin, and lead are below it. It is relatively unreactive. Because of its large chemical affinity for oxygen, it was not until 1823 that Jöns Jakob Berzelius was first able to prepare it and characterize it in pure form. Its melting and boiling points of 1414 °C and 3265 °C respectively are the second-highest among all the metalloids and nonmetals, being only surpassed by boron. Silicon is the eighth most common element in the universe by mass, but very rarely occurs as the pure element in the Earth's crust. It is most widely distributed in dusts, sands, planetoids, and planets as various forms of silicon dioxide (silica) or silicates. More than 90% of the Earth's crust is composed of silicate minerals, making silicon the second most abundant element in the Earth's crust (about 28% by mass) after oxygen. ")
	if (PTOECon == "p" or PTOECon == "P" or PTOECon == "15"):
		print ("[P]")
		print ("Phosphorus")
		print ("Table ID: 15")
		print ("Excerpt from https://www.wikipedia.org/wiki/Phosphorus")
		print ("Phosphorus is a chemical element with symbol P and atomic number 15. Elemental phosphorus exists in two major forms, white phosphorus and red phosphorus, but because it is highly reactive, phosphorus is never found as a free element on Earth. It has a concentration in the Earth's crust of about one gram per kilogram (compare copper at about 0.06 grams). With few exceptions, minerals containing phosphorus are in the maximally oxidized state as inorganic phosphate rocks. ")
	if (PTOECon == "s" or PTOECon == "S" or PTOECon == "16"):
		print ("[S]")
		print ("Sulfur")
		print ("Table ID: 16")
		print ("Excerpt from https://www.wikipedia.org/wiki/Sulfur")
		print ("Sulfur or sulphur is a chemical element with symbol S and atomic number 16. It is abundant, multivalent, and nonmetallic. Under normal conditions, sulfur atoms form cyclic octatomic molecules with a chemical formula S8. Elemental sulfur is a bright yellow crystalline solid at room temperature. Chemically, sulfur reacts with all elements except for gold, platinum, iridium, tellurium, and the noble gases. ")
	if (PTOECon == "cl" or PTOECon == "CL" or PTOECon == "Cl" or PTOECon == "17"):
		print ("[CL]")
		print ("Chlorine")
		print ("Table ID: 17")
		print ("Excerpt from https://www.wikipedia.org/wiki/Chlorine")
		print ("Chlorine is a chemical element with symbol Cl and atomic number 17. The second-lightest of the halogens, it appears between fluorine and bromine in the periodic table and its properties are mostly intermediate between them. Chlorine is a yellow-green gas at room temperature. It is an extremely reactive element and a strong oxidising agent: among the elements, it has the highest electron affinity and the third-highest electronegativity, behind only oxygen and fluorine. ")
	if (PTOECon == "ar" or PTOECon == "AR" or PTOECon == "Ar" or PTOECon == "18"):
		print ("[AR]")
		print ("Argon")
		print ("Table ID: 18")
		print ("Excerpt from https://www.wikipedia.org/wiki/Argon")
		print ("Argon is a chemical element with symbol Ar and atomic number 18. It is in group 18 of the periodic table and is a noble gas.[5] Argon is the third-most abundant gas in the Earth's atmosphere, at 0.934% (9340 ppmv). It is more than twice as abundant as water vapor (which averages about 4000 ppmv, but varies greatly), 23 times as abundant as carbon dioxide (400 ppmv), and more than 500 times as abundant as neon (18 ppmv). Argon is the most abundant noble gas in Earth's crust, comprising 0.00015% of the crust. ")
	if (PTOECon == "k" or PTOECon == "K" or PTOECon == "19"):
		print ("[K]")
		print ("Potassium")
		print ("Table ID: 19")
		print ("Excerpt from https://www.wikipedia.org/wiki/Potassium")
		print ("Potassium is a chemical element with symbol K (from Neo-Latin kalium) and atomic number 19. It was first isolated from potash, the ashes of plants, from which its name derives. In the periodic table, potassium is one of the alkali metals. All of the alkali metals have a single valence electron in the outer electron shell, which is easily removed to create an ion with a positive charge – a cation, which combines with anions to form salts. Potassium in nature occurs only in ionic salts. Elemental potassium is a soft silvery-white alkali metal that oxidizes rapidly in air and reacts vigorously with water, generating sufficient heat to ignite hydrogen emitted in the reaction, and burning with a lilac-colored flame. It is found dissolved in sea water (which is 0.04% potassium by weight[5][6]), and is part of many minerals. ")
	if (PTOECon == "ca" or PTOECon == "CA" or PTOECon == "Ca" or PTOECon == "20"):
		print ("[CA]")
		print ("Calcium")
		print ("Table ID: 20")
		print ("Excerpt from https://www.wikipedia.org/wiki/Calcium")
		print ("Calcium is a chemical element with symbol Ca and atomic number 20. As an alkaline earth metal, calcium is a reactive metal that forms a dark oxide-nitride layer when exposed to air. Its physical and chemical properties are most similar to its heavier homologues strontium and barium. It is the fifth most abundant element in Earth's crust and the third most abundant metal, after iron and aluminium. The most common calcium compound on Earth is calcium carbonate, found in limestone and the fossilised remnants of early sea life; gypsum, anhydrite, fluorite, and apatite are also sources of calcium. The name derives from Latin calx ''lime'', which was obtained from heating limestone. ")
	if (PTOECon == "sc" or PTOECon == "SC" or PTOECon == "Sc" or PTOECon == "21"):
		print ("[SC]")
		print ("Scandium")
		print ("Table ID: 21")
		print ("Excerpt from https://www.wikipedia.org/wiki/Scandium")
		print ("Scandium is a chemical element with symbol Sc and atomic number 21. A silvery-white metallic d-block element, it has historically been classified as a rare-earth element,[5] together with yttrium and the lanthanides. It was discovered in 1879 by spectral analysis of the minerals euxenite and gadolinite from Scandinavia")
	if (PTOECon == "ti" or PTOECon == "TI" or PTOECon == "Ti" or PTOECon == "22"):
		print ("[TI]")
		print ("Titanium")
		print ("Table ID: 22")
		print ("Excerpt from https://www.wikipedia.org/wiki/Titanium")
		print ("Titanium is a chemical element with symbol Ti and atomic number 22. It is a lustrous transition metal with a silver color, low density, and high strength. Titanium is resistant to corrosion in sea water, aqua regia, and chlorine. ")
	if (PTOECon == "v" or PTOECon == "V" or PTOECon == "23"):
		print ("[V]")
		print ("Vanadium")
		print ("Table ID: 23")
		print ("Excerpt from https://www.wikipedia.org/wiki/Vanadium")
		print ("Vanadium is a chemical element with symbol V and atomic number 23. It is a hard, silvery-grey, ductile, malleable transition metal. The elemental metal is rarely found in nature, but once isolated artificially, the formation of an oxide layer (passivation) somewhat stabilizes the free metal against further oxidation. ")
	if (PTOECon == "cr" or PTOECon == "CR" or PTOECon == "Cr" or PTOECon == "24"):
		print ("[CR]")
		print ("Chromium")
		print ("Table ID: 24")
		print ("Excerpt from https://www.wikipedia.org/wiki/Chromium")
		print ("Chromium is a chemical element with symbol Cr and atomic number 24. It is the first element in group 6. It is a steely-grey, lustrous, hard and brittle transition metal.[4] Chromium boasts a high usage rate as a metal that is able to be highly polished while resisting tarnishing. Chromium is also the main component of stainless steel, a popular steel alloy due to its uncommonly high specular reflection. Simple polished chromium reflects almost 70% of the visible spectrum, with almost 90% of infrared light waves being reflected.[5] The name of the element is derived from the Greek word χρῶμα, chrōma, meaning color,[6] because many chromium compounds are intensely colored. ")
	if (PTOECon == "mn" or PTOECon == "MN" or PTOECon == "Mn" or PTOECon == "25"):
		print ("[MN]")
		print ("Manganese")
		print ("Table ID: 25")
		print ("Excerpt from https://www.wikipedia.org/wiki/Manganese")
		print ("Manganese is a chemical element with symbol Mn and atomic number 25. It is not found as a free element in nature; it is often found in minerals in combination with iron. Manganese is a metal with important industrial metal alloy uses, particularly in stainless steels. ")
	if (PTOECon == "fe" or PTOECon == "FE" or PTOECon == "Fe" or PTOECon == "26"):
		print "[FE]")
		print ("Iron")
		print ("Table ID: 26")
		print ("Excerpt from https://www.wikipedia.org/wiki/Iron")
		print ("Iron is a chemical element with symbol Fe (from Latin: ferrum) and atomic number 26. It is a metal in the first transition series. It is by mass the most common element on Earth, forming much of Earth's outer and inner core. It is the fourth most common element in the Earth's crust. Its abundance in rocky planets like Earth is due to its abundant production by fusion in high-mass stars, where it is the last element to be produced with release of energy before the violent collapse of a supernova, which scatters the iron into space. ")
	if (PTOECon == "co" or PTOECon == "CO" or PTOECon == "Co" or PTOECon == "27"):
		print ("[CO]")
		print ("Cobalt")
		print ("Table ID: 27")
		print ("Excerpt from https://www.wikipedia.org/wiki/Cobalt")
		print ("Cobalt is a chemical element with symbol Co and atomic number 27. Like nickel, cobalt is found in the Earth's crust only in chemically combined form, save for small deposits found in alloys of natural meteoric iron. The free element, produced by reductive smelting, is a hard, lustrous, silver-gray metal. ")
	if (PTOECon == "ni" or PTOECon == "NI" or PTOECon == "Ni" or PTOECon == "28"):
		print ("[NI]")
		print ("Nickel")
		print ("Table ID: 28")
		print ("Excerpt from https://www.wikipedia.org/wiki/Nickel")
		print ("Nickel is a chemical element with symbol Ni and atomic number 28. It is a silvery-white lustrous metal with a slight golden tinge. Nickel belongs to the transition metals and is hard and ductile. Pure nickel, powdered to maximize the reactive surface area, shows a significant chemical activity, but larger pieces are slow to react with air under standard conditions because an oxide layer forms on the surface and prevents further corrosion (passivation). Even so, pure native nickel is found in Earth's crust only in tiny amounts, usually in ultramafic rocks,[6][7] and in the interiors of larger nickel–iron meteorites that were not exposed to oxygen when outside Earth's atmosphere. ")
	if (PTOECon == "exit" or PTOECon == "Exit" or PTOECon == "EXIT"):
		print ("Sorry, but the exit funciton is unavailable due to a forever loop. To exit, manually close the program")
	noMore = input("Press [ENTER] key to continue")
noMore = input("Press [ENTER] key to exit")
'''
comments
'''
# The whole program got overwritten at 3:58 pm due to Notepad++ experiencing an error. It has infuriated me, since I hurt my back really bad making the program and now I have to completely redo items
# the recovery process is going along well. I have the table all finished back up again, now time for definitions to be added 1/50 out of 118 so far. - Sean Patrick Myrick @ 4:57 pm on December 29th 2018
# Adding in the elements isn't hard to do, it is very easy, the part that makes it take longer is the process. 
'''
lost media
'''
# the original version was lost due to a program error with notepad++ 
# this version has been recreated. It contains all the original info, plus more
# DAY 1:
# Table created
# didn't contain loops
# didn't contain number searches
# didn't go past Atomic Number 10
# DAY 2 (crash):
# contained loops
# didn't go past Atomic Number 50
# added number searches
# Recreation
# DAY 1
# Recreated table
# added first 10 atomic elements
# added loops 
''' 
change log
'''
# V10 - Added more comments 
# V10 - Added in NA and MG (elements 11 and 12)
# V10 - Added change log
# V11 - Added in Alluminium and Silicon (elements 13 and 14)
# V11 - Updated change log 
# V12 - Added in Phosphorus and Sulfur (elements 15 and 16)
# V13 - Updated change log
# V13 - Added in Chlorine and Argon (elements 17 and 18)
# V14 - Updated change log 
# V14 - Added in Potassium and Calcium (elements 19 and 20)
# V15 - Updated change log 
# V15 - Added in Scandium and Titanium (elements 21 and 22)
# V16 - Updated change log 
# V16 - Added in Vanadium and Chromium (elements 23 and 24)
# V17 - Updated change log
# V17 - Modified ASCII table design (very minor change)
# V17 - Added in Manganese and Iron (elements 25 and 26)
# V18 - Updated change log 
# V18 - Added in Cobalt and Nickel (elements 27 and 28)
'''
# end of script
'''
# end of program
''''''
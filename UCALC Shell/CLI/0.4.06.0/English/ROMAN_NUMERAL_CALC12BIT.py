# ASCII art that says "ROMAN NUMERAL CALCULATOR" #
print (" ____  _____  __  __    __    _  _    _  _  __  __  __  __  ____  ____    __    __   ")
print ("(  _ \\(  _  )(  \\/  )  /__\\  ( \\( )  ( \\( )(  )(  )(  \\/  )( ___)(  _ \\  /__\\  (  )  ")
print (" )   / )(_)(  )    (  /(__)\\  )  (    )  (  )(__)(  )    (  )__)  )   / /(__)\\  )(__ ")
print ("(_)\\_)(_____)(_/\\/\\_)(__)(__)(_)\\_)  (_)\\_)(______)(_/\\/\\_)(____)(_)\\_)(__)(__)(____)")
print ("  ___    __    __    ___  __  __  __      __   ____  _____  ____        ")             
print (" / __)  /__\\  (  )  / __)(  )(  )(  )    /__\\ (_  _)(  _  )(  _ \\     ")               
print ("( (__  /(__)\\  )(__( (__  )(__)(  )(__  /(__)\\  )(   )(_)(  )   /   ")                 
print (" \\___)(__)(__)(____)\\___)(______)(____)(__)(__)(__) (_____)(_)\\_) ")                   
print ("\n\n")
tripToRome = str(input("Press [ENTER] key to start"))
# this is branched off old source code. Extra junk was added so that it matched the old case #
if (tripToRome == ""):
	if (tripToRome == ""):
		if (tripToRome == ""):
			calcIDSes = int(55)
			if (tripToRome == ""):
				print ("\n\n\n\n\n\n\n\n\n\n\n\n")
				if calcIDSes == 55:
					# options table #
					print ("Roman numeral calculator")
					print ("NOTICE: this calculator is locked in 12 BIT MODE")
					print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
					print ("▒ Modes           ▒ ID LIST ▒")
					print ("▒ int -> numeral  ▒ ID: 1   ▒")
					print ("▒ numeral -> int  ▒ ID: 2   ▒")
					print ("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
					getInputForRomeA = int(input("Enter an ID to start >> "))
					# int to numeral mode #
					if getInputForRomeA == 1:
						getInputForRome1 = int(input("Enter a number to calculate: "))
						print ("Addition            [ID: 1]")
						print ("Subtraction         [ID: 2]")
						print ("Multiplication      [ID: 3]")
						print ("Division            [ID: 4]")
						print ("Modular division    [ID: 5]")
						getInputForRome2 = int(input("What type of calculation do you want to do out of the given options? Enter ID here: "))
						getInputForRome3 = int(input("Enter the second number to calculate: "))
						if getInputForRome2 == 1:
							preRome = int(getInputForRome1 + getInputForRome3)
						if getInputForRome2 == 2:
							preRome = int(getInputForRome1 - getInputForRome3)
						if getInputForRome2 == 3:
							preRome = int(getInputForRome1 * getInputForRome3)	
						if getInputForRome2 == 4:
							preRome = int(getInputForRome1 / getInputForRome3)	
						if getInputForRome2 == 5:
							preRome = int(getInputForRome1 % getInputForRome3)
						if preRome < 1:
							print ("Syntax error! The number you entered is too small to be transferred as a roman numeral")
						if preRome == 1:
							print ("The answer is I")
						if preRome == 2:
							print ("The answer is II")
						if preRome == 3:
							print ("The answer is III")
						if preRome == 4:
							print ("The answer is IV")
						if preRome == 5:
							print ("The answer is V")
						if preRome == 6:
							print ("The answer is VI")
						if preRome == 7:
							print ("The answer is VII")
						if preRome == 8:
							print ("The answer is VIII")
						if preRome == 9:
							print ("The answer is IX")
						if preRome == 10:
							print ("The answer is X")
						if preRome == 11:
							print ("The answer is XI")
						if preRome == 12:
							print ("The answer is XII")
						if preRome == 13:
							print ("The answer is XIII")
						if preRome == 14:
							print ("The answer is XIV")
						if preRome == 15:
							print ("The answer is XV")
						if preRome == 16:
							print ("The answer is XVI")	
						if preRome == 17:
							print ("The answer is XVII")
						if preRome == 18:
							print ("The answer is XVIII")
						if preRome == 19:
							print ("The answer is XVIX")
						if preRome == 20:
							print ("The answer is XX")
						if preRome == 21:
							print ("The answer is XXI")
						if preRome == 22:
							print ("The answer is XXII")
						if preRome == 23:
							print ("The answer is XXIII")
						if preRome == 24:
							print ("The answer is XXIV")
						if preRome == 25:
							print ("The answer is XXV")
						if preRome == 26:
							print ("The answer is XXVI")
						if preRome == 27:
							print ("The answer is XXVII")
						if preRome == 28:
							print ("The answer is XXVIII")
						if preRome == 29:
							print ("The answer is XXIX")
						if preRome == 30:
							print ("The answer is XXX")
						if preRome == 31:
							print ("The answer is XXXI")
						if preRome == 32:
							print ("The answer is XXXII")
						if preRome == 33:
							print ("The answer is XXXIII")
						if preRome == 34:
							print ("The answer is XXXIV")
						if preRome == 35:
							print ("The answer is XXXV")
						if preRome == 36:
							print ("The answer is XXXVI")
						if preRome == 37:
							print ("The answer is XXXVII")
						if preRome == 38:
							print ("The answer is XXXVIII")
						if preRome == 39:
							print ("The answer is XXXVIX")
						if preRome == 40:
							print ("The answer is XL")
						if preRome == 41:
							print ("The answer is XLI")
						if preRome == 42:
							print ("The answer is XLII")
						if preRome == 43:
							print ("The answer is XLIII")
						if preRome == 44:
							print ("The answer is XLIV")
						if preRome == 45:
							print ("The answer is XLV")
						if preRome == 46:
							print ("The answer is XLVI")
						if preRome == 47:
							print ("The answer is XLVII")
						if preRome == 48:
							print ("The answer is XLVIII")
						if preRome == 49:
							print ("The answer is XLVIX")
						if preRome == 50:
							print ("The answer is L")
						if preRome == 51:
							print ("The answer is LI")
						if preRome == 52:
							print ("The answer is LII")
						if preRome == 53:
							print ("The answer is LIII")
						if preRome == 54:
							print ("The answer is LIV")
						if preRome == 55:
							print ("The answer is LV")
						if preRome == 56:
							print ("The answer is LVI")
						if preRome == 57:
							print ("The answer is LVII")
						if preRome == 58:
							print ("The answer is LVIII")
						if preRome == 59:
							print ("The answer is LVIX")
						if preRome == 60:
							print ("The answer is LX")
						if preRome == 61:
							print ("The answer is LXI")
						if preRome == 62:
							print ("The answer is LXII")
						if preRome == 63:
							print ("The answer is LXIII")
						if preRome == 64:
							print ("The answer is LXIV")
						if preRome == 65:
							print ("The answer is LXV")
						if preRome == 66:
							print ("The answer is LXVI")
						if preRome == 67:
							print ("The answer is LXVII")
						if preRome == 68:
							print ("The answer is LXVIII")
						if preRome == 69:
							print ("The answer is LXVIX")
						if preRome == 70:
							print ("The answer is LXX")
						if preRome == 71:
							print ("The answer is LXXI")
						if preRome == 72:
							print ("The answer is LXXII")
						if preRome == 73:
							print ("The answer is LXXIII")
						if preRome == 74:
							print ("The answer is LXXIV")
						if preRome == 75:
							print ("The answer is LXXV")
						if preRome == 76:
							print ("The answer is LXXVI")
						if preRome == 77:
							print ("The answer is LXXVII")
						if preRome == 78:
							print ("The answer is LXXVIII")
						if preRome == 79:
							print ("The answer is LXXVIX")
						if preRome == 80:
							print ("The answer is LXXX")
						if preRome == 81:
							print ("The answer is LXXXI")
						if preRome == 82:
							print ("The answer is LXXXII")
						if preRome == 83:
							print ("The answer is LXXXIII")
						if preRome == 84:
							print ("The answer is LXXXIV")
						if preRome == 85:
							print ("The answer is LXXXV")
						if preRome == 86:
							print ("The answer is LXXXVI")
						if preRome == 87:
							print ("The answer is LXXXVII")
						if preRome == 88:
							print ("The answer is LXXXVIII")
						if preRome == 89:
							print ("The answer is LXXXVIX")
						if preRome == 90:
							print ("The answer is XC")
						if preRome == 91:
							print ("The answer is XCI")
						if preRome == 92:
							print ("The answer is XCII")
						if preRome == 93:
							print ("The answer is XCIII")
						if preRome == 94:
							print ("The answer is XCIV")
						if preRome == 95:
							print ("The answer is XCV")
						if preRome == 96:
							print ("The answer is XCVI")
						if preRome == 97:
							print ("The answer is XCVII")
						if preRome == 98:
							print ("The answer is XCVIII")
						if preRome == 99:
							print ("The answer is XCVIX")
						if preRome == 100:  #-----------------------------------100 section
							print ("The answer is C")
						if preRome == 101:
							print ("The answer is CI") 
						if preRome == 102:
							print ("The answer is CII") 
						if preRome == 103:
							print ("The answer is CIII")
						if preRome == 104:
							print ("The answer is CIV")
						if preRome == 105:
							print ("The answer is CV")
						if preRome == 106:
							print ("The answer is CVI")
						if preRome == 107:
							print ("The answer is CVII")
						if preRome == 108:
							print ("The answer is CVIII")
						if preRome == 109:
							print ("The answer is CVIX")
						if preRome == 110:
							print ("The answer is CX")
						if preRome == 111:
							print ("The answer is CXI")
						if preRome == 112:
							print ("The answer is CXII")
						if preRome == 113:
							print ("The answer is CXIII")
						if preRome == 114:
							print ("The answer is CXIV")
						if preRome == 115:
							print ("The answer is CXV")
						if preRome == 116:
							print ("The answer is CXVI")
						if preRome == 117:
							print ("The answer is CXVII")
						if preRome == 118:
							print ("The answer is CXVIII")
						if preRome == 119:
							print ("The answer is CXIX")
						if preRome == 120:
							print ("The answer is CXX")
						if preRome == 121:
							print ("The answer is CXXI")
						if preRome == 122:
							print ("The answer is CXXII")
						if preRome == 123:
							print ("The answer is CXXIII")
						if preRome == 124:
							print ("The answer is CXXIV")
						if preRome == 125:
							print ("The answer is CXXV")
						if preRome == 126:
							print ("The answer is CXXVI")
						if preRome == 127:
							print ("The answer is CXXVII")
						if preRome == 128:
							print ("The answer is CXXVIII")
						if preRome == 129:
							print ("The answer is CXXIX")
						if preRome == 130:
							print ("The answer is CXXX")
						if preRome == 131:
							print ("The answer is CXXXI")
						if preRome == 132:
							print ("The answer is CXXXII")
						if preRome == 133:
							print ("The answer is CXXXIII")
						if preRome == 134:
							print ("The answer is CXXXIV")
						if preRome == 135:
							print ("The answer is CXXXV")
						if preRome == 136:
							print ("The answer is CXXXVI")
						if preRome == 137:
							print ("The answer is CXXXVII")
						if preRome == 138:
							print ("The answer is CXXXVIII")
						if preRome == 139:
							print ("The answer is CXXXIX")
						if preRome == 140:
							print ("The answer is CXL")
						if preRome == 141:
							print ("The answer is CXLI")
						if preRome == 142:
							print ("The answer is CXLII")
						if preRome == 143:
							print ("The answer is CXLIII")
						if preRome == 144:
							print ("The answer is CXLIV")
						if preRome == 145:
							print ("The answer is CXLV")
						if preRome == 146:
							print ("The answer is CXLVI")
						if preRome == 147:
							print ("The answer is CXLVII")
						if preRome == 148:
							print ("The answer is CXLVIII")
						if preRome == 149:
							print ("The answer is CXLVIX")
						if preRome == 150:
							print ("The answer is CL")
						if preRome == 151:
							print ("The answer is CLI")
						if preRome == 152:
							print ("The answer is CLII")
						if preRome == 153:
							print ("The answer is CLIII")
						if preRome == 154:
							print ("The answer is CLIV")
						if preRome == 155:
							print ("The answer is CLV")
						if preRome == 156:
							print ("The answer is CLVI")
						if preRome == 157:
							print ("The answer is CLVII")
						if preRome == 158:
							print ("The answer is CLVIII")
						if preRome == 159:
							print ("The answer is CLVIX")
						if preRome == 160:
							print ("The answer is CLX")
						if preRome == 161:
							print ("The answer is CLXI")
						if preRome == 162:
							print ("The answer is CLXII")
						if preRome == 163:
							print ("The answer is CLXIII")
						if preRome == 164:
							print ("The answer is CLXIV")
						if preRome == 165:
							print ("The answer is CLXV")
						if preRome == 166:
							print ("The answer is CLXVI")
						if preRome == 167:
							print ("The answer is CLXVII")
						if preRome == 168:
							print ("The answer is CLXVIII")
						if preRome == 169:
							print ("The answer is CLXIX")
						if preRome == 170:
							print ("The answer is CLXX")
						if preRome == 171:
							print ("The answer is CLXXI")
						if preRome == 172:
							print ("The answer is CLXXII")
						if preRome == 173:
							print ("The answer is CLXXIII")
						if preRome == 174:
							print ("The answer is CLXXIV")
						if preRome == 175:
							print ("The answer is CLXXV")
						if preRome == 176:
							print ("The answer is CLXXVI")
						if preRome == 177:
							print ("The answer is CLXXVII")
						if preRome == 178:
							print ("The answer is CLXXVIII")
						if preRome == 179:
							print ("The answer is CLXXIX")
						if preRome == 180:
							print ("The answer is CLXXX")
						if preRome == 181:
							print ("The answer is CLXXXI")
						if preRome == 182:
							print ("The answer is CLXXXII")
						if preRome == 183:
							print ("The answer is CLXXXIII")
						if preRome == 184:
							print ("The answer is CLXXXIV")
						if preRome == 185:
							print ("The answer is CLXXXV")
						if preRome == 186:
							print ("The answer is CLXXXVI")
						if preRome == 187:
							print ("The answer is CLXXXVII")
						if preRome == 188:
							print ("The answer is CLXXXVIII")
						if preRome == 189:
							print ("The answer is CLXXXVIX")
						if preRome == 190:
							print ("The answer is CXC")
						if preRome == 191:
							print ("The answer is CXCI")
						if preRome == 192:
							print ("The answer is CXCII")
						if preRome == 193:
							print ("The answer is CXCIII")
						if preRome == 194:
							print ("The answer is CXCIV")
						if preRome == 195:
							print ("The answer is CXCV")
						if preRome == 196:
							print ("The answer is CXCVI")
						if preRome == 197:
							print ("The answer is CXCVII")
						if preRome == 198:
							print ("The answer is CXCVIII")
						if preRome == 199:
							print ("The answer is CXCVIX")
						if preRome == 200: #------------------------------------------ 200 Section
							print ("The answer is CC")
						if preRome == 201:
							print ("The answer is CCI")
						if preRome == 202:
							print ("The answer is CCII")
						if preRome == 203:
							print ("The answer is CCIII")
						if preRome == 204:
							print ("The answer is CCIV")
						if preRome == 205:
							print ("The answer is CCV")
						if preRome == 206:
							print ("The answer is CCVI")
						if preRome == 207:
							print ("The answer is CCVII")
						if preRome == 208:
							print ("The answer is CCVIII")
						if preRome == 209:
							print ("The answer is CCVIX")
						if preRome == 210:
							print ("The answer is CCX")
						if preRome == 211:
							print ("The answer is CCXI")
						if preRome == 212:
							print ("The answer is CCXII")
						if preRome == 213:
							print ("The answer is CCXIII")
						if preRome == 214:
							print ("The answer is CCXIV")
						if preRome == 215:
							print ("The answer is CCXV")
						if preRome == 216:
							print ("The answer is CCXVI")
						if preRome == 217:
							print ("The answer is CCXVII")
						if preRome == 218:
							print ("The answer is CCXVIII")
						if preRome == 219:
							print ("The answer is CCXVIX")
						if preRome == 220:
							print ("The answer is CCXX")
						if preRome == 221:
							print ("The answer is CCXXI")
						if preRome == 222:
							print ("The answer is CCXXII")
						if preRome == 223:
							print ("The answer is CCXXIII")
						if preRome == 224:
							print ("The answer is CCXXIV")
						if preRome == 225:
							print ("The answer is CCXXV")
						if preRome == 226:
							print ("The answer is CCXXVI")
						if preRome == 227:
							print ("The answer is CCXXVII")
						if preRome == 228:
							print ("The answer is CCXXVIII")
						if preRome == 229:
							print ("The answer is CCXXVIX")
						if preRome == 230:
							print ("The answer is CCXXX")
						if preRome == 231:
							print ("The answer is CCXXXI")
						if preRome == 232:
							print ("The answer is CCXXXII")
						if preRome == 233:
							print ("The answer is CCXXXIII")
						if preRome == 234:
							print ("The answer is CCXXXIV")
						if preRome == 235:
							print ("The answer is CCXXXV")
						if preRome == 236:
							print ("The answer is CCXXXVI")
						if preRome == 237:
							print ("The answer is CCXXXVII")
						if preRome == 238:
							print ("The answer is CCXXXVIII")
						if preRome == 239:
							print ("The answer is CCXXXVIX")
						if preRome == 240:
							print ("The answer is CCXL")
						if preRome == 241:
							print ("The answer is CCXLI")
						if preRome == 242:
							print ("The answer is CCXLII")
						if preRome == 243:
							print ("The answer is CCXLIII")
						if preRome == 244:
							print ("The answer is CCXLIV")
						if preRome == 245:
							print ("The answer is CCXLV")
						if preRome == 246:
							print ("The answer is CCXLVI")
						if preRome == 247:
							print ("The answer is CCXLVII")
						if preRome == 248:
							print ("The answer is CCXLVIII")
						if preRome == 249:
							print ("The answer is CCXLVIX")
						if preRome == 250:
							print ("The answer is CCL")
						if preRome == 251:
							print ("The answer is CCLI")
						if preRome == 252:
							print ("The answer is CCLII")
						if preRome == 253:
							print ("The answer is CCLIII")
						if preRome == 254:
							print ("The answer is CCLIV")
						if preRome == 255:
							print ("The answer is CCLV")
						if preRome == 256:
							print ("The answer is CCLVI")
						if preRome == 257:
							print ("The answer is CCLVII")
						if preRome == 258:
							print ("The answer is CCLVIII")
						if preRome == 259:
							print ("The answer is CCLVIX")
						if preRome == 260:
							print ("The answer is CCLX")
						if preRome == 261:
							print ("The answer is CCLXI")
						if preRome == 262:
							print ("The answer is CCLXII")
						if preRome == 263:
							print ("The answer is CCLXIII")
						if preRome == 264:
							print ("The answer is CCLXIV")
						if preRome == 265:
							print ("The answer is CCLXV")
						if preRome == 266:
							print ("The answer is CCLXVI")
						if preRome == 267:
							print ("The answer is CCLXVII")
						if preRome == 268:
							print ("The answer is CCLXVIII")
						if preRome == 269:
							print ("The answer is CCLXVIX")
						if preRome == 270:
							print ("The answer is CCLXX")
						if preRome == 271:
							print ("The answer is CCLXXI")
						if preRome == 272:
							print ("The answer is CCLXXII")
						if preRome == 273:
							print ("The answer is CCLXXIII")
						if preRome == 274:
							print ("The answer is CCLXXIV")
						if preRome == 275:
							print ("The answer is CCLXXV")
						if preRome == 276:
							print ("The answer is CCLXXVI")
						if preRome == 277:
							print ("The answer is CCLXXVII")
						if preRome == 278:
							print ("The answer is CCLXXVIII")
						if preRome == 279:
							print ("The answer is CCLXXVIX")
						if preRome == 280:
							print ("The answer is CCLXXX")
						if preRome == 281:
							print ("The answer is CCLXXXI")
						if preRome == 282:
							print ("The answer is CCLXXXII")
						if preRome == 283:
							print ("The answer is CCLXXXIII")
						if preRome == 284:
							print ("The answer is CCLXXXIV")
						if preRome == 285:
							print ("The answer is CCLXXXV")
						if preRome == 286:
							print ("The answer is CCLXXXVI")
						if preRome == 287:
							print ("The answer is CCLXXXVII")
						if preRome == 288:
							print ("The answer is CCLXXXVIII")
						if preRome == 289:
							print ("The answer is CCLXXXIX")
						if preRome == 290:
							print ("The answer is CCXC")
						if preRome == 291:
							print ("The answer is CCXCI")
						if preRome == 292:
							print ("The answer is CCXCII")
						if preRome == 293:
							print ("The answer is CCXCIII")
						if preRome == 294:
							print ("The answer is CCXCIV")
						if preRome == 295:
							print ("The answer is CCXCV")
						if preRome == 296:
							print ("The answer is CCXCVI")
						if preRome == 297:
							print ("The answer is CCXCVII")
						if preRome == 298:
							print ("The answer is CCXCVIII")
						if preRome == 299:
							print ("The answer is CCXCIX")
						if preRome == 300:  #----------------------------------------300 section
							print ("The answer is CCC")							
						if preRome == 400:  #----------------------------------------400 section
							print ("The answer is CD")
						if preRome == 401:
							print ("The answer is CDI")
						if preRome == 402:
							print ("The answer is CDII")
						if preRome == 403:
							print ("The answer is CDIII")
						if preRome == 404:
							print ("The answer is CDIV")
						if preRome == 405:
							print ("The answer is CDV")
						if preRome == 406:
							print ("The answer is CDVI")
						if preRome == 407:
							print ("The answer is CDVII")
						if preRome == 408:
							print ("The answer is CDVIII")
						if preRome == 409:
							print ("The answer is CDVIX")
						if preRome == 410:
							print ("The answer is CDX")
						if preRome == 411:
							print ("The answer is CDXI")
						if preRome == 412:
							print ("The answer is CDXII")
						if preRome == 413:
							print ("The answer is CDXIII")
						if preRome == 414:
							print ("The answer is CDXIV")
						if preRome == 415:
							print ("The answer is CDXV")
						if preRome == 416:
							print ("The answer is CDXVI")
						if preRome == 417:
							print ("The answer is CDXVII")
						if preRome == 418:
							print ("The answer is CXXVIII")
						if preRome == 419:
							print ("The answer is CDXVIX")
						if preRome == 420:
							print ("The answer is CDXX")
						if preRome == 421:
							print ("The answer is CDXXI")
						if preRome == 422:
							print ("The answer is CDXXII")
						if preRome == 423:
							print ("The answer is CDXXIII")
						if preRome == 424:
							print ("The answer is CDXXIV")
						if preRome == 425:
							print ("The answer is CDXXV")
						if preRome == 426:
							print ("The answer is CDXXVI")
						if preRome == 427:
							print ("The answer is CDXXVII")
						if preRome == 428:
							print ("The answer is CDXXVIII")
						if preRome == 429:
							print ("The answer is CDXXVIX")
						if preRome == 430:
							print ("The answer is CDXXX")
						if preRome == 431:
							print ("The answer is CDXXXI")
						if preRome == 432:
							print ("The answer is CDXXXII")
						if preRome == 433:
							print ("The answer is CDXXXIII")
						if preRome == 434:
							print ("The answer is CDXXXIV")
						if preRome == 435:
							print ("The answer is CDXXXV")
						if preRome == 436:
							print ("The answer is CDXXXVI")
						if preRome == 437:
							print ("The answer is CDXXXVII")
						if preRome == 438:
							print ("The answer is CDXXXVIII")
						if preRome == 439:
							print ("The answer is CDXXXVIX")
						if preRome == 440:
							print ("The answer is CDXL")
						if preRome == 441:
							print ("The answer is CDXLI")
						if preRome == 442:
							print ("The answer is CDXLII")
						if preRome == 443:
							print ("The answer is CDXLIII")
						if preRome == 444:
							print ("The answer is CDXLIV")
						if preRome == 445:
							print ("The answer is CDXLV")
						if preRome == 446:
							print ("The answer is CDXLVI")
						if preRome == 447:
							print ("The answer is CDXLVII")
						if preRome == 448:
							print ("The answer is CDXLVIII")
						if preRome == 449:
							print ("The answer is CDXLVIX")
						if preRome == 450:
							print ("The answer is CDL")
						if preRome == 451:
							print ("The answer is CDLI")
						if preRome == 452:
							print ("The answer is CDLII")
						if preRome == 453:
							print ("The answer is CDLIII")
						if preRome == 454:
							print ("The answer is CDLIV")
						if preRome == 455:
							print ("The answer is CDLV")
						if preRome == 456:
							print ("The answer is CDLVI")
						if preRome == 457:
							print ("The answer is CDLVII")
						if preRome == 458:
							print ("The answer is CDLVIII")
						if preRome == 459:
							print ("The answer is CDLVIX")
						if preRome == 460:
							print ("The answer is CDLX")
						if preRome == 461:
							print ("The answer is CDLXI")
						if preRome == 462:
							print ("The answer is CDLXII")
						if preRome == 463:
							print ("The answer is CDLXIII")
						if preRome == 464:
							print ("The answer is CDLXIV")
						if preRome == 465:
							print ("The answer is CDLXV")
						if preRome == 466:
							print ("The answer is CDLXVI")
						if preRome == 467:
							print ("The answer is CDLXVII")
						if preRome == 468:
							print ("The answer is CDLXVIII")
						if preRome == 469:
							print ("The answer is CDLXIX")
						if preRome == 470:
							print ("The answer is CDLXX")
						if preRome == 471:
							print ("The answer is CDLXXI")
						if preRome == 472:
							print ("The answer is CDLXXII")
						if preRome == 473:
							print ("The answer is CDLXXIII")
						if preRome == 474:
							print ("The answer is CDLXXIV")
						if preRome == 475:
							print ("The answer is CDLXXV")
						if preRome == 476:
							print ("The answer is CDLXXVI")
						if preRome == 477:
							print ("The answer is CDLXXVII")
						if preRome == 478:
							print ("The answer is CDLXXVIII")
						if preRome == 479:
							print ("The answer is CDLXXVIX")
						if preRome == 480:
							print ("The answer is CDLXXX")
						if preRome == 481:
							print ("The answer is CDLXXXI")
						if preRome == 482:
							print ("The answer is CDLXXXII")
						if preRome == 483:
							print ("The answer is CDLXXXIII")
						if preRome == 484:
							print ("The answer is CDLXXXIV")
						if preRome == 485:
							print ("The answer is CDLXXXV")
						if preRome == 486:
							print ("The answer is CDLXXXVI")
						if preRome == 487:
							print ("The answer is CDLXXXVII")
						if preRome == 488:
							print ("The answer is CDLXXXVIII")
						if preRome == 489:
							print ("The answer is CDLXXXVIX")
						if preRome == 490:
							print ("The answer is CDXC")
						if preRome == 491:
							print ("The answer is CDXCI")
						if preRome == 492:
							print ("The answer is CDXCII")
						if preRome == 493:
							print ("The answer is CDXCIII")
						if preRome == 494:
							print ("The answer is CDXCIV")
						if preRome == 495:
							print ("The answer is CDXCV")
						if preRome == 496:
							print ("The answer is CDXCVI")
						if preRome == 497:
							print ("The answer is CDXCVII")
						if preRome == 498:
							print ("The answer is CDXCVIII")
						if preRome == 499:
							print ("The answer is CDXCVIX")
						if preRome == 500:  #----------------------------------------500 section
							print ("The answer is D")				
						if preRome == 1000: #----------------------------------------1000 section 
							print ("The answer is M")
						if preRome == 1001:
							print ("The answer is MI")
						if preRome == 1002:
							print ("The answer is MII")
						if preRome == 1003:
							print ("The answer is MIII")
						if preRome == 1004:
							print ("The answer is MIV")
						if preRome == 1005:
							print ("The answer is MV")
						if preRome == 1006:
							print ("The answer is MVI")
						if preRome == 1007:
							print ("The answer is MVII")
						if preRome == 1008:
							print ("The answer is MVIII")
						if preRome == 1009:
							print ("The answer is MVIX")
						if preRome == 1010:
							print ("The answer is MX")
						if preRome == 1011:
							print ("The answer is MXI")
						if preRome == 1012:
							print ("The answer is MXII")
						if preRome == 1013:
							print ("The answer is MXIII")
						if preRome == 1014:
							print ("The answer is MXIV")
						if preRome == 1015:
							print ("The answer is MXV")
						if preRome == 1016:
							print ("The answer is MXVI")
						if preRome == 1017:
							print ("The answer is MXVII")
						if preRome == 1018:
							print ("The answer is MXVIII")
						if preRome == 1019:
							print ("The answer is MXVIX")
						if preRome == 1020:
							print ("The answer is MXX")
						if preRome == 1021:
							print ("The answer is MXXI")
						if preRome == 1022:
							print ("The answer is MXXII")
						if preRome == 1023:
							print ("The answer is MXXIII")
						if preRome == 1024:
							print ("The answer is MXXIV")
						if preRome == 1025:
							print ("The answer is MXXV")
						if preRome == 1026:
							print ("The answer is MXXVI")
						if preRome == 1027:
							print ("The answer is MXXVII")
						if preRome == 1028:
							print ("The answer is MXXVIII")
						if preRome == 1029:
							print ("The answer is MXXVIX")
						if preRome == 1030:
							print ("The answer is MXXX")
						if preRome == 1031:
							print ("The answer is MXXXI")
						if preRome == 1032:
							print ("The answer is MXXXII")
						if preRome == 1033:
							print ("The answer is MXXXIII")
						if preRome == 1034:
							print ("The answer is MXXXIV")
						if preRome == 1035:
							print ("The answer is MXXXV")
						if preRome == 1036:
							print ("The answer is MXXXVI")
						if preRome == 1037:
							print ("The answer is MXXXVII")
						if preRome == 1038:
							print ("The answer is MXXXVIII")
						if preRome == 1039:
							print ("The answer is MXXXVIX")
						if preRome == 1040:
							print ("The answer is MXL")
						if preRome == 1041:
							print ("The answer is MXLI")
						if preRome == 1042:
							print ("The answer is MXLII")
						if preRome == 1043:
							print ("The answer is MXLIII")
						if preRome == 1044:
							print ("The answer is MXLIV")
						if preRome == 1045:
							print ("The answer is MXLV")
						if preRome == 1046:
							print ("The answer is MXLVI")
						if preRome == 1047:
							print ("The answer is MXLVII")
						if preRome == 1048:
							print ("The answer is MXLVIII")
						if preRome == 1049:
							print ("The answer is MXLVIX")
						if preRome == 1050:
							print ("The answer is ML")
						if preRome == 1051:
							print ("The answer is MLI")
						if preRome == 1052:
							print ("The answer is MLII")
						if preRome == 1053:
							print ("The answer is MLIII")
						if preRome == 1054:
							print ("The answer is MLIV")
						if preRome == 1055:
							print ("The answer is MLV")
						if preRome == 1056:
							print ("The answer is MLVI")
						if preRome == 1057:
							print ("The answer is MLVII")
						if preRome == 1058:
							print ("The answer is MLVIII")
						if preRome == 1059:
							print ("The answer is MLVIX")
						if preRome == 1060:
							print ("The answer is MLX")
						if preRome == 4000: #----------------------------------------4000 section
							print ("The answer is MMMM")
						if preRome == 4001:
							print ("The answer is MMMMI")
						if preRome == 4002:
							print ("The answer is MMMMII")
						if preRome == 4003:
							print ("The answer is MMMMIII")
						if preRome == 4004:
							print ("The answer is MMMMIV")
						if preRome == 4005:
							print ("The answer is MMMMV")
						if preRome == 4006:
							print ("The answer is MMMMVI")
						if preRome == 4007:
							print ("The answer is MMMMVII")
						if preRome == 4008:
							print ("The answer is MMMMVIII")
						if preRome == 4009:
							print ("The answer is MMMMVIX")
						if preRome == 4010:
							print ("The answer is MMMMX")
						if preRome == 4011:
							print ("The answer is MMMMXI")
						if preRome == 4012:
							print ("The answer is MMMMXII")
						if preRome == 4013:
							print ("The answer is MMMMXIII")
						if preRome == 4014:
							print ("The answer is MMMMXIV")
						if preRome == 4015:
							print ("The answer is MMMMXV")
						if preRome == 4016:
							print ("The answer is MMMMXVI")
						if preRome == 4017:
							print ("The answer is MMMMXVII")
						if preRome == 4018:
							print ("The answer is MMMMXVIII")
						if preRome == 4019:
							print ("The answer is MMMMXVIX")
						if preRome == 4020:
							print ("The answer is MMMMXX")
						if preRome == 4021:
							print ("The answer is MMMMXXI")
						if preRome > 4096:
							print ("Syntax error! The number you entered is too large to be transferred as a roman numeral")
						# numeral to int mode #
					if getInputForRomeA == 2:
						romeReversi = str(input("Enter a roman numeral to convert: "))
						# UPPERCASE
						if (romeReversi == "I"):
							print ("This is equal to 1")
						if (romeReversi == "II"):
							print ("This is equal to 2")
						if (romeReversi == "III"):
							print ("This is equal to 3")
						if (romeReversi == "IV"):
							print ("This is equal to 4")
						if (romeReversi == "IIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 4")
						if (romeReversi == "V"):
							print ("This is equal to 5")
						if (romeReversi == "VI"):
							print ("This is equal to 6")
						if (romeReversi == "VII"):
							print ("This is equal to 7")
						if (romeReversi == "VIII"):
							print ("This is equal to 8")
						if (romeReversi == "IX"):
							print ("This is equal to 9")
						if (romeReversi == "VIIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 9")
						if (romeReversi == "X"):
							print ("This is equal to 10")
						if (romeReversi == "XI"):
							print ("This is equal to 11")
						if (romeReversi == "XII"):
							print ("This is equal to 12")
						if (romeReversi == "XIII"):
							print ("This is equal to 13")
						if (romeReversi == "XIV"):
							print ("This is equal to 14")
						if (romeReversi == "XIIII"): # Yes this is real. You can also use IIII instead of IV #
							print ("This is equal to 14")
						if (romeReversi == "XV"):
							print ("This is equal to 15")
						if (romeReversi == "XVI"):
							print ("This is equalk to 16")
						# lowercase
						if (romeReversi == "i"):
							print ("This is equal to 1")
						if (romeReversi == "ii"):
							print ("This is equal to 2")
						if (romeReversi == "iii"):
							print ("This is equal to 3")
						if (romeReversi == "iv"):
							print ("This is equal to 4")
						if (romeReversi == "iiii"):  # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 4")
						if (romeReversi == "v"):
							print ("This is equal to 5")
						if (romeReversi == "vi"):
							print ("This is equal to 6")
						if (romeReversi == "vii"):
							print ("This is equal to 7")
						if (romeReversi == "viii"):
							print ("This is equal to 8")
						if (romeReversi == "ix"):
							print ("This is equal to 9")
						if (romeReversi == "viiii"): # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 9")
						if (romeReversi == "x"):
							print ("This is equal to 10")
						if (romeReversi == "xi"):
							print ("This is equal to 11")
						if (romeReversi == "xii"):
							print ("This is equal to 12")
						if (romeReversi == "xiii"):
							print ("This is equal to 13")
						if (romeReversi == "xiv"):
							print ("This is equal to 14")
						if (romeReversi == "xiiii"): # Yes this is real. You can also use iiii instead of iv #
							print ("This is equal to 14")
						if (romeReversi == "xv"):
							print ("This is equal to 15")
						if (romeReversi == "xvi"):
							print ("This is equalk to 16")
						else:
							print ("Invalid numeral entered!")
# ends the program #
endRome = input("Press [ENTER] key to quit")
# end of script # 175 lines of code # 7530 bytes total #
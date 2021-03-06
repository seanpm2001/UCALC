			if WikIDSelect == 20009:
				print ("In computer architecture, 26-bit integers, memory addresses, or other data units are those that are 26 bits wide, and thus can ")
				print ("represent values up to 64 mega (base 2). Two examples of computer processors that featured 26-bit memory addressing are certain ")
				print ("second generation IBM System/370 mainframe computer models introduced in 1981 (and several subsequent models), which had 26-bit ")
				print ("physical addresses but had only the same 24-bit virtual addresses as earlier models, and the first generations of ARM processors.")
				more1 = input("Contents")
				print (" ")
				print ("1 History")
				print ("1.1 IBM System/370")
				print ("1.2 Early ARM processors")
				print ("2 External links")
				print (" ")
				more1 = input("History")
				more1 = input("IBM System/370")
				print (" ")
				print ("As data processing needs continued to grow, IBM and their customers faced challenges directly addressing larger memory sizes. ")
				print ("In what ended up being a short-term ''emergency'' solution, a pair of IBM's second wave of System/370 models, the 3033 and ")
				print ("3081, introduced 26-bit real memory addressing, increasing the System/370's amount of physical memory that could be attached ")
				print ("by a factor of 4 from the previous 24-bit limit of 16 MB. IBM referred to 26-bit addressing as ''extended real addressing,'' ")
				print ("and some subsequent models also included 26-bit support. However, only 2 years later, IBM introduced 31-bit memory addressing, ")
				print ("expanding both physical and virtual addresses to 31 bits, with its System/370-XA models, and even the popular 3081 was ")
				print ("upgradeable to XA standard.")
				print (" ")
				print ("Given 26-bit's brief history as the state-of-the-art in memory addressing available in IBM's model range, and given that ")
				print ("virtual addresses were still limited to 24 bits, software exploitation of 26-bit mode was limited. The few customers that ")
				print ("exploited 26-bit mode eventually adjusted their applications to support 31-bit addressing,[citation needed] and IBM dropped ")
				print ("support for 26-bit mode after several years producing models supporting 24-bit, 26-bit, and 31-bit modes. The 26-bit mode is ")
				print ("the only addressing mode that IBM removed from its line of mainframe computers descended from the System/360. All the other ")
				print ("addressing modes, including now 64-bit mode, are supported in current model mainframes.")
				more1 = input("Early ARM processors")
				print (" ")
				print ("In the ARM processor architecture, 26-bit refers to the design used in the original ARM processors where the Program Counter")
				print ("(PC) and Processor Status Register (PSR) were combined into one 32-bit register (R15), the status flags filling the high 6 ")
				print ("bits and the Program Counter taking up the lower 26 bits.")
				print (" ")
				print ("In fact, because the program counter is always word-aligned the lowest two bits are always zero which allowed the designers") 
				print ("to reuse these two bits to hold the processor's mode bits too. The four modes allowed were USR26, SVC26, IRQ26, FIQ26; ")
				print ("contrast this with the 32 possible modes available when the program status was separated from the program counter in ")
				print ("more recent ARM architectures.")
				print (" ")
				print ("This design enabled more efficient program execution, as the Program Counter and status flags could be saved and restored ")
				print ("with a single operation. This resulted in faster subroutine calls and interrupt response than traditional designs, ")
				print ("which would have to do two register loads or saves when calling or returning from a subroutine.")
				print (" ")
				print ("Despite having a 32-bit ALU and word-length, processors based on ARM architecture version 1 and 2 had only a 26-bit PC and ")
				print ("address bus, and were consequently limited to 64 MiB of addressable memory. This was still a vast amount of memory at the ")
				print ("time, but because of this limitation, architectures since have included various steps away from the original 26-bit design.")
				print (" ")
				print ("The ARM architecture version 3 introduced a 32-bit PC and separate PSR, as well as a 32-bit address bus, allowing 4 GiB of ")
				print ("memory to be addressed. The change in the PC/PSR layout caused incompatibility with code written for previous architectures, ")
				print ("so the processor also included a 26-bit compatibility mode which used the old PC/PSR combination. The processor could still ")
				print ("address 4 GB in this mode, but could not execute anything above address 0x3FFFFFC (64 MB). This mode was used by RISC OS ")
				print ("running on the Acorn Risc PC to utilise the new processors while retaining compatibility with existing software.")
				print (" ")
				print ("ARM architecture version 4 made the support of the 26-bit addressing modes optional, and ARM architecture version 5 ")
				print ("onwards has removed them entirely. ")
				print (" ")
				noMore = input("Press [ENTER] key to exit")
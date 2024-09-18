import colorama 
from colorama import *
colorama.init()

UPK_COLOR = Fore.WHITE

UDSK_ISQUIT = 0

SCKDB_COMMANDS = {
    
}

#UDIK: user determined input key

#UPK: user preference key

#UDSK: user determined sudo key

#SCKDB: sys controlled key database

def mainloop():
    global UPK_COLOR, UDSK_ISQUIT

    while UDSK_ISQUIT != 1:
        UDIK_USERINPUT = input(UPK_COLOR + "maximas > ")

        arguments = UDIK_USERINPUT.split()

        ARGU_COM = arguments[0] if len(arguments) > 1 else None
        ARGU_FIRST = arguments[1] if len(arguments) > 1 else None
        ARGU_SECOND = arguments[2] if len(arguments) > 2 else None
        ARGU_THIRD = arguments[3] if len(arguments) > 3 else None
        ARGU_FOURTH = arguments[4] if len(arguments) > 4 else None
        ARGU_FIFTH = arguments[5] if len(arguments) > 5 else None


        ARGU_FIRSTELSE = arguments[1:] if len(arguments) > 0 else []
        ARGU_SECONDELSE = arguments[2:] if len(arguments) > 1 else []
        ARGU_THIRDELSE = arguments[3:] if len(arguments) > 2 else []
        ARGU_FOURTHELSE = arguments[4:] if len(arguments) > 3 else []
        ARGU_FIFTHELSE = arguments[5:] if len(arguments) > 4 else []
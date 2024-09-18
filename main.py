import colorama 
from colorama import *
colorama.init()

UPK_COLOR = Fore.WHITE

UDSK_ISQUIT = 0



#UDIK: user determined input key

#UPK: user preference key

#UDSK: user determined sudo key

#SCKDB: sys controlled key database

def ECHO_HANDLER(a, b, c, d, e, f, g, E, F, G, H, colors_dependency_lib):
    temp = 0
    ret = ""
    retex = ""
    if a == "-d":
        for temp in range(b):
            temp += 1

            if c == "-c":
                COLOR = d
            else:
                COLOR = "err_in_color"

            if e == "-t":
                TXT_TO_PRN = F
            else:
                TXT_TO_PRN = "err_in_txt"
    
                
            try:
                COL_TO_USE = colors_dependency_lib[COLOR]
            except Exception as e:
                ret = "err_in_color"
                retex = f"{e}"

            ret = (COL_TO_USE + ("🌴 out: " + TXT_TO_PRN))

    else:
        ret = "err_in_do"
    
    return ret, retex
    
SCKDB_COMMANDS = {
    'echo':ECHO_HANDLER
}

def mainloop():
    global UPK_COLOR, UDSK_ISQUIT

    while UDSK_ISQUIT != 1:
        UDIK_USERINPUT = input(UPK_COLOR + "maximas > ")

        arguments = UDIK_USERINPUT.split()

        ARGU_COM = arguments[0] if len(arguments) > 0 else None
        ARGU_FIRST = arguments[1] if len(arguments) > 1 else None
        ARGU_SECOND = arguments[2] if len(arguments) > 2 else None
        ARGU_THIRD = arguments[3] if len(arguments) > 3 else None
        ARGU_FOURTH = arguments[4] if len(arguments) > 4 else None
        ARGU_FIFTH = arguments[5] if len(arguments) > 5 else None
        ARGU_SIXTH = arguments[6] if len(arguments) > 6 else None
        ARGU_SEVENTH = arguments[7] if len(arguments) > 7 else None


        ARGU_FIRSTELSE = arguments[1:] if len(arguments) > 0 else []
        ARGU_SECONDELSE = arguments[2:] if len(arguments) > 1 else []
        ARGU_THIRDELSE = arguments[3:] if len(arguments) > 2 else []
        ARGU_FOURTHELSE = arguments[4:] if len(arguments) > 3 else []
        ARGU_FIFTHELSE = arguments[5:] if len(arguments) > 4 else []
        ARGU_SIXTHELSE = arguments[6:] if len(arguments) > 5 else []
        ARGU_SEVENTHELSE = arguments[7:] if len(arguments) > 6 else []
        ARGU_EIGHTHELSE = arguments[8:] if len(arguments) > 7 else []

        
mainloop()
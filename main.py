import colorama 
from colorama import *
colorama.init()

def mainloop():
    user_color = Fore.WHITE

    while user_input != 'quit':

        user_input = input(user_color + "maximas > ")

mainloop()
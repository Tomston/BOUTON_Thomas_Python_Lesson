from application_terminal import Terminal
#from application_panda3d import Panda3DApplication
from application_tkinter import GUIApplication, GUIoptionWindow

# Python Standard Library Modules
import os
import sys

# Custom Modules
#import application as xx

application_instance = None

# Main Function
def main(application_mode):
    pass # pass the line

    clear_terminal()
    pass

    # Main Function Switch
    match application_mode:
        case "Terminal":
            # print("Well done")
            # Application instance
            application_instance = Terminal() # create the App instance from application file
            # terminal_instance.app_quit() # quit the instance form application file
            pass
            """ Doesn't work on mac => need x86_64 chip architecture
            MAC M1 to execute the file in the terminal => arch -x86_64 /bin/bash            
            case "Panda 3D":
            application_instance = Panda3DApplication()
            application_instance.run()
            pass
            """
        case "Custom Tkinter":
            application_instance = GUIApplication()
            application_instance.mainloop()
            pass
        case _:
            "Default"

   

# Function to clear terminal
# https://docs.python.org/3/library/sys.html#sys.platform
def clear_terminal():
    if (sys.platform == "win32"):
         os.system('cls')
    elif (sys.platform == "darwin"):
        os.system('clear')
    else:
        os.system('cls')



# Main Guard = execute the file if the file name is main
if __name__ == "__main__":
    mode = input("Quel mode voulez-vous entre Terminal, Panda 3D et Custom Tkinter ? : ")
    main(mode)

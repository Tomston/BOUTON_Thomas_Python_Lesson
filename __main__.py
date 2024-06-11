from application_terminal import Terminal
from application_panda3d import Panda3DApplication

# Python Standard Library Modules
import os
import sys

# Custom Modules
#import application as xx


# Main Function
def main(application_mode):
    pass # pass the line

    clear_terminal()
    pass

    # Main Function Switch
    match application_mode:
        case "Terminal":
            print("Well done")
             # Application instance
            terminal_instance = Terminal() # create the App instance from application file
            # terminal_instance.app_quit() # quit the instance form application file
            pass
        case "Panda 3D":
            panda3d_instance = Panda3DApplication()
            panda3d_instance.run()
            pass
        case "Custom Tkinter":
            pass
        case other:
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
    main("Terminal")
    print(__name__)

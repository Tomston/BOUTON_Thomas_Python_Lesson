from application import App
import customtkinter

class GUIApplication (App, customtkinter.CTk):

    def __init__ (self):
        self.app_launch()

    def app_launch(self):
        super().__init__() # hérite de la méthode/constructeur "__init__" des méthodes App et customtkinter pour être exécutées
        self.geometry("1000x800")
        self.title("Python Application")

        # Top Level Window
        self.option_window = None

        # Buttons
        # First Button for options
        self.button_options = customtkinter.CTkButton(self, text="Options", command=self.button_app_options)
        self.button_options.grid(row=0, column=0, padx=15, pady=15)

        # Second Button to quit
        self.button_quit = customtkinter.CTkButton(self, text="Quit Application", command=self.button_app_quit)
        self.button_quit.grid(row=0, column=1, padx=10, pady=15)

        # Third Button
        self.combobox_characters = customtkinter.CTkComboBox(self, values=["Car", "Plane", "Boat"],command=self.button_select_char)
        self.combobox_characters.grid(row=0, column=2)

    def app_menu (self): ...

    def app_options (self): 
        if self.option_window is None or not self.option_window.winfo_exists():
            self.option_window = GUIoptionWindow()
            self.option_window.focus()
        else:
            self.option_window.focus()

    def app_quit (self):
        exit() # permet de quitter le programme
    
    def button_app_options(self):
        self.app_options() # non configuré donc on fait référence à la méthode app_quit

    def button_app_quit(self): 
        self.app_quit()

    def button_select_char(self): ...

class GUIoptionWindow (customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Python APP - Options")

        self_label = customtkinter.CTkLabel(self, text="Top Level Window")
        self.label.grid(row=0, column=15)

if __name__ == "__main__":
    guiApplication_test_instance = GUIApplication()
    guiApplication_test_instance.mainloop()
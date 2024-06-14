from application import App
import customtkinter
from googlefinance import getQuotes
from PIL import Image

# Init global variable
save_input = None
# global xxxx is only use on a method to init a global variable
# gobal save_input

class GUIApplication (App, customtkinter.CTk):

    def __init__ (self):
        self.app_launch()

    def app_launch(self):
        super().__init__() # hérite de la méthode/constructeur "__init__" des méthodes App et customtkinter pour être exécutées
        self.geometry("1100x800")
        self.title("Python Application")

        # Top Level Window
        self.option_window = None
        self.input_dialog = None 
 
        """ 
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

        # Input
        self.button_input = customtkinter.CTkButton(self, text="Enter new character", command=self.button_input_new_char)
        self.button_input.grid(row=1, column=0)

        # To display input
        self.label_character_name = customtkinter.CTkLabel(self, text="No charcter selected")
        self.label_character_name.grid(row=3, column=0)
        """  

        """ Display the stock index chosen
        self.cours = customtkinter.CTkLabel(self, text="Quel est le cours boursier à répliquer 'Nasdaq100' ou 'S&P500' : ?")
        self.cours.grid(padx=300, pady=10)

        self.input = customtkinter.CTkEntry(self)
        self.input.grid(padx=300, pady=10)

        self.display_cours = customtkinter.CTkButton(self, text="Input", command=self.display_stock_price)
        self.display_cours.grid(padx=300, pady=10)

        self.result = customtkinter.CTkLabel(self, text="")
        self.result.grid(padx=300, pady=10)
        """
        # Padding for the GUI
        self.padding = customtkinter.CTkLabel(self, text="")
        self.padding.grid(row=0, ipady=20)

        self.cours = customtkinter.CTkLabel(self, text="Quel est le cours boursier que vous voulez répliquer : ?")
        self.cours.grid(row=20, column=1)

        self.combobox_index = customtkinter.CTkComboBox(self, values=["Nasdaq100", "S&P500", "CAC40", "Eurostoxx50", "MSCI World"])
        self.combobox_index.grid(row=20, column=2)
        self.test_button_index = customtkinter.CTkButton(self, text="Input", command=self.get_value_index)
        self.test_button_index.grid(row=20, column=3)
        
        # execute for the first time the function
        self.get_value_index()
        # print(f"{self.combobox_index.get()}")

        # Padding for the GUI
        self.padding = customtkinter.CTkLabel(self, text="")
        self.padding.grid(row=21, column=0, ipady=5)


        self.three_months = customtkinter.CTkButton(self, text="3 months", command=self.app_menu)
        self.three_months.grid(row=22, column=0, padx=50)
        self.one_year = customtkinter.CTkButton(self, text="1 year", command=self.app_menu)
        self.one_year.grid(row=22, column=1, padx=50)
        self.five_years = customtkinter.CTkButton(self, text="5 years", command=self.app_menu)
        self.five_years.grid(row=22, column=2, padx=50) 
        self.ten_years = customtkinter.CTkButton(self, text="10 years", command=self.app_menu)
        self.ten_years.grid(row=22, column=3, padx=50)

    """     
    def display_stock_price(self):
        global save_input
        save_input = self.input.get()
        self.result.configure(text=f"{save_input}")  
    """
    def get_value_index(self):

        self.get_combo_index = self.combobox_index.get()

        #print in terminal
        #print(f"{self.combobox_index.get()}")

        match self.get_combo_index:
            case "Nasdaq100":
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/Nasdaq100_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)
            case "S&P500":
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/S&P500_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)
            case "CAC40":
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/CAC40_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)
            case "Eurostoxx50":
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/Eurostoxx50_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)
            case "MSCI World":
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/MSCIWORLD_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)
            case _:
                self.Open_Nasdaq_index_picture = customtkinter.CTkImage(light_image=Image.open("projet_python/src/Nasdaq100_index.png"), size=(1000, 550))
                self.Open_Nasdaq_index_picture_label = customtkinter.CTkLabel(self, image=self.Open_Nasdaq_index_picture, text="")
                self.Open_Nasdaq_index_picture_label.grid(row=30, column=0, columnspan=5, pady=5)

    def app_menu (self): ...

    def app_options (self): 
        # Create a second window 
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

    def button_input_new_char(self):
        self.input_dialog = customtkinter.CTkInputDialog(text="Please enter a new character", title="input")
       
        # input display 
        self.label_character_name.configure(text=self.input_dialog.get_input())

    


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
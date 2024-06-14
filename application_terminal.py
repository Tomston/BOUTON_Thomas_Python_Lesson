from application import App
from data import data

# print("Balise : fichier terminal")


class Terminal(App, data): # permet d'hériter des methodes et des instances de App
    # print("Balise : classe terminal")
    #Attibuts de classe
    project_name = "Projet en Python"
    
    #
    def __init__(self):
        # self.terminal_state for debug
        self.terminal_state = "Chargement en cours...."
        self.app_launch()
        #Attributs d'instance

    #
    def app_launch(self):
        print(f"Bienvenue sur le {Terminal.project_name}")
        self.app_menu()

    #
    def app_menu(self):
        print("Menu Principal : Vous souhaitez visualiser les performances de quels indices boursiers ?\n 1) Nasdaq100\n 2) S&P500\n 3) CAC40\n 4) Eurostoxx50\n 5) MSCI World\n")
        print("Saisissez votre choix :")
        self.input_game = input()
        
        match self.input_game:
            case "1": 
                data.Nasdaq_data_index(self)
                print("\n Voici les performances de votre indice :")

                for i in range (0,4,1):
                    print(f"{self.Nasdaq_date[i]} : {self.Nasdaq_performance[i]}")

                self.new_index()
            
            case "2": 
                data.SP500_data_index(self)
                print("\n Voici les performances de votre indice :")

                for i in range (0,4,1):
                    print(f"{self.SP500_date[i]} : {self.SP500_performance[i]}")

                self.new_index()

            case "3": 
                data.CAC40_data_index(self)
                print("\n Voici les performances de votre indice :")

                for i in range (0,4,1):
                    print(f"{self.CAC40_date[i]} : {self.CAC40_performance[i]}")

                self.new_index()

            case "4": 
                data.Eurostoxx50_data_index(self)
                print("\n Voici les performances de votre indice :")

                for i in range (0,4,1):
                    print(f"{self.Eurostoxx50_date[i]} : {self.Eurostoxx50_performance[i]}")

                self.new_index()

            case "5": 
                data.MSCIWORLD_data_index(self)
                print("\nVoici les performances de votre indice :")

                for i in range (0,4,1):
                    print(f"{self.MSCIWORLD_date[i]} : {self.MSCIWORLD_performance[i]}")

                self.new_index()

            case _:
                print("Veuillez tapez 1, 2, 3, 4 ou 5 sur le terminal")
                self.app_quit()

    def app_options(self):
        ...
    
    def app_quit(self):
        exit()

    def new_index(self):
        print("Voulez-vous visualiser l'indice boursier d'un autre indice ? Tapez 'Oui' ou 'Non' :")
        self.new_index_choice = input()
        print(f"{self.new_index_choice}")
         
        if (self.new_index_choice == "Oui"):
            self.app_menu()
        elif (self.new_index_choice == "Non"):
            self.app_quit()
    
""" 
from projet_python.src.application_terminal import App
class Terminal (App):
    

    def __init__(self):
        self.app_launch()

    def app_launch(self):
        self.clear_terminal()
        print("Welcome to the ")

    def app_main_menu(self):
        pass
        
    def app_quit(self): 
        pass
"""
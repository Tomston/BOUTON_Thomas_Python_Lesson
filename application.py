# Python Standard Library Modules
from abc import ABC, abstractmethod


class App (ABC):

    #app_is_running = False

# -----------------------------------
    # Methods
    @abstractmethod # permet de modifier la méthode juste en bas et avoir une méthode abstraite au lien d'une méthode concrète
    def app_launch(self): pass

    @abstractmethod
    def app_menu(self): pass

    @abstractmethod
    def app_options(self): pass

    @abstractmethod
    def app_quit(self): pass

## NE DOIT JAMAIS ETRE INSTANCIER

"""
LES METHODES ABSTRAITES SONT UNIQUEMENT UTILSEES POUR S'ASSURER QUE TOUS
LES FICHIERS UTILISERONT LES MEMES METHODES ET BENEIFICIERONT DES MEMES 
FONCTIONNALITES QUELLES QUE SOIT LE FICHIER
=> pour cela on utilise des méthodes abstraites = bonne pratique
"""
# Python Standard Library Modules
from abc import ABC, abstractmethod


class App (ABC):

    #app_is_running = False

# -----------------------------------
    # Methods
    @abstractmethod
    def app_launch(self): pass

    @abstractmethod
    def app_menu(self): pass

    @abstractmethod
    def app_options(self): pass

    @abstractmethod
    def app_quit(self): pass

## NE DOIT JAMAIS ETRE INSTANCIER

"""
LES METHODES ABSTRAITES SONT UNIQUEMENT UTILSES POUR S'ASSURER QUE TOUS
LES FICHIERS UTILISERONT LES MEMES METHODES ET BENEIFICIERONT DES MEMES 
FONCTIONNALITES QUELLES QUE SOIT LE FICHIER
=> pour cela on utilise des méthodes abstraites = bonne pratique
"""
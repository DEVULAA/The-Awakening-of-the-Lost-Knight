import constantes as c

#pas obligatoire si pas utilisé
from Button import *

import pygame
from Frame import Frame
pygame.init()

class Test(Frame):

    #peut être mit en pause
    pausable = False

    def __init__(self):
        #variable global
        #self.variable = ...
        pass


    def verifyEvents(self,event):
        #gestion des events
        #event.??????
        pass
        
    def showUpdate(self):
        #action à exécuter à chaque frame
        #self.fenetre.??????????
        pass

    def firstAction(self):
        #pas obligatoire
        #action à faire seulement la première fois qu'elle est executé
        pass

    def pause(self):
        #pas obligatoire
        #action à faire lorsque le jeu est mit en pause
        return self.fenetre.copy()

    def unpasue(self):
        #pas obligatoire
        #action à faire lorsque le jeu sort de la pause
        pass

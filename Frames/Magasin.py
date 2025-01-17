import constantes as c
from Button import *
import pygame
from Frame import Frame
pygame.init()

class Magasin(Frame):
    def __init__(self):
        self.cases = pygame.image.load("assets/images/CASES.png")
        self.bouton_retour = Button(c.bouton_background, 'Retour', 20, c.BLANC, 250, 50, (c.LARGEUR // 2) - 250 // 2,500)


    def verifyEvents(self,event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Si le bouton jouer est cliqué, changer l'état du jeu
            if self.bouton_retour.getHitbox().collidepoint(mouse_x, mouse_y):
                c.est_menu = False
                c.game_state = "lobby"
        
    def showUpdate(self):
        self.bouton_retour.show(self.fenetre)
        self.fenetre.blit(self.cases, self.cases.get_rect(center=(c.LARGEUR//2, c.HAUTEUR//2)))


    def firstAction(self):
        c.est_menu = True





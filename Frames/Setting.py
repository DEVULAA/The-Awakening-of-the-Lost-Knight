import constantes as c
from Button import *
import pygame
from Frame import Frame
pygame.init()
class Setting(Frame):
    def __init__(self):
        self.ecran_touches = pygame.image.load("assets/images/ecran_touches.png").convert_alpha()
        self.ecran_touches_pos = (0, 0)
        self.afficher_ecran_touche = False

        self.attente = 0

        self.font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
        self.texte_gros = self.font.render("Paramètres", True, c.NOIR)
        self.texte_rect = self.texte_gros.get_rect(center=((c.LARGEUR // 2) + 10, c.HAUTEUR - (c.HAUTEUR - 40)))


        self.bouton_retour = Button(c.bouton_background, 'Retour', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - (250//2), 500)

        self.bouton_touches = Button(c.bouton_background, 'Touches', 20, c.BLANC, 250, 50, (c.LARGEUR // 2) - (250 // 2), 400)

        self.bouton_mute_image = "assets/images/unmute.png" if c.musique else "assets/images/mute.png"
        self.bouton_mute = pygame.image.load(self.bouton_mute_image)
        self.bouton_mute = pygame.transform.scale(self.bouton_mute.convert_alpha(),(self.bouton_mute.get_width() * 3, self.bouton_mute.get_height() * 3))
        self.rect_bouton_mute = self.bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))


    def verifyEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.rect_bouton_mute.collidepoint(mouse_x, mouse_y):
                if not c.musique:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

                c.musique = not c.musique

            # Si le bouton jouer est cliqué, changer l'état du jeu
            if self.bouton_retour.getHitbox().collidepoint(mouse_x, mouse_y):
                c.game_state = "menu"



            if self.bouton_touches.getHitbox().collidepoint(mouse_x, mouse_y):
                self.afficher_ecran_touche = True
                self.attente = pygame.time.get_ticks()


            if self.ecran_touches.get_rect().collidepoint(mouse_x, mouse_y) and self.afficher_ecran_touche and pygame.time.get_ticks() - self.attente >= 500:
                self.afficher_ecran_touche = False
        
    def showUpdate(self):

        if c.musique:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sons/musique/menu_titre.wav")
                pygame.mixer.music.play(-1)

        else:
            pygame.mixer.music.pause()

        self.fenetre.blit(c.fond, (0, 0))

        self.fenetre.blit(self.texte_gros, self.texte_rect)

        self.bouton_mute_image = "assets/images/unmute.png" if c.musique else "assets/images/mute.png"
        self.bouton_mute = pygame.image.load(self.bouton_mute_image)
        self.bouton_mute = pygame.transform.scale(self.bouton_mute.convert_alpha(),(self.bouton_mute.get_width() * 3, self.bouton_mute.get_height() * 3))
        self.rect_bouton_mute = self.bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))

        self.fenetre.blit(self.bouton_mute, self.rect_bouton_mute)

        self.bouton_retour.show(self.fenetre)
        self.bouton_touches.show(self.fenetre)

        if self.afficher_ecran_touche:
            self.fenetre.blit(self.ecran_touches, self.ecran_touches_pos)

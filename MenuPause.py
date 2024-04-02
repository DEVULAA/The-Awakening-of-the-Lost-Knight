import constantes as c
from Button import Button
import pygame
from Frame import Frame
pygame.init()
class MenuPause(Frame):
    def __init__(self):
        self.image_pause = None

        self.arriere_plan = pygame.Surface((c.LARGEUR, c.HAUTEUR), pygame.SRCALPHA)
        self.arriere_plan.fill((128, 128, 128, 128))

        self.font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
        self.texte_gros = self.font.render("Pause", True, c.NOIR)
        self.texte_rect = self.texte_gros.get_rect(center=(c.LARGEUR / 2, c.HAUTEUR - (c.HAUTEUR - 40)))

        self.bouton_continuer = Button(c.bouton_background, 'Continuer', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - 250//2, 400)
        self.bouton_quitter = Button(c.bouton_background, 'Retour au menu', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - 250//2, 500)

        

    def setImagePause(self,image):
        self.image_pause = image

    def verifyEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.bouton_continuer.getHitbox().collidepoint(mouse_x, mouse_y):
                    c.unpause_game = True

                if self.rect_bouton_mute.collidepoint(mouse_x, mouse_y):
                    c.musique = not c.musique

                if self.bouton_quitter.getHitbox().collidepoint(mouse_x, mouse_y):
                    c.pause = False
                    c.game_state = "menu"
        
    def showUpdate(self):
        if c.musique:
            pygame.mixer.music.pause()
        self.fenetre.blit(self.image_pause, (0, 0))
        self.fenetre.blit(self.arriere_plan, (0, 0))

        self.fenetre.blit(self.texte_gros, self.texte_rect)

        self.bouton_mute_image = "assets/images/unmute.png" if c.musique else "assets/images/mute.png"
        self.bouton_mute = pygame.image.load(self.bouton_mute_image)
        self.bouton_mute = pygame.transform.scale(self.bouton_mute.convert_alpha(), (self.bouton_mute.get_width() * 3, self.bouton_mute.get_height() * 3))
        self.rect_bouton_mute = self.bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))
        self.fenetre.blit(self.bouton_mute, self.rect_bouton_mute)

        self.bouton_continuer.show(self.fenetre)
        self.bouton_quitter.show(self.fenetre)




import constantes as c
import pygame
pygame.init()
class Button:
    def __init__(self,image, texte, taille_texte, couleur_texte, bouton_largeur, bouton_hauteur, pos_x, pos_y):
        self.image = image
        self.texte = texte
        self.taille_texte = taille_texte
        self.couleur_texte = couleur_texte
        self.bouton_largeur = bouton_largeur
        self.bouton_hauteur = bouton_hauteur
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", self.taille_texte)

        self.texte_surface = self.font.render(self.texte, True, self.couleur_texte)

        self.bouton_surface = pygame.Surface((self.bouton_largeur, self.bouton_hauteur))
        self.bouton_surface.set_alpha(0)
        self.bouton_surface.fill(c.BLANC)

    def show(self,fenetre):
        # Dessine le bouton
        fenetre.blit(self.bouton_surface, (self.pos_x, self.pos_y))


        # Charge et affiche l'image
        self.image_surface = pygame.image.load(self.image).convert_alpha()
        self.image_surface = pygame.transform.scale(self.image_surface,(self.bouton_largeur, self.bouton_hauteur))  # Ajuste la taille de l'image
        fenetre.blit(self.image_surface, (self.pos_x + 10, self.pos_y + 10))

        # Dessine le texte au centre du bouton
        self.texte_x = self.pos_x + 10 + (self.bouton_largeur - self.texte_surface.get_width()) / 2
        self.texte_y = self.pos_y + 10 + (self.bouton_hauteur - self.texte_surface.get_height()) / 2
        fenetre.blit(self.texte_surface, (self.texte_x, self.texte_y))

    def getHitbox(self):
        bouton_rect = self.bouton_surface.get_rect()
        bouton_rect.topleft = (self.pos_x, self.pos_y)
        return bouton_rect
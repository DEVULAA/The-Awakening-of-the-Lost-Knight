import pygame
import constantes as c

pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.pos_personnage = (c.LARGEUR // 2, c.HAUTEUR // 2) # Position du personnage
        self.image_dos = [c.personnage_dos,
                          c.personnage_dos_marche1,
                          c.personnage_dos_marche2]
        self.image_face = c.personnage_face

        self.rect = self.image_dos[0].get_rect()
    def animation(self, sens):
        if sens == "haut":
            fenetre.blit(self.image_dos[0], self.image_dos[0].get_rect(center=(self.pos_personnage)))
        if sens == "bas":
            fenetre.blit(self.image_face, self.image_face.get_rect(center=(self.pos_personnage)))




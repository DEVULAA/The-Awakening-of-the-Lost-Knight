import pygame
import constantes as c

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

def principal():

    fenetre.fill(c.BLANC)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            c.running = False


import pygame
import constantes as c
# initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

cases = pygame.image.load("assets/CASES.png")


def principal():

    fenetre.fill(c.BLANC)

    while c.running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False


        pygame.display.flip()


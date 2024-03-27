# Importer les modules
import pygame
import constantes as c
import lobby

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# Fonction principale de jouer.py
def principal():

    fenetre.fill(c.BLANC)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            c.running = False
            pygame.quit()

        lobby.principal()


import pygame
from constantes import *

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

def principal():
    fenetre.fill(BLANC)
import pygame
from constantes import *

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((800, 600))

def main():
    fenetre.fill(BLANC)
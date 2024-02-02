import pygame

from constantes import *

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

def principal():
    fenetre.fill(BLANC)
    font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
    texte_gros = font.render("Paramètres", True, NOIR)
    texte_rect = texte_gros.get_rect(center=(LARGEUR / 2, HAUTEUR - (HAUTEUR - 40)))
    fenetre.blit(texte_gros, texte_rect)

    bouton_retour = creer_bouton(bouton_background, 'RETOUR', 20, 220, 50, 290, 530)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Si le bouton jouer est cliqué, changer l'état du jeu
            if bouton_retour.collidepoint(mouse_x, mouse_y):
                game_state = "menu"



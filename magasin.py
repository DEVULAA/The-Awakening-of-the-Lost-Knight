"""
import pygame
import constantes as c
# initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

cases = pygame.image.load("assets/images/CASES.png")


def principal():
    c.est_menu = True
    fenetre.fill(c.BLANC)

    while c.est_menu:


        bouton_retour = c.creer_bouton(c.bouton_background, 'Retour', 20, c.BLANC, 250, 50, (c.LARGEUR // 2) - 250 // 2,
                                       500)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtenir la position de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Si le bouton jouer est cliqué, changer l'état du jeu
                if bouton_retour.collidepoint(mouse_x, mouse_y):
                    c.est_menu = False

        fenetre.blit(cases, cases.get_rect(center=(c.LARGEUR//2, c.HAUTEUR//2)))
        pygame.display.flip()

"""
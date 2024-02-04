import pygame
import constantes as c

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# Chargement de la carte
carte = c.carte
carte = pygame.transform.scale(carte, (carte.get_width() * 5, carte.get_height() * 5))

def principal():
    # Position du personnage
    pos_personnage = (c.LARGEUR // 2, c.HAUTEUR // 2)

    # Position de la carte
    offset_carte = [(c.LARGEUR // 2) + 450, (c.HAUTEUR // 2) - 3980]

    offset_carte[0] += 1 # Update la carte pour qu'elle s'affiche

    while c.running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.running = False

        # Déplacement de la carte
        touches = pygame.key.get_pressed()

        if touches[pygame.K_LEFT]:
            offset_carte[0] += 4
        if touches[pygame.K_RIGHT]:
            offset_carte[0] -= 4
        if touches[pygame.K_UP]:
            offset_carte[1] += 4
        if touches[pygame.K_DOWN]:
            offset_carte[1] -= 4

        #verification si echap est pressé

        if touches[pygame.K_ESCAPE]:
            c.verif_echap = 0
            while c.verif_echap == 0:
                import menu_echap
                menu_echap.principal()

        if c.verif_echap == 2:
            c.game_state = "menu"

        fenetre.fill(c.BLANC)
        fenetre.blit(carte, carte.get_rect(center=(offset_carte))) #Affichage de la carte
        fenetre.blit(c.personnage, c.personnage.get_rect(center=(pos_personnage))) #Affichage du personnage


        # Mettre à jour l'affichage
        pygame.display.flip()

        # Mets à jour les FPS
        pygame.time.Clock().tick(c.FPS)


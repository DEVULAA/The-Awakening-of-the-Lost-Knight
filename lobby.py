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



    # Position de la carte
    offset_carte = [(c.LARGEUR // 2) + 450, (c.HAUTEUR // 2) - 3980]

    offset_carte[0] += 1 # Update la carte pour qu'elle s'affiche
    fenetre.fill(c.BLANC)


    while c.running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    import menu_echap
                    menu_echap.principal()

        fenetre.blit(carte, carte.get_rect(center=(offset_carte))) #Affichage de la carte
        fenetre.blit(c.personnage_dos, c.personnage_dos.get_rect(center=(c.pos_personnage)))  # Affichage du personnage


        touches = pygame.key.get_pressed()

        if not c.pause:

            if touches[pygame.K_LEFT]:
               offset_carte[0] += 4
            if touches[pygame.K_RIGHT]:
                offset_carte[0] -= 4
            if touches[pygame.K_UP]:
                offset_carte[1] += 4
                c.animation("haut")
            if touches[pygame.K_DOWN]:
                offset_carte[1] -= 4
                c.animation("bas")



        # Mettre à jour l'affichage
        pygame.display.flip()

        # Mets à jour les FPS
        pygame.time.Clock().tick(c.FPS)


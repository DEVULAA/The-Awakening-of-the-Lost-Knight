import pygame
import constantes as c
# initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

arriere_plan = pygame.image.load("assets/images/level1/background.png")

sol = pygame.image.load("assets/images/level1/background_sol.png")
sol_rect = sol.get_rect(topleft=(0, 552))

personnage_level = pygame.image.load("assets/images/personnage/level/main.png")
personnage_level = pygame.transform.scale(personnage_level, (personnage_level.get_width() * 2.5, personnage_level.get_height() * 2.5))




touches_pressee = {"gauche": False, "droite": False, "haut": False}


def principal():

    pos_perso_x = 43
    pos_perso_y = 415

    conteur_saut = 0
    max_saut = 17


    en_saut = False

    fenetre.fill(c.BLANC)

    while c.running:

        pygame.time.Clock().tick(c.FPS)

        fenetre.blit(arriere_plan, (0, 0))
        fenetre.blit(sol, sol_rect)

        if c.musique == False:
            pygame.mixer.music.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    touches_pressee["gauche"] = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    touches_pressee["droite"] = True
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and not en_saut:
                    en_saut = True
                    conteur_saut = max_saut

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    touches_pressee["gauche"] = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    touches_pressee["droite"] = False

                if event.key == pygame.K_ESCAPE:

                    perso_rect = personnage_level.get_rect(topleft=(pos_perso_x, pos_perso_y))
                    fenetre.blit(personnage_level, perso_rect)

                    c.image_pause = fenetre.copy()
                    import menu_echap
                    menu_echap.principal()

        bordures_verif_droite = pos_perso_x >= 0
        bordures_verif_gauche = pos_perso_x <= 710



        if touches_pressee["gauche"] and bordures_verif_droite:
            pos_perso_x = pos_perso_x - 4

        if touches_pressee["droite"] and bordures_verif_gauche:
            pos_perso_x = pos_perso_x + 4

        if en_saut:
            pos_perso_y -= conteur_saut
            if conteur_saut > -max_saut:
                conteur_saut -= 1
            else:
                en_saut = False

        perso_rect = personnage_level.get_rect(topleft=(pos_perso_x, pos_perso_y))
        fenetre.blit(personnage_level, perso_rect)

        pygame.display.flip()

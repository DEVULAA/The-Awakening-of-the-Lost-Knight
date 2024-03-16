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

    pos_perso = (43, 415)

    while c.running:

        fenetre.fill(c.BLANC)


        fenetre.blit(arriere_plan, (0, 0))
        fenetre.blit(sol, sol_rect)

        fenetre.blit(personnage_level, pos_perso)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    c.image_pause = fenetre.copy()
                    import menu_echap
                    menu_echap.principal()


                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    touches_pressee["gauche"] = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    touches_pressee["droite"] = True
                elif event.key == pygame.K_UP or event.key == pygame.K_z:
                    touches_pressee["haut"] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    touches_pressee["gauche"] = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    touches_pressee["droite"] = False
                elif event.key == pygame.K_UP or event.key == pygame.K_z:
                    touches_pressee["haut"] = False

        bordures_verif_droite = pos_perso[0] >= 0
        bordures_verif_gauche = pos_perso[0] <= 710

        if touches_pressee["gauche"] and bordures_verif_droite:
            pos_perso = (pos_perso[0] - 0.3, pos_perso[1])

        elif touches_pressee["droite"] and bordures_verif_gauche:
            pos_perso = (pos_perso[0] + 0.3, pos_perso[1])

        pygame.display.flip()


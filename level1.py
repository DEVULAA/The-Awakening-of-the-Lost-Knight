import pygame
import constantes as c

# initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

arriere_plan = pygame.image.load("assets/images/level1/background.png")

sol = pygame.image.load("assets/images/level1/background_sol.png")
sol_rect = sol.get_rect(topleft=(0, 552))

# Charger la sprite sheet
sprite_sheet = pygame.image.load("assets/images/personnage/level/char_sheet.png").convert_alpha()

# Définir les dimensions de chaque sprite dans la sprite sheet
sprite_width = 56
sprite_height = 56

# Créer une liste pour stocker chaque sprite de l'animation d'attente
waiting_animation = []
for i in range(6):  # Il y a 6 sprites dans l'animation d'attente
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, 0, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2.5, sprite.get_height() * 2.5))  # Ajuster la taille du sprite
    waiting_animation.append(sprite.convert_alpha())

animation_marche = []
for i in range(8):  # Il y a 8 sprites dans l'animation de marche
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, sprite_height*2, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2.5, sprite.get_height() * 2.5))  # Ajuster la taille du sprite
    animation_marche.append(sprite.convert_alpha())

# Initialiser l'index de l'animation d'attente
waiting_index = 0
index_marche = 0

touches_pressee = {"gauche": False, "droite": False, "haut": False}

def principal():
    global waiting_index, index_marche  # Utiliser la variable globale waiting_index

    pos_perso_x = 43
    pos_perso_y = 415

    conteur_attente = 0
    conteur_marche = 0

    conteur_saut = 0
    max_saut = 17


    derniere_direction = "droite"


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

                    c.image_pause = fenetre.copy()
                    import menu_echap
                    menu_echap.principal()

        bordures_verif_droite = pos_perso_x >= 0
        bordures_verif_gauche = pos_perso_x <= 690

        if touches_pressee["gauche"] and bordures_verif_droite and not touches_pressee["droite"]:

            pos_perso_x = pos_perso_x - 4
            derniere_direction = "gauche"
            # Afficher le sprite de l'animation de marche inversée
            perso_rect = pygame.transform.flip(animation_marche[index_marche], True, False).get_rect(topleft=(pos_perso_x, pos_perso_y))
            fenetre.blit(pygame.transform.flip(animation_marche[index_marche], True, False), perso_rect)

        elif touches_pressee["droite"] and bordures_verif_gauche and not touches_pressee["gauche"]:

            pos_perso_x = pos_perso_x + 4
            derniere_direction = "droite"
            # Afficher le sprite de l'animation de marche
            perso_rect = animation_marche[index_marche].get_rect(topleft=(pos_perso_x, pos_perso_y))
            fenetre.blit(animation_marche[index_marche], perso_rect)

        else:

            if derniere_direction == "droite":

                # Afficher le sprite de l'animation d'attente
                perso_rect = waiting_animation[waiting_index].get_rect(topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(waiting_animation[waiting_index], perso_rect)
            else:
                perso_rect = pygame.transform.flip(waiting_animation[waiting_index], True, False).get_rect(
                    topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(pygame.transform.flip(waiting_animation[waiting_index], True, False), perso_rect)

        if en_saut:
            pos_perso_y -= conteur_saut
            if conteur_saut > -max_saut:
                conteur_saut -= 1
            else:
                en_saut = False


        if int(conteur_attente) == 10:
            # Mettre à jour l'index de l'animation d'attente
            waiting_index = (waiting_index + 1) % len(waiting_animation)
            conteur_attente = 0

        if int(conteur_marche) == 5:
            # Mettre à jour l'index de l'animation de marche
            index_marche = (index_marche + 1) % len(animation_marche)
            conteur_marche = 0

        conteur_attente += 1
        conteur_marche += 1


        pygame.display.flip()

principal()
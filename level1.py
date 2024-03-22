import pygame
import constantes as c

# initialiser pygame
pygame.init()

# créer la fenêtre
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# chargement de l'arrière plan
arriere_plan = pygame.image.load("assets/images/level1/background.png")

# chargement du sol
sol = pygame.image.load("assets/images/level1/background_sol.png")
sol_rect = sol.get_rect(topleft=(0, 552))


# -------------------- ANIMATIONS JOUEUR ---------------------
# chargement de la feuille des sprites du joueur
sprite_sheet = pygame.image.load("assets/images/personnage/level/char_sheet.png").convert_alpha()

# dimensions de chaque case de la feuille des sprites
sprite_width = 56
sprite_height = 56

# animation attente
waiting_animation = []
for i in range(6):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, 0, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    waiting_animation.append(sprite.convert_alpha())

# animation marche
animation_marche = []
for i in range(8):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, sprite_height*2, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_marche.append(sprite.convert_alpha())

# animation attaque
animation_attaque = []
for i in range(8):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 1, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_attaque.append(sprite.convert_alpha())

# image de saut
sprite_saut = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
sprite_saut.blit(sprite_sheet, (0, 0), (sprite_width*7, sprite_height*3, sprite_width, sprite_height))
sprite_saut = pygame.transform.scale(sprite_saut, (sprite_saut.get_width() * 3, sprite_saut.get_height() * 3))  # Ajuster la taille du sprite


# initialisation d'index pour les animations
waiting_index = 0
index_marche = 0
index_attaque = 0


# -------------------- ANIMATIONS BOSS ---------------------

#chargement de la feuille des sprites du boss
boss_sheet = pygame.image.load("assets/images/boss/level/boss_sheet.png").convert_alpha()

# dimensions du boss
boss_width = 64
boss_height = 64

# animation attente
boss_animation_attente = []
for i in range(6):
    sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
    sprite.blit(boss_sheet, (0, 0), (i*boss_width, 0, boss_width, boss_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
    boss_animation_attente.append(sprite.convert_alpha())

#animation degats
boss_animation_degats = []
for i in range(4):
    sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
    sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height*2, boss_width, boss_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
    boss_animation_degats.append(sprite.convert_alpha())

#animation mort
boss_animation_mort = []
for i in range(7):
    sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
    sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height*3, boss_width, boss_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
    boss_animation_mort.append(sprite.convert_alpha())

# index animations boss
index_boss_attente = 0
index_boss_degats = 0
index_boss_mort = 0

# dictionnaire des touches pressées
touches_pressee = {"gauche": False, "droite": False, "haut": False}


def principal():
    global waiting_index, index_marche, index_attaque, index_boss_attente, index_boss_degats, index_boss_mort

    pos_perso_x = 43
    pos_perso_y = 385

    pos_boss_x = 650
    pos_boss_y = 425


    vie_boss = 500 # initialise la vie du boss à 500 HP
    vie_perso = 100 # initialise la vie du joueur à 100 HP

    conteur_attente = 0
    conteur_marche = 0
    compteur_attaque = 0

    compteur_attente_boss = 0
    compteur_degats_boss = 0
    compteur_boss_mort = 0

    conteur_saut = 0
    max_saut = 17

    derniere_direction = "droite"

    en_saut = False
    attaque = False

    boss_est_attaque = False

    fini = False

    fenetre.fill(c.BLANC)

    while c.running:
        pygame.time.Clock().tick(c.FPS)

        fenetre.blit(arriere_plan, (0, 0))
        fenetre.blit(sol, sol_rect)

        if c.musique == False:
            pygame.mixer.music.pause()

        if not fini :
            if c.musique:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("assets/sons/musique/levels.wav")
                    pygame.mixer.music.set_volume(c.volume / 100)
                    pygame.mixer.music.play(-1)


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

                if event.key == pygame.K_f and not attaque:
                    attaque = True
                    if perso_rect.colliderect(boss_rect):

                        index_boss_degats = 0
                        vie_boss -= 10
                        boss_est_attaque = True

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
        bordures_verif_gauche = pos_perso_x <= 632

        if touches_pressee["gauche"] and bordures_verif_droite and not touches_pressee["droite"]:

            pos_perso_x = pos_perso_x - 4
            derniere_direction = "gauche"

            if not en_saut and not attaque:
                # Afficher le sprite de l'animation de marche inversée
                perso_rect = pygame.transform.flip(animation_marche[index_marche], True, False).get_rect(topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(pygame.transform.flip(animation_marche[index_marche], True, False), perso_rect)

        elif touches_pressee["droite"] and bordures_verif_gauche and not touches_pressee["gauche"]:

            pos_perso_x = pos_perso_x + 4
            derniere_direction = "droite"

            if not en_saut and not attaque:

                # Afficher le sprite de l'animation de marche
                perso_rect = animation_marche[index_marche].get_rect(topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(animation_marche[index_marche], perso_rect)

        else:

            if derniere_direction == "droite":
                if not en_saut and not attaque:
                    # Afficher le sprite de l'animation d'attente
                    perso_rect = waiting_animation[waiting_index].get_rect(topleft=(pos_perso_x, pos_perso_y))
                    fenetre.blit(waiting_animation[waiting_index], perso_rect)
            else:
                if not en_saut and not attaque:
                    perso_rect = pygame.transform.flip(waiting_animation[waiting_index], True, False).get_rect(
                            topleft=(pos_perso_x, pos_perso_y))
                    fenetre.blit(pygame.transform.flip(waiting_animation[waiting_index], True, False), perso_rect)


        if attaque and not fini:

            if not en_saut:
                if derniere_direction == "droite":
                    perso_rect = animation_attaque[index_attaque].get_rect(topleft=(pos_perso_x, pos_perso_y))
                    fenetre.blit(animation_attaque[index_attaque], perso_rect)
                else:
                    perso_rect = pygame.transform.flip(animation_attaque[index_attaque], True, False).get_rect(
                            topleft=(pos_perso_x, pos_perso_y))
                    fenetre.blit(pygame.transform.flip(animation_attaque[index_attaque], True, False), perso_rect)


        if en_saut:

            pos_perso_y -= conteur_saut
            if conteur_saut > -max_saut:
                conteur_saut -= 1
            else:
                en_saut = False

            if derniere_direction == "droite":
                # Afficher l'image de saut
                perso_rect = sprite_saut.get_rect(topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(sprite_saut, perso_rect)
            else:
                perso_rect = pygame.transform.flip(sprite_saut, True, False).get_rect(topleft=(pos_perso_x, pos_perso_y))
                fenetre.blit(pygame.transform.flip(sprite_saut, True, False), perso_rect)

        if int(conteur_attente) == 10:
            # Mettre à jour l'index de l'animation d'attente
            waiting_index = (waiting_index + 1) % len(waiting_animation)
            conteur_attente = 0

        if int(conteur_marche) == 5:
            # Mettre à jour l'index de l'animation de marche
            index_marche = (index_marche + 1) % len(animation_marche)
            conteur_marche = 0


        if int(compteur_attaque) == 5:
            # Mettre à jour l'index de l'animation d'attaque
            index_attaque = (index_attaque + 1) % len(animation_attaque)
            compteur_attaque = 0

            # Vérifier si l'animation d'attaque est terminée
            if index_attaque == 0:
                attaque = False

        conteur_attente += 1
        conteur_marche += 1

        if attaque:
            compteur_attaque += 1

        # gestion boss
        if not boss_est_attaque and vie_boss > 0:

            boss_rect = boss_animation_attente[index_boss_attente].get_rect(topleft=(pos_boss_x, pos_boss_y))
            fenetre.blit(boss_animation_attente[index_boss_attente], boss_rect)

        if int(compteur_attente_boss) == 5:
            index_boss_attente = (index_boss_attente + 1) % len(boss_animation_attente)
            compteur_attente_boss = 0

        compteur_attente_boss += 1

        if boss_est_attaque and not fini:


            boss_rect = boss_animation_degats[index_boss_degats].get_rect(topleft=(pos_boss_x, pos_boss_y))
            fenetre.blit(boss_animation_degats[index_boss_degats], boss_rect)


            if int(compteur_degats_boss) == 5:
                index_boss_degats = (index_boss_degats + 1) % len(boss_animation_degats)
                compteur_degats_boss = 0

            if index_boss_degats == 3:
                boss_est_attaque = False

            compteur_degats_boss += 1


        if vie_boss == 0:

            if not fini:

                boss_rect = boss_animation_mort[index_boss_mort].get_rect(topleft=(pos_boss_x, pos_boss_y))
                fenetre.blit(boss_animation_mort[index_boss_mort], boss_rect)

                if int(compteur_boss_mort) == 10:
                    index_boss_mort = (index_boss_mort + 1) % len(boss_animation_mort)
                    compteur_boss_mort = 0

            compteur_boss_mort += 1

            if index_boss_mort == 6:
                fini = True
                fenetre.blit(boss_animation_mort[6], boss_rect)

        pygame.display.flip()

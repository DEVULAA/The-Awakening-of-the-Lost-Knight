import pygame
import constantes as c
import random as r

# initialiser pygame
pygame.init()

# créer la fenêtre
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# chargement de l'arrière plan
arriere_plan = pygame.image.load("assets/images/level1/background.png").convert_alpha()



# -------------------- ANIMATIONS JOUEUR ---------------------
# chargement de la feuille des sprites du joueur
sprite_sheet = pygame.image.load("assets/images/personnage/level/char_sheet.png").convert_alpha()

# dimensions de chaque case de la feuille des sprites
sprite_width = 56
sprite_height = 56

# animation attente
animation_attente = []
for i in range(6):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, 0, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_attente.append(sprite.convert_alpha())

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


# animation dégats
animation_degat = []
for i in range(4):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 5, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_degat.append(sprite.convert_alpha())

# animation de mort
animation_mort = []
for i in range(8):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 6, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_mort.append(sprite.convert_alpha())
for i in range(4):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 7, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    animation_mort.append(sprite.convert_alpha())

# animation bouclier
bouclier_animation = []
for i in range(3):
    sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 10, sprite_width, sprite_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
    bouclier_animation.append(sprite.convert_alpha())

# image de saut
sprite_saut = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
sprite_saut.blit(sprite_sheet, (0, 0), (sprite_width*7, sprite_height*3, sprite_width, sprite_height))
sprite_saut = pygame.transform.scale(sprite_saut, (sprite_saut.get_width() * 3, sprite_saut.get_height() * 3))  # Ajuster la taille du sprite


# initialisation d'index pour les animations
index_attente = 0
index_marche = 0
index_attaque = 0
index_degat = 0
index_mort = 0
index_bouclier = 0

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

# animation attaque boss
boss_animation_attaque = []
for i in range(5):
    sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
    sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height, boss_width, boss_height))
    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
    boss_animation_attaque.append(sprite.convert_alpha())

# index animations boss
index_boss_attente = 0
index_boss_degats = 0
index_boss_mort = 0
index_boss_attaque = 0


# dictionnaire des touches pressées
touches_pressee = {"gauche": False, "droite": False, "haut": False}


def principal():
    global index_attente, index_marche, index_attaque, index_boss_attente, index_boss_degats, index_boss_mort, index_degat, index_mort, index_bouclier, index_boss_attaque

    pos_perso_x = 0
    pos_perso_y = 385

    pos_boss_x = 650
    pos_boss_y = 425

    vie_boss = 300 # initialise la vie du boss à 300 HP
    vie_perso = 100 # initialise la vie du joueur à 100 HP

    compteur_attente = 0
    compteur_marche = 0
    compteur_attaque = 0
    compteur_degat = 0
    compteur_mort = 0
    compteur_bouclier = 0

    compteur_attente_boss = 0
    compteur_degats_boss = 0
    compteur_boss_mort = 0
    compteur_attaque_boss = 0

    animation_temps_debut = 0

    compteur_saut = 0
    max_saut = 17

    temps_replis = 0

    derniere_direction = "droite"

    en_saut = False
    attaque = False

    joueur_est_attaque = False
    joueur_bouclier = False
    animation_bouclier_finie = False

    boss_est_attaque = False
    boss_attaque = False
    attaque_deja_fait = False





    barre_boss = pygame.image.load("assets/images/boss/level/barre_de_vie.png").convert_alpha()
    rect_barre_boss = barre_boss.get_rect(topleft=(445, 35))

    barre_joueur = pygame.image.load("assets/images/personnage/level/barre_de_vie.png").convert_alpha()
    rect_barre_joueur = barre_joueur.get_rect(topleft=(70, 35))

    icone = pygame.image.load('assets/images/icone.png').convert_alpha()
    icone = pygame.transform.scale(icone, (icone.get_width() * 2, icone.get_height() * 2))

    icone_rect = icone.get_rect(center=(c.LARGEUR / 2, 40))


    fini = False

    fenetre.fill(c.BLANC)

    while c.running:
        pygame.time.Clock().tick(c.FPS)

        fenetre.blit(arriere_plan, (0, 0))

        couleur_barre_boss = (70, 199, 58)
        interieur_barre_boss = pygame.Rect(447, 39, int(vie_boss / 1.14), 7)

        couleur_barre_joueur = (204, 33, 0)
        interieur_barre_joueur = pygame.Rect(89, 39, int(vie_perso * 2.64), 7)

        pygame.draw.rect(fenetre, couleur_barre_boss, interieur_barre_boss)
        fenetre.blit(barre_boss, rect_barre_boss)

        pygame.draw.rect(fenetre, couleur_barre_joueur, interieur_barre_joueur)
        fenetre.blit(barre_joueur, rect_barre_joueur)

        fenetre.blit(icone, icone_rect)


        perso_rect = animation_attente[0].get_rect(topleft=(pos_perso_x, pos_perso_y))
        perso_rect_bouclier = animation_attente[0].get_rect(topleft=(pos_perso_x, pos_perso_y))
        perso_rect[2] = 130
        perso_rect_bouclier[2] = 100


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
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and not en_saut and not joueur_bouclier and not animation_bouclier_finie and not fini:
                    en_saut = True
                    compteur_saut = max_saut

                if event.key == pygame.K_f and not attaque and not fini and not joueur_bouclier and not animation_bouclier_finie:
                    attaque = True

                    if perso_rect.colliderect(boss_rect):

                        index_boss_degats = 0
                        vie_boss -= 30
                        boss_est_attaque = True
                        animation_temps_debut = pygame.time.get_ticks()

                if event.key == pygame.K_b and not attaque and not fini and not joueur_bouclier:

                    compteur_bouclier = 0
                    joueur_bouclier = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    touches_pressee["gauche"] = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    touches_pressee["droite"] = False

                if event.key == pygame.K_b :

                    joueur_bouclier = False
                    animation_bouclier_finie = False

                if event.key == pygame.K_ESCAPE:

                    c.image_pause = fenetre.copy()
                    import menu_echap
                    menu_echap.principal()

        bordures_verif_droite = pos_perso_x >= 0
        bordures_verif_gauche = pos_perso_x <= 632

        if touches_pressee["gauche"] and bordures_verif_droite and not touches_pressee["droite"] and not fini:

            if not joueur_bouclier and not animation_bouclier_finie:
                pos_perso_x = pos_perso_x - 4
            else :
                pos_perso_x = pos_perso_x - 1

            if joueur_bouclier or animation_bouclier_finie:
                derniere_direction = "droite"
            else:
                derniere_direction = "gauche"

            if not en_saut and not attaque and not joueur_est_attaque and not animation_bouclier_finie and not joueur_bouclier:
                # Afficher le sprite de l'animation de marche inversée
                fenetre.blit(pygame.transform.flip(animation_marche[index_marche], True, False), perso_rect)

        elif touches_pressee["droite"] and bordures_verif_gauche and not touches_pressee["gauche"] and not fini:

            if not pos_boss_x - pos_perso_x <= perso_rect[2]:

                if not joueur_bouclier and not animation_bouclier_finie:
                    pos_perso_x = pos_perso_x + 4
                else:
                    pos_perso_x = pos_perso_x + 1
                derniere_direction = "droite"

            if not en_saut and not attaque and not joueur_est_attaque and not animation_bouclier_finie and not joueur_bouclier :

                # Afficher le sprite de l'animation de marche
                fenetre.blit(animation_marche[index_marche], perso_rect)

        else:

            if derniere_direction == "droite":
                if not en_saut and not attaque and not joueur_est_attaque and not joueur_bouclier and not animation_bouclier_finie:
                    # Afficher le sprite de l'animation d'attente
                    fenetre.blit(animation_attente[index_attente], perso_rect)
            else:

                if not en_saut and not attaque and not joueur_est_attaque and not joueur_bouclier and not animation_bouclier_finie:
                    fenetre.blit(pygame.transform.flip(animation_attente[index_attente], True, False), perso_rect)


        if attaque and not fini and not joueur_est_attaque:

            if not en_saut:
                if derniere_direction == "droite":
                    fenetre.blit(animation_attaque[index_attaque], perso_rect)
                else:
                    fenetre.blit(pygame.transform.flip(animation_attaque[index_attaque], True, False), perso_rect)


        if en_saut and not fini:

            pos_perso_y -= compteur_saut
            if compteur_saut > -max_saut:
                compteur_saut -= 1
            else:
                en_saut = False



            if derniere_direction == "droite" :
                # Afficher l'image de saut
                fenetre.blit(sprite_saut, perso_rect)
            else:
                fenetre.blit(pygame.transform.flip(sprite_saut, True, False), perso_rect)

        if joueur_est_attaque and not en_saut and vie_perso > 0:

            if derniere_direction == "droite":
                fenetre.blit(animation_degat[index_degat], perso_rect)
            else:
                fenetre.blit(pygame.transform.flip(animation_degat[index_degat], True, False), perso_rect)

            if int(compteur_degat) == 5:
                # Mettre à jour l'index de l'animation de degat
                index_degat = (index_degat + 1) % len(animation_degat)
                compteur_degat = 0

            if index_degat == 3:
                index_degat = 0
                joueur_est_attaque = False


            compteur_degat += 1

        if joueur_bouclier and not en_saut and vie_perso > 0 and not fini and not joueur_est_attaque:


            fenetre.blit(bouclier_animation[index_bouclier], perso_rect_bouclier)


            if int(compteur_bouclier) == 5:
                index_bouclier = (index_bouclier + 1) % len(bouclier_animation)
                compteur_bouclier = 0

            if index_bouclier == 2:

                index_bouclier = 0
                animation_bouclier_finie = True
                joueur_bouclier = False

            compteur_bouclier += 1

        if animation_bouclier_finie:
            fenetre.blit(bouclier_animation[2], perso_rect_bouclier)


        if int(compteur_attente) == 7:
            # Mettre à jour l'index de l'animation d'attente
            index_attente = (index_attente + 1) % len(animation_attente)
            compteur_attente = 0

        if int(compteur_marche) == 5:
            # Mettre à jour l'index de l'animation de marche
            index_marche = (index_marche + 1) % len(animation_marche)
            compteur_marche = 0


        if int(compteur_attaque) == 5:
            # Mettre à jour l'index de l'animation d'attaque
            index_attaque = (index_attaque + 1) % len(animation_attaque)
            compteur_attaque = 0

            # Vérifier si l'animation d'attaque est terminée
            if index_attaque == 0:
                attaque = False


        compteur_attente += 1
        compteur_marche += 1

        if attaque:
            compteur_attaque += 1


        if int(compteur_attente_boss) == 5:
            index_boss_attente = (index_boss_attente + 1) % len(boss_animation_attente)
            compteur_attente_boss = 0

        compteur_attente_boss += 1

        if (pos_boss_x -  pos_perso_x) < 300 and (pos_boss_x -  pos_perso_x) > 50 and not attaque_deja_fait:

            boss_attaque = True
            temps_replis = pygame.time.get_ticks()

        if pygame.time.get_ticks() - temps_replis > 2000 and attaque_deja_fait:
            attaque_deja_fait = False

        if (pos_boss_x - pos_perso_x) >= 300:
            attaque_deja_fait = False


        if boss_est_attaque and not fini and animation_temps_debut > 0 and pygame.time.get_ticks() - animation_temps_debut >= 300 and vie_boss > 0:

            boss_rect = boss_animation_degats[index_boss_degats].get_rect(topleft=(pos_boss_x, pos_boss_y))
            fenetre.blit(boss_animation_degats[index_boss_degats], (boss_rect[0], boss_rect[1]))


            if int(compteur_degats_boss) == 5:
                index_boss_degats = (index_boss_degats + 1) % len(boss_animation_degats)
                compteur_degats_boss = 0

            if index_boss_degats == 3:
                boss_est_attaque = False

            compteur_degats_boss += 1

        elif boss_attaque and not attaque_deja_fait and not fini:

            boss_rect = boss_animation_attaque[index_boss_attaque].get_rect(topleft=(pos_boss_x, pos_boss_y))
            fenetre.blit(boss_animation_attaque[index_boss_attaque], (boss_rect[0], boss_rect[1]))

            if not perso_rect_bouclier.colliderect(boss_rect):
                pos_boss_x -= 6

            if int(compteur_attaque_boss) == 5:
                index_boss_attaque = (index_boss_attaque + 1) % len(boss_animation_attaque)
                compteur_attaque_boss = 0

            if index_boss_attaque == 4:
                compteur_attaque_boss = 0
                index_boss_attaque = 0
                boss_attaque = False
                attaque_deja_fait = True

            compteur_attaque_boss += 1

        elif vie_boss > 0:
            boss_rect = boss_animation_attente[index_boss_attente].get_rect(topleft=(pos_boss_x, pos_boss_y))
            fenetre.blit(boss_animation_attente[index_boss_attente], (boss_rect[0], boss_rect[1]))

        if pos_boss_x != 650 and temps_replis > 0 and pygame.time.get_ticks() - temps_replis >= 2500:

            if pos_boss_x <=650:
                pos_boss_x += 2


        if boss_attaque and perso_rect.colliderect(boss_rect) and not fini and not attaque and not joueur_est_attaque and not fini and not joueur_est_attaque and not animation_bouclier_finie:
            vie_perso -= 20
            joueur_est_attaque = True


        if vie_boss == 0:

            if not fini:

                boss_rect = boss_animation_mort[index_boss_mort].get_rect(topleft=(pos_boss_x, pos_boss_y))
                fenetre.blit(boss_animation_mort[index_boss_mort], (boss_rect[0], boss_rect[1]))

                if int(compteur_boss_mort) == 10:
                    index_boss_mort = (index_boss_mort + 1) % len(boss_animation_mort)
                    compteur_boss_mort = 0

            compteur_boss_mort += 1

            if index_boss_mort == 6:
                fini = True
                fenetre.blit(boss_animation_mort[6], (boss_rect[0], boss_rect[1]))

        if vie_perso <= 0:

            if not fini:

                if derniere_direction == "droite":

                    fenetre.blit(animation_mort[index_mort], perso_rect)
                else:

                    fenetre.blit(pygame.transform.flip(animation_mort[index_mort], True, False), perso_rect)

                if int(compteur_mort) == 6:
                    index_mort = (index_mort + 1) % len(animation_mort)
                    compteur_mort = 0

            compteur_mort += 1

            if index_mort == 11:
                fini = True
                fenetre.blit(animation_mort[11], perso_rect)

        pygame.display.flip()
import constantes as c
import random as r
import pygame
from Frame import Frame
pygame.init()
class LevelPink(Frame):
    pausable = True
    def __init__(self):

        # chargement de l'arrière plan
        self.arriere_plan = pygame.image.load("assets/images/level1/background.png").convert_alpha()


        # -------------------- ANIMATIONS JOUEUR ---------------------
        # Feuille des animations personnage level
        sprite_sheet = pygame.image.load("assets/images/personnage/level/char_sheet.png").convert_alpha()

        # dimensions de chaque case de la feuille des sprites
        sprite_width = 56
        sprite_height = 56

        # animation attente personnage
        self.animation_attente = []
        for i in range(6):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, 0, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_attente.append(sprite.convert_alpha())

        # animation marche personnage
        self.animation_marche = []
        for i in range(8):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i*sprite_width, sprite_height*2, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_marche.append(sprite.convert_alpha())

        # animation attaque personnage
        self.animation_attaque = []
        for i in range(8):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 1, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_attaque.append(sprite.convert_alpha())


        # animation dégats personnage
        self.animation_degat = []
        for i in range(4):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 5, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_degat.append(sprite.convert_alpha())

        # animation de mort personnage
        self.animation_mort = []
        for i in range(8):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 6, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_mort.append(sprite.convert_alpha())
        for i in range(4):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 7, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.animation_mort.append(sprite.convert_alpha())

        # animation bouclier personnage
        self.bouclier_animation = []
        for i in range(3):
            sprite = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
            sprite.blit(sprite_sheet, (0, 0), (i * sprite_width, sprite_height * 10, sprite_width, sprite_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
            self.bouclier_animation.append(sprite.convert_alpha())

        # animation de saut personnage
        self.sprite_saut = pygame.Surface([sprite_width, sprite_height], pygame.SRCALPHA)
        self.sprite_saut.blit(sprite_sheet, (0, 0), (sprite_width*7, sprite_height*3, sprite_width, sprite_height))
        self.sprite_saut = pygame.transform.scale(self.sprite_saut, (self.sprite_saut.get_width() * 3, self.sprite_saut.get_height() * 3))  # Ajuster la taille du sprite


        # Victoire joeur
        self.victoire_joueur = pygame.image.load("assets/images/level1/you_win.png").convert_alpha()

        # Init index personnage
        self.index_attente = 0
        self.index_marche = 0
        self.index_attaque = 0
        self.index_degat = 0
        self.index_mort = 0
        self.index_bouclier = 0

        # -------------------- ANIMATIONS BOSS ---------------------
        # Feuille des animations boss level
        boss_sheet = pygame.image.load("assets/images/boss/level/boss_sheet.png").convert_alpha()

        # dimensions de chaque case de la feuille des sprites
        boss_width = 64
        boss_height = 64

        # animation attente boss
        self.boss_animation_attente = []
        for i in range(6):
            sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
            sprite.blit(boss_sheet, (0, 0), (i*boss_width, 0, boss_width, boss_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            self.boss_animation_attente.append(sprite.convert_alpha())

        # animation degats boss
        self.boss_animation_degats = []
        for i in range(4):
            sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
            sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height*2, boss_width, boss_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            self.boss_animation_degats.append(sprite.convert_alpha())

        # animation mort boss
        self.boss_animation_mort = []
        for i in range(7):
            sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
            sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height*3, boss_width, boss_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            self.boss_animation_mort.append(sprite.convert_alpha())

        # animation attaque boss
        self.boss_animation_attaque = []
        for i in range(5):
            sprite = pygame.Surface([boss_width, boss_height], pygame.SRCALPHA)
            sprite.blit(boss_sheet, (0, 0), (i*boss_width, boss_height, boss_width, boss_height))
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            self.boss_animation_attaque.append(sprite.convert_alpha())

        # victoire boss
        self.victoire_boss = pygame.image.load("assets/images/level1/you_lose.png").convert_alpha()

        # index animations boss
        self.index_boss_attente = 0
        self.index_boss_degats = 0
        self.index_boss_mort = 0
        self.index_boss_attaque = 0


        # dictionnaire des touches pressées
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False}

        self.nb_attaque_bouclier = 0

        self.pos_perso_x = 0
        self.pos_perso_y = 385

        self.pos_boss_x = 625
        self.pos_boss_y = 425

        self.vie_boss = 300 # initialise la vie du boss à 300 HP
        self.vie_perso = 100 # initialise la vie du joueur à 100 HP

        self.compteur_attente = 0
        self.compteur_marche = 0
        self.compteur_attaque = 0
        self.compteur_degat = 0
        self.compteur_mort = 0
        self.compteur_bouclier = 0

        self.compteur_attente_boss = 0
        self.compteur_degats_boss = 0
        self.compteur_boss_mort = 0
        self.compteur_attaque_boss = 0

        self.animation_temps_debut = 0

        self.compteur_saut = 0
        self.max_saut = 17

        self.temps_replis = 0

        self.derniere_direction = "droite"

        self.victoire = ""
        self.temps_affichage = 0

        self.en_saut = False
        self.attaque = False

        self.joueur_est_attaque = False
        self.joueur_bouclier = False
        self.animation_bouclier_finie = False

        self.boss_est_attaque = False
        self.boss_attaque = False
        self.attaque_deja_fait = False





        # Import des barres de vie
        self.barre_boss = pygame.image.load("assets/images/boss/level/barre_de_vie.png").convert_alpha()
        self.rect_barre_boss = self.barre_boss.get_rect(topleft=(445, 35))

        self.barre_joueur = pygame.image.load("assets/images/personnage/level/barre_de_vie.png").convert_alpha()
        self.rect_barre_joueur = self.barre_joueur.get_rect(topleft=(70, 35))

        self.icone = pygame.image.load('assets/images/icone.png').convert_alpha()
        self.icone = pygame.transform.scale(self.icone, (self.icone.get_width() * 2, self.icone.get_height() * 2))

        self.icone_rect = self.icone.get_rect(center=(c.LARGEUR / 2, 40))


        self.fini = False
        self.ne_plus_afficher = False



    def verifyEvents(self,event):
        # Touches
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.touches_pressee["gauche"] = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.touches_pressee["droite"] = True
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and not self.en_saut and not self.joueur_bouclier and not self.animation_bouclier_finie and not self.fini:
                self.en_saut = True
                self.compteur_saut = self.max_saut

            if event.key == pygame.K_f and not self.attaque and not self.fini and not self.joueur_bouclier and not self.animation_bouclier_finie:
                self.attaque = True

                if self.perso_rect.colliderect(self.boss_rect):

                    self.index_boss_degats = 0
                    self.vie_boss -= 30
                    self.boss_est_attaque = True
                    self.animation_temps_debut = pygame.time.get_ticks()

            if event.key == pygame.K_b and not self.attaque and not self.fini and not self.joueur_bouclier:

                self.compteur_bouclier = 0
                self.joueur_bouclier = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.touches_pressee["gauche"] = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.touches_pressee["droite"] = False

            if event.key == pygame.K_b :

                self.joueur_bouclier = False
                self.animation_bouclier_finie = False
        
    def showUpdate(self):
        self.fenetre.blit(self.arriere_plan, (0, 0))

        couleur_barre_boss = (70, 199, 58)
        interieur_barre_boss = pygame.Rect(447, 39, int(self.vie_boss / 1.14), 7)

        self.couleur_barre_joueur = (204, 33, 0)
        self.interieur_barre_joueur = pygame.Rect(89, 39, int(self.vie_perso * 2.64), 7)

        pygame.draw.rect(self.fenetre, couleur_barre_boss, interieur_barre_boss)
        self.fenetre.blit(self.barre_boss, self.rect_barre_boss)

        pygame.draw.rect(self.fenetre, self.couleur_barre_joueur, self.interieur_barre_joueur)
        self.fenetre.blit(self.barre_joueur, self.rect_barre_joueur)

        self.fenetre.blit(self.icone, self.icone_rect)


        self.perso_rect = self.animation_attente[0].get_rect(topleft=(self.pos_perso_x, self.pos_perso_y))
        self.perso_rect_bouclier = self.animation_attente[0].get_rect(topleft=(self.pos_perso_x, self.pos_perso_y))
        self.perso_rect[2] = 150
        self.perso_rect_bouclier[2] = 120

        # Musique level
        if c.musique == False:
            pygame.mixer.music.pause()

        if not self.fini :
            if c.musique:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("assets/sons/musique/levels.wav")
                    pygame.mixer.music.play(-1)

        
        self.bordures_verif_droite = self.pos_perso_x >= 0
        self.bordures_verif_gauche = self.pos_perso_x <= 632

        if self.touches_pressee["gauche"] and self.bordures_verif_droite and not self.touches_pressee["droite"] and not self.fini:

            if not self.joueur_bouclier and not self.animation_bouclier_finie:
                self.pos_perso_x = self.pos_perso_x - 4
            else :
                self.pos_perso_x -= 1

            if self.joueur_bouclier or self.animation_bouclier_finie:
                self.derniere_direction = "droite"
            else:
                self.derniere_direction = "gauche"

            if not self.en_saut and not self.attaque and not self.joueur_est_attaque and not self.animation_bouclier_finie and not self.joueur_bouclier:
                # Afficher le sprite de l'animation de marche inversée
                self.fenetre.blit(pygame.transform.flip(self.animation_marche[self.index_marche], True, False), self.perso_rect)

        elif self.touches_pressee["droite"] and self.bordures_verif_gauche and not self.touches_pressee["gauche"] and not self.fini:

            if not self.pos_boss_x - self.pos_perso_x <= self.perso_rect_bouclier[2]:

                if not self.joueur_bouclier and not self.animation_bouclier_finie:
                    self.pos_perso_x += 4
                else:
                    self.pos_perso_x += 1
                self.derniere_direction = "droite"

            if not self.en_saut and not self.attaque and not self.joueur_est_attaque and not self.animation_bouclier_finie and not self.joueur_bouclier :

                # Afficher le sprite de l'animation de marche
                self.fenetre.blit(self.animation_marche[self.index_marche], self.perso_rect)

        else:

            if self.derniere_direction == "droite":
                if not self.en_saut and not self.attaque and not self.joueur_est_attaque and not self.joueur_bouclier and not self.animation_bouclier_finie:
                    # Afficher le sprite de l'animation d'attente
                    self.fenetre.blit(self.animation_attente[self.index_attente], self.perso_rect)
            else:

                if not self.en_saut and not self.attaque and not self.joueur_est_attaque and not self.joueur_bouclier and not self.animation_bouclier_finie:
                    self.fenetre.blit(pygame.transform.flip(self.animation_attente[self.index_attente], True, False), self.perso_rect)


        if self.attaque and not self.fini and not self.joueur_est_attaque:

            if not self.en_saut:
                if self.derniere_direction == "droite":
                    self.fenetre.blit(self.animation_attaque[self.index_attaque], self.perso_rect)
                else:
                    self.fenetre.blit(pygame.transform.flip(self.animation_attaque[self.index_attaque], True, False), self.perso_rect)

        # Gestion du saut
        if self.en_saut and not self.fini:

            self.pos_perso_y -= self.compteur_saut
            if self.compteur_saut > -self.max_saut:
                self.compteur_saut -= 1
            else:
                self.en_saut = False



            if self.derniere_direction == "droite" :
                # Afficher l'image de saut
                self.fenetre.blit(self.sprite_saut, self.perso_rect)
            else:
                self.fenetre.blit(pygame.transform.flip(self.sprite_saut, True, False), self.perso_rect)

        if self.joueur_est_attaque and not self.en_saut and self.vie_perso > 0:

            if self.derniere_direction == "droite":
                self.fenetre.blit(self.animation_degat[self.index_degat], self.perso_rect)
            else:
                self.fenetre.blit(pygame.transform.flip(self.animation_degat[self.index_degat], True, False), self.perso_rect)

            if int(self.compteur_degat) == 5:
                # Mettre à jour l'index de l'animation de degat
                self.index_degat = (self.index_degat + 1) % len(self.animation_degat)
                self.compteur_degat = 0

            if self.index_degat == 3:
                self.index_degat = 0
                self.joueur_est_attaque = False


            self.compteur_degat += 1

        if self.joueur_bouclier and not self.en_saut and self.vie_perso > 0 and not self.fini and not self.joueur_est_attaque:


            self.fenetre.blit(self.bouclier_animation[self.index_bouclier], self.perso_rect_bouclier)


            if int(self.compteur_bouclier) == 5:
                self.index_bouclier = (self.index_bouclier + 1) % len(self.bouclier_animation)
                self.compteur_bouclier = 0

            if self.index_bouclier == 2:

                self.index_bouclier = 0
                self.animation_bouclier_finie = True
                self.joueur_bouclier = False

            self.compteur_bouclier += 1

        if self.animation_bouclier_finie:
            self.fenetre.blit(self.bouclier_animation[2], self.perso_rect_bouclier)
            self.derniere_direction == "droite"


        if int(self.compteur_attente) == 7:
            # Mettre à jour l'index de l'animation d'attente
            self.index_attente = (self.index_attente + 1) % len(self.animation_attente)
            self.compteur_attente = 0

        if int(self.compteur_marche) == 5:
            # Mettre à jour l'index de l'animation de marche
            self.index_marche = (self.index_marche + 1) % len(self.animation_marche)
            self.compteur_marche = 0


        if int(self.compteur_attaque) == 5:
            # Mettre à jour l'index de l'animation d'attaque
            self.index_attaque = (self.index_attaque + 1) % len(self.animation_attaque)
            self.compteur_attaque = 0

            # Vérifier si l'animation d'attaque est terminée
            if self.index_attaque == 0:
                self.attaque = False


        self.compteur_attente += 1
        self.compteur_marche += 1

        if self.attaque:
            self.compteur_attaque += 1

        if int(self.compteur_attente_boss) == 5:
            self.index_boss_attente = (self.index_boss_attente + 1) % len(self.boss_animation_attente)
            self.compteur_attente_boss = 0

        self.compteur_attente_boss += 1

        if (self.pos_boss_x -  self.pos_perso_x) < 300 and (self.pos_boss_x -  self.pos_perso_x) > 50 and not self.attaque_deja_fait:

            self.boss_attaque = True
            self.temps_replis = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.temps_replis > r.randint(1000, 2000) and self.attaque_deja_fait:
            self.attaque_deja_fait = False

        if (self.pos_boss_x - self.pos_perso_x) >= 300:
            self.attaque_deja_fait = False


        if self.boss_est_attaque and not self.fini and self.animation_temps_debut > 0 and pygame.time.get_ticks() - self.animation_temps_debut >= 300 and self.vie_boss > 0:

            self.boss_rect = self.boss_animation_degats[self.index_boss_degats].get_rect(topleft=(self.pos_boss_x, self.pos_boss_y))
            self.fenetre.blit(self.boss_animation_degats[self.index_boss_degats], (self.boss_rect[0], self.boss_rect[1]))


            if int(self.compteur_degats_boss) == 5:
                self.index_boss_degats = (self.index_boss_degats + 1) % len(self.boss_animation_degats)
                self.compteur_degats_boss = 0

            if self.index_boss_degats == 3:
                self.boss_est_attaque = False

            self.compteur_degats_boss += 1

        elif self.boss_attaque and not self.attaque_deja_fait and not self.fini:

            self.boss_rect = self.boss_animation_attaque[self.index_boss_attaque].get_rect(topleft=(self.pos_boss_x, self.pos_boss_y))
            self.fenetre.blit(self.boss_animation_attaque[self.index_boss_attaque], (self.boss_rect[0], self.boss_rect[1]))

            if not self.perso_rect_bouclier.colliderect(self.boss_rect) and self.pos_boss_x >= 350:
                self.pos_boss_x -= 6



            if int(self.compteur_attaque_boss) == 5:
                self.index_boss_attaque = (self.index_boss_attaque + 1) % len(self.boss_animation_attaque)
                self.compteur_attaque_boss = 0

            if self.index_boss_attaque == 4:
                self.compteur_attaque_boss = 0
                self.index_boss_attaque = 0
                self.boss_attaque = False
                self.attaque_deja_fait = True

            self.compteur_attaque_boss += 1

        elif self.vie_boss > 0:
            self.boss_rect = self.boss_animation_attente[self.index_boss_attente].get_rect(topleft=(self.pos_boss_x, self.pos_boss_y))
            self.fenetre.blit(self.boss_animation_attente[self.index_boss_attente], (self.boss_rect[0], self.boss_rect[1]))

        if self.pos_boss_x != 625 and self.temps_replis > 0 and pygame.time.get_ticks() - self.temps_replis >= 2500:

            if self.pos_boss_x <=625:
                self.pos_boss_x += 2


        if self.boss_attaque and self.perso_rect.colliderect(self.boss_rect) and not self.fini and not self.attaque and not self.joueur_est_attaque and not self.animation_bouclier_finie:
            self.vie_perso -= 10
            self.joueur_est_attaque = True


        if self.vie_boss == 0:

            if not self.fini:

                self.boss_rect = self.boss_animation_mort[self.index_boss_mort].get_rect(topleft=(self.pos_boss_x, self.pos_boss_y))
                self.fenetre.blit(self.boss_animation_mort[self.index_boss_mort], (self.boss_rect[0], self.boss_rect[1]))

                if int(self.compteur_boss_mort) == 10:
                    self.index_boss_mort = (self.index_boss_mort + 1) % len(self.boss_animation_mort)
                    self.compteur_boss_mort = 0

            self.compteur_boss_mort += 1

            if self.index_boss_mort == 6:
                self.fini = True
                self.fenetre.blit(self.boss_animation_mort[6], (self.boss_rect[0], self.boss_rect[1]))
                self.victoire = "joueur"
                self.image_blur = self.fenetre.copy()
                self.image_blur = pygame.transform.box_blur(self.image_blur, 10, repeat_edge_pixels=True)
                self.temps_affichage = pygame.time.get_ticks()
                self.index_boss_mort = 0

        if self.vie_perso <= 0:

            if not self.fini:

                if self.derniere_direction == "droite":

                    self.fenetre.blit(self.animation_mort[self.index_mort], self.perso_rect)

                else:

                    self.fenetre.blit(pygame.transform.flip(self.animation_mort[self.index_mort], True, False), self.perso_rect)

                if int(self.compteur_mort) == 6:
                    self.index_mort = (self.index_mort + 1) % len(self.animation_mort)
                    self.compteur_mort = 0

            self.compteur_mort += 1

            if self.index_mort == 11:

                self.fini = True
                self.fenetre.blit(self.animation_mort[11], self.perso_rect)
                self.victoire = "boss"
                self.temps_affichage = pygame.time.get_ticks()
                self.image_blur = self.fenetre.copy()
                self.image_blur = pygame.transform.box_blur(self.image_blur, 10, repeat_edge_pixels=True)
                self.index_mort = 0

        # Titre de victoire ou defaite
        if self.fini and not self.ne_plus_afficher:

            if self.victoire == "boss" :
                self.fenetre.blit(self.image_blur, (0, 0))
                self.fenetre.blit(self.victoire_boss, (0, 0))

            elif self.victoire == "joueur":
                self.fenetre.blit(self.image_blur, (0, 0))
                self.fenetre.blit(self.victoire_joueur, (0, 0))

        if pygame.time.get_ticks() - self.temps_affichage >= 5000 and self.fini:
            self.ne_plus_afficher = True

        if self.ne_plus_afficher:

            if c.musique:
                pygame.mixer.music.fadeout(500)
                pygame.mixer.music.unload()

            c.game_state = "lobby"

        
    
    def pause(self):
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False}
        return self.fenetre.copy()

    def unpause(self):
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False}
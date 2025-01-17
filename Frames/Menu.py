import constantes as c
from Button import *
import pygame
from Frame import Frame
pygame.init()

class Menu(Frame):
    def __init__(self):
        # brillance du logo
        self.animation_logo = [f"assets/images/logo_animation/logo_0{i}.png" for i in range(10)]
        self.animation_logo.append("assets/images/logo_animation/logo_10.png")
        self.animation_logo.append("assets/images/logo_animation/logo_11.png")
        self.animation_logo.append("assets/images/logo_animation/logo_12.png")

        self.index_animation = 0
        self.compteur_animation = 0
        self.animation_terminee = False

        self.temps_derniere_animation = pygame.time.get_ticks()

        # Charger l'image d'ombre
        self.ombre = pygame.image.load('assets/images/logo_ombre.png')
        self.ombre = pygame.transform.scale(self.ombre, (self.ombre.get_width() * 0.5, self.ombre.get_height() * 0.5))

        self.bouton_jouer = Button(c.bouton_background, 'Jouer', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 273)
        self.bouton_parametres = Button(c.bouton_background, 'Paramètres', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 353)
        self.bouton_quitter = Button(c.bouton_background, 'Quitter', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 433)


    

    def verifyEvents(self,event):
        # Si l'utilisateur clique avec la souris, vérifier les boutons
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Si le bouton jouer est cliqué, changer l'état du jeu
            if self.bouton_jouer.getHitbox().collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.fadeout(500)
                c.game_state = "lobby"


            # Si le bouton paramètres est cliqué, changer l'état du jeu
            if self.bouton_parametres.getHitbox().collidepoint(mouse_x, mouse_y):

                c.game_state = "setting"

            # Si le bouton quitter est cliqué, quitter le jeu
            if self.bouton_quitter.getHitbox().collidepoint(mouse_x, mouse_y):
                c.running = False

    def showUpdate(self):

        if c.musique:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sons/musique/menu_titre.wav")
                pygame.mixer.music.play(-1)

        else:
            pygame.mixer.music.pause()

        self.fenetre.blit(c.fond, (0, 0))

        logo = pygame.image.load(self.animation_logo[self.index_animation])
        logo = pygame.transform.scale(logo, (logo.get_width() * 0.5, logo.get_height() * 0.5))

        # Afficher l'ombre
        self.fenetre.blit(self.ombre, self.ombre.get_rect(
            center=(c.LARGEUR // 2 + 3, 150 + 3)))  # décalage de 3 pixels vers le bas et à droite

        self.fenetre.blit(logo, logo.get_rect(center=(c.LARGEUR//2, 150)))

        self.bouton_jouer.show(self.fenetre)
        self.bouton_parametres.show(self.fenetre)
        self.bouton_quitter.show(self.fenetre)
            
        # Pour les animations
        if self.compteur_animation == 5 and not self.animation_terminee:
            self.index_animation += 1
            self.compteur_animation = 0

        if not self.animation_terminee:
            self.compteur_animation += 1

        if self.index_animation >= len(self.animation_logo):
            self.index_animation = 0

            self.animation_terminee = True

        if self.animation_terminee:

            if pygame.time.get_ticks() - self.temps_derniere_animation >= 4000:
                self.animation_terminee = False
                self.temps_derniere_animation = pygame.time.get_ticks()

    def firstAction(self):
        pass

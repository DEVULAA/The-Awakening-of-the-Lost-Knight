import constantes as c
from Button import *
import pygame
from Frame import Frame
pygame.init()
class Lobby(Frame):
    pausable = True
    def __init__(self):

        self.carte = c.carte
        self.carte = pygame.transform.scale(self.carte, (self.carte.get_width() * 3, self.carte.get_height() * 3))

        self.current_frame_dos = 0
        self.current_frame_face = 0
        self.current_frame_droite = 0
        self.current_frame_gauche = 0
        self.derniere_direction = "haut"

        self.compteur_animation = 0
        self.vitesse_animation = 4

        self.eau_nb_images = 4
        self.eau_duree = 1600
        self.eau_laps = self.eau_duree // self.eau_nb_images
        self.eau_index = 0
        pygame.time.set_timer(pygame.USEREVENT, self.eau_laps)

        self.carte_masque = pygame.image.load("assets/images/map_mask.png").convert_alpha()
        self.carte_masque = pygame.transform.scale(self.carte_masque, (self.carte_masque.get_width() * 3, self.carte_masque.get_height() * 3))

        self.carte_masque_mask = pygame.mask.from_surface(self.carte_masque)

        self.personnage_mask = pygame.mask.from_surface(c.personnage_dos)

        self.dos_animation = [c.personnage_dos, c.personnage_dos_marche1, c.personnage_dos_marche2]
        self.face_animation = [c.personnage_face, c.personnage_face_marche1, c.personnage_face_marche2]
        self.droite_animation = [c.personnage_droite, c.personnage_droite_marche1, c.personnage_droite_marche2]
        self.gauche_animation = [c.personnage_gauche, c.personnage_gauche_marche1, c.personnage_gauche_marche2]

        self.eau_animation = [c.eau_1, c.eau_2, c.eau_3, c.eau_4]

        self.ombre = pygame.image.load("assets/images/personnage/shadow.png").convert_alpha()
        self.ombre = pygame.transform.scale(self.ombre, (self.ombre.get_width() * 2.5, self.ombre.get_height() * 2.5))


        self.bouton_shop = pygame.image.load("assets/images/shop.png").convert_alpha()
        self.bouton_shop = pygame.transform.scale(self.bouton_shop, (self.bouton_shop.get_width() * 3, self.bouton_shop.get_height() * 3))
        self.rect_bouton_shop = self.bouton_shop.get_rect(topright=(c.LARGEUR - 8, 8))

        # Création de l'ombre
        self.ombre_bouton_shop = self.bouton_shop.copy()  # Crée une copie de l'image du bouton shop
        self.ombre_bouton_shop.fill((0, 0, 0, 50), special_flags=pygame.BLEND_RGBA_MULT)  # Remplit l'image avec la couleur de l'ombre  # Applique une ombre semi-transparente

        # Création de l'image du bouton shop lorsqu'il est survolé
        self.bouton_shop_hover = pygame.transform.scale(self.bouton_shop, (self.bouton_shop.get_width() + 3, self.bouton_shop.get_height() + 3))  # Augmente la taille de l'image de 3 pixels


        # Création de l'image du bouton level
        self.bouton_level = pygame.image.load("assets/images/bouton_level.png").convert_alpha()
        self.bouton_level = pygame.transform.scale(self.bouton_level, (self.bouton_level.get_width() * 4, self.bouton_level.get_height() * 4))

        self.rect_personnage = c.personnage_dos.get_rect(center=(c.pos_personnage))
        self.rect_personnage[1] += 50
        self.rect_personnage[3] = 30

        self.chat_background = pygame.image.load("assets/images/chat_background.png").convert_alpha()
        self.chat_background = pygame.transform.scale(self.chat_background, (self.chat_background.get_width() * 1.75, self.chat_background.get_height() * 1.75))
        self.rect_chat_background = self.chat_background.get_rect(center=(c.LARGEUR / 2, c.HAUTEUR - 100))

        self.touches_pressee = {"gauche": False, "droite": False, "haut": False, "bas": False}

        self.offset_carte = [c.LARGEUR + 1500, c.HAUTEUR - 1200]

        self.objets = []

    def update_collisions(self):
        self.rect_chateau_sable = c.chateau_sable.get_rect(center=(self.offset_carte[0] - 2300, self.offset_carte[1] + 1000))
        self.rect_caisse1 = c.caisse.get_rect(center=(self.offset_carte[0] - 2100, self.offset_carte[1] + 1200))
        self.rect_caisse2 = c.caisse.get_rect(center=(self.offset_carte[0] - 2170, self.offset_carte[1] + 1170))
        self.rect_palmier = c.palmier.get_rect(center=(self.offset_carte[0] - 2200, self.offset_carte[1] + 850))

        self.rect_arbre = c.arbre.get_rect(center=(self.offset_carte[0] - 1500, self.offset_carte[1] + 850))
        self.rect_arbre[1] += 95
        self.rect_arbre[3] = 80

        self.pos_arbre = c.arbre.get_rect(center=(self.offset_carte[0] - 1500, self.offset_carte[1] + 850))

        self.rect_arbre_haut = c.arbre_haut.get_rect(center=(self.offset_carte[0] - 1500, self.offset_carte[1] + 850))


        self.objets = [self.rect_chateau_sable, self.rect_palmier, self.rect_caisse1, self.rect_caisse2, self.rect_arbre]  # liste des collisions
        

    def verifyEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                
            #Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #Si le bouton jouer est cliqué, changer l'état du jeu
            if self.rect_bouton_shop.collidepoint(mouse_x, mouse_y):
                c.game_state = "shop"
                
        # Touches
        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.touches_pressee["gauche"] = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.touches_pressee["droite"] = True
            elif event.key == pygame.K_UP or event.key == pygame.K_z:
                self.touches_pressee["haut"] = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.touches_pressee["bas"] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                self.touches_pressee["gauche"] = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.touches_pressee["droite"] = False
            elif event.key == pygame.K_UP or event.key == pygame.K_z:
                self.touches_pressee["haut"] = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.touches_pressee["bas"] = False

        if event.type == pygame.USEREVENT:
            self.eau_index = (self.eau_index + 1) % self.eau_nb_images
        
    def showUpdate(self):
        if c.musique:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sons/musique/lobby.wav")
                pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.pause()

        
        self.fenetre.blit(self.eau_animation[self.eau_index], c.eau_1.get_rect(center=(self.offset_carte)))
        self.fenetre.blit(self.carte, self.carte.get_rect(center=(self.offset_carte))) #Affichage de la carte

        self.rect_bouton_level = self.bouton_level.get_rect(center=(self.offset_carte[0] + 850, self.offset_carte[1] + 2))

        self.fenetre.blit(self.bouton_level, self.rect_bouton_level)

        self.fenetre.blit(self.ombre,
                    self.ombre.get_rect(
                         center=(c.LARGEUR // 2, (c.HAUTEUR // 2) + (c.personnage_dos.get_height() + 5) // 2)))



        # Collisions
        self.update_collisions()

        self.fenetre.blit(c.chateau_sable, self.rect_chateau_sable)
        self.fenetre.blit(c.caisse, self.rect_caisse1)
        self.fenetre.blit(c.caisse, self.rect_caisse2)
        self.fenetre.blit(c.palmier, self.rect_palmier)
        self.fenetre.blit(c.arbre, self.pos_arbre)

        if not c.pause and not c.est_menu:

            #Affichage du bouton shop
            if self.rect_bouton_shop.collidepoint(pygame.mouse.get_pos()):  # Si la souris est sur le bouton shop
            
                self.fenetre.blit(self.bouton_shop_hover, self.rect_bouton_shop.move(-1,
                                                                      -1))  # Affiche la version agrandie du bouton shop, décalée de 1 pixel vers la gauche et vers le haut pour centrer l'agrandissement
            else:
                self.fenetre.blit(self.bouton_shop, self.rect_bouton_shop)
                self.fenetre.blit(self.ombre_bouton_shop, (self.rect_bouton_shop.x + 3, self.rect_bouton_shop.y + 3))

            if self.touches_pressee["gauche"]:

                self.offset_carte[0] += 7

                if self.compteur_animation % self.vitesse_animation == 0:
                    self.current_frame_gauche = (self.current_frame_gauche + 1) % len(self.gauche_animation)
                self.fenetre.blit(self.gauche_animation[self.current_frame_gauche],
                             c.personnage_gauche.get_rect(center=(c.pos_personnage)))

                self.derniere_direction = "gauche"

            elif self.touches_pressee["droite"]:

                self.offset_carte[0] -= 7

                if self.compteur_animation % self.vitesse_animation == 0:
                    self.current_frame_droite = (self.current_frame_droite + 1) % len(self.droite_animation)
                self.fenetre.blit(self.droite_animation[self.current_frame_droite], c.personnage_droite.get_rect(center=(c.pos_personnage)))

                self.derniere_direction = "droite"

            elif self.touches_pressee["haut"]:

                self.offset_carte[1] += 7

                if self.compteur_animation % self.vitesse_animation == 0:
                    self.current_frame_dos = (self.current_frame_dos + 1) % len(self.dos_animation)
                self.fenetre.blit(self.dos_animation[self.current_frame_dos],
                                c.personnage_face.get_rect(center=(c.pos_personnage)))  # Affichage du personnage

                self.derniere_direction = "haut"

            elif self.touches_pressee["bas"]:
                self.offset_carte[1] -= 7

                if self.compteur_animation % self.vitesse_animation == 0:
                    self.current_frame_face = (self.current_frame_face + 1) % len(self.face_animation)
                self.fenetre.blit(self.face_animation[self.current_frame_face],
                             c.personnage_face.get_rect(center=(c.pos_personnage)))  # Affichage du personnage


                self.derniere_direction = "bas"

            else: #Aucune touche n'est enfoncée

                if self.derniere_direction == "haut":
                    self.fenetre.blit(self.dos_animation[0], c.personnage_face.get_rect(center=(c.pos_personnage)))

                elif self.derniere_direction == "bas":
                    self.fenetre.blit(self.face_animation[0], c.personnage_face.get_rect(center=(c.pos_personnage)))

                elif self.derniere_direction == "gauche":
                    self.fenetre.blit(c.personnage_gauche, c.personnage_gauche.get_rect(center=(c.pos_personnage)))

                elif self.derniere_direction == "droite":
                    self.fenetre.blit(c.personnage_droite, c.personnage_droite.get_rect(center=(c.pos_personnage)))

            # Collisions
            for objet in self.objets:

                if self.rect_personnage.colliderect(objet):
                    # Collision détectée, annule le déplacement dans la direction correspondante
                    if self.touches_pressee["gauche"] and self.derniere_direction == "gauche" and c.determinerCote(
                            self.rect_personnage, objet) == "gauche":
                        self.offset_carte[0] -= 7
                    elif self.touches_pressee["droite"] and self.derniere_direction == "droite" and c.determinerCote(
                            self.rect_personnage, objet) == "droite":
                        self.offset_carte[0] += 7
                    elif self.touches_pressee["haut"] and self.derniere_direction == "haut" and c.determinerCote(self.rect_personnage,
                                                                                                       objet) == "bas":
                        self.offset_carte[1] -= 7
                    elif self.touches_pressee["bas"] and self.derniere_direction == "bas" and c.determinerCote(self.rect_personnage,
                                                                                                     objet) == "haut":
                        self.offset_carte[1] += 7

            # Si le personnage est sur le bouton du 1er niveau

            if self.rect_bouton_level.colliderect(self.rect_personnage):

                self.fenetre.blit(self.chat_background, self.rect_chat_background) # Afficher la bulle de texte

                if pygame.key.get_pressed()[pygame.K_SPACE]:

                    pygame.mixer.music.fadeout(500)
                    c.game_state = "level_pink"

            if self.carte.get_rect(center=(self.offset_carte))[0] >= 0:
                self.offset_carte[0] -= 7 #gauche

            if self.carte.get_rect(center=(self.offset_carte))[1] >= 0 :
                self.offset_carte[1] -= 7 #haut

            if self.carte.get_rect(center=(self.offset_carte))[1] <= -2640 :
                self.offset_carte[1] += 7 #bas

            if self.carte.get_rect(center=(self.offset_carte))[0] <= -4960 or self.carte.get_rect(center=(self.offset_carte))[0] <= -3485:
                self.offset_carte[0] += 7 #droite



        # Objets dessus le personnage
        self.fenetre.blit(c.arbre_haut, self.rect_arbre_haut)

        self.compteur_animation += 1


    def firstAction(self):
        print("first action")
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False, "bas": False}
        if c.musique:
            pygame.mixer.music.unload()
            pygame.mixer.music.load("assets/sons/musique/lobby_intro.wav")
            pygame.mixer.music.play()


    
    def pause(self):
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False, "bas": False}
        return self.fenetre.copy()

    def unpause(self):
        self.touches_pressee = {"gauche": False, "droite": False, "haut": False, "bas": False}
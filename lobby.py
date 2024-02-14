import pygame
import constantes as c
# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# Chargement de la carte
carte = c.carte
carte = pygame.transform.scale(carte, (carte.get_width() * 3, carte.get_height() * 3))


dos_animation = [c.personnage_dos, c.personnage_dos_marche1, c.personnage_dos_marche2]
face_animation = [c.personnage_face, c.personnage_face_marche1, c.personnage_face_marche2]
droite_animation = [c.personnage_droite, c.personnage_droite_marche1, c.personnage_droite_marche2]
gauche_animation = [c.personnage_gauche, c.personnage_gauche_marche1, c.personnage_gauche_marche2]


eau_animation = [c.eau_1, c.eau_2, c.eau_3, c.eau_4]

ombre = pygame.image.load("assets/images/personnage/shadow.png")
ombre = pygame.transform.scale(ombre, (ombre.get_width() * 2.5, ombre.get_height() * 2.5))

bouton_shop = pygame.image.load("assets/images/shop.png").convert_alpha()
bouton_shop = pygame.transform.scale(bouton_shop, (bouton_shop.get_width() * 3, bouton_shop.get_height() * 3))
rect_bouton_shop = bouton_shop.get_rect(topright=(c.LARGEUR - 8, 8))

# Création de l'ombre
ombre_bouton_shop = bouton_shop.copy()  # Crée une copie de l'image du bouton shop
ombre_bouton_shop.fill((0, 0, 0, 50), special_flags=pygame.BLEND_RGBA_MULT)  # Remplit l'image avec la couleur de l'ombre  # Applique une ombre semi-transparente

# Création de l'image du bouton shop lorsqu'il est survolé
bouton_shop_hover = pygame.transform.scale(bouton_shop, (bouton_shop.get_width() + 3, bouton_shop.get_height() + 3))  # Augmente la taille de l'image de 3 pixels

def principal():

    # Position de la carte
    offset_carte = [c.LARGEUR, c.HAUTEUR]

    offset_carte[0] += 1 # Update la carte pour qu'elle s'affiche
    fenetre.fill(c.BLANC)

    current_frame_dos = 0
    current_frame_face = 0
    current_frame_droite = 0
    current_frame_gauche = 0
    derniere_direction = "haut"

    compteur_animation = 0
    vitesse_animation = 6

    eau_nb_images = 4
    eau_duree = 1600
    eau_laps = eau_duree // eau_nb_images
    eau_index = 0
    pygame.time.set_timer(pygame.USEREVENT, eau_laps)



    while c.running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtenir la position de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Si le bouton jouer est cliqué, changer l'état du jeu
                if rect_bouton_shop.collidepoint(mouse_x, mouse_y):


                        import magasin
                        magasin.principal()  # Exécute la fonction principal() du module magasin

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    import menu_echap
                    menu_echap.principal()

            if event.type == pygame.USEREVENT:
                eau_index = (eau_index + 1) % eau_nb_images

        fenetre.blit(eau_animation[eau_index], c.eau_1.get_rect(center=(offset_carte)))
        fenetre.blit(carte, carte.get_rect(center=(offset_carte))) #Affichage de la carte

        fenetre.blit(ombre,
                     ombre.get_rect(center=(c.LARGEUR // 2, (c.HAUTEUR // 2) + (c.personnage_dos.get_height()+5) // 2)))

        fenetre.blit(ombre_bouton_shop, (rect_bouton_shop.x + 3, rect_bouton_shop.y + 3))
        fenetre.blit(bouton_shop, rect_bouton_shop)


        touches = pygame.key.get_pressed()


        if not c.pause and not c.est_menu:

            # Affichage du bouton shop
            if rect_bouton_shop.collidepoint(pygame.mouse.get_pos()):  # Si la souris est sur le bouton shop
                fenetre.blit(bouton_shop_hover, rect_bouton_shop.move(-1,
                                                                      -1))  # Affiche la version agrandie du bouton shop, décalée de 1 pixel vers la gauche et vers le haut pour centrer l'agrandissement
            else:
                fenetre.blit(bouton_shop, rect_bouton_shop)

            if touches[pygame.K_LEFT] or touches[pygame.K_q]:

                offset_carte[0] += 5

                if compteur_animation % vitesse_animation == 0:
                    current_frame_gauche = (current_frame_gauche + 1) % len(gauche_animation)
                fenetre.blit(gauche_animation[current_frame_gauche],
                             c.personnage_gauche.get_rect(center=(c.pos_personnage)))

                derniere_direction = "gauche"

            elif touches[pygame.K_RIGHT] or touches[pygame.K_d]:

                offset_carte[0] -= 5

                if compteur_animation % vitesse_animation == 0:
                    current_frame_droite = (current_frame_droite + 1) % len(droite_animation)
                fenetre.blit(droite_animation[current_frame_droite],
                             c.personnage_droite.get_rect(center=(c.pos_personnage)))

                derniere_direction = "droite"

            elif touches[pygame.K_UP] or touches[pygame.K_z]:

                offset_carte[1] += 5

                if compteur_animation % vitesse_animation == 0:
                    current_frame_dos = (current_frame_dos + 1) % len(dos_animation)
                fenetre.blit(dos_animation[current_frame_dos],
                                c.personnage_face.get_rect(center=(c.pos_personnage)))  # Affichage du personnage

                derniere_direction = "haut"

            elif touches[pygame.K_DOWN] or touches[pygame.K_s]:
                offset_carte[1] -= 5

                if compteur_animation % vitesse_animation == 0:
                    current_frame_face = (current_frame_face + 1) % len(face_animation)
                fenetre.blit(face_animation[current_frame_face],
                             c.personnage_face.get_rect(center=(c.pos_personnage)))  # Affichage du personnage


                derniere_direction = "bas"

            else: #Aucune touche n'est enfoncée

                if derniere_direction == "haut":
                    fenetre.blit(dos_animation[0], c.personnage_face.get_rect(center=(c.pos_personnage)))

                elif derniere_direction == "bas":
                    fenetre.blit(face_animation[0], c.personnage_face.get_rect(center=(c.pos_personnage)))

                elif derniere_direction == "gauche":
                    fenetre.blit(c.personnage_gauche, c.personnage_gauche.get_rect(center=(c.pos_personnage)))

                elif derniere_direction == "droite":
                    fenetre.blit(c.personnage_droite, c.personnage_droite.get_rect(center=(c.pos_personnage)))







        # Mettre à jour l'affichage
        pygame.display.flip()

        # Mets à jour les FPS
        pygame.time.Clock().tick(c.FPS)

        compteur_animation += 1


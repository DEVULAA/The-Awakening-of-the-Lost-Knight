import pygame
import constantes as c
# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# Chargement de la carte
carte = c.carte
carte = pygame.transform.scale(carte, (carte.get_width() * 5, carte.get_height() * 5))

dos_animation = [c.personnage_dos, c.personnage_dos_marche1, c.personnage_dos_marche2]
face_animation = [c.personnage_face, c.personnage_face_marche1, c.personnage_face_marche2]
droite_animation = [c.personnage_droite, c.personnage_droite_marche1, c.personnage_droite_marche2]
gauche_animation = [c.personnage_gauche, c.personnage_gauche_marche1, c.personnage_gauche_marche2]


def principal():

    # Position de la carte
    offset_carte = [(c.LARGEUR // 2) + 450, (c.HAUTEUR // 2) - 3980]

    offset_carte[0] += 1 # Update la carte pour qu'elle s'affiche
    fenetre.fill(c.BLANC)

    current_frame_dos = 0
    current_frame_face = 0
    current_frame_droite = 0
    current_frame_gauche = 0
    derniere_direction = "haut"

    compteur_animation = 0
    vitesse_animation = 6

    while c.running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                c.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    import menu_echap
                    menu_echap.principal()

        fenetre.blit(carte, carte.get_rect(center=(offset_carte))) #Affichage de la carte



        touches = pygame.key.get_pressed()


        if not c.pause:

            if touches[pygame.K_LEFT]:
                offset_carte[0] += 4

                if compteur_animation % vitesse_animation == 0:
                    current_frame_gauche = (current_frame_gauche + 1) % len(gauche_animation)
                fenetre.blit(gauche_animation[current_frame_gauche],
                             c.personnage_gauche.get_rect(center=(c.pos_personnage)))

                derniere_direction = "gauche"

            elif touches[pygame.K_RIGHT]:
                offset_carte[0] -= 4

                if compteur_animation % vitesse_animation == 0:
                    current_frame_droite = (current_frame_droite + 1) % len(droite_animation)
                fenetre.blit(droite_animation[current_frame_droite],
                             c.personnage_droite.get_rect(center=(c.pos_personnage)))



                derniere_direction = "droite"

            elif touches[pygame.K_UP]:
                offset_carte[1] += 4
                if compteur_animation % vitesse_animation == 0:
                    current_frame_dos = (current_frame_dos + 1) % len(dos_animation)
                fenetre.blit(dos_animation[current_frame_dos],
                                c.personnage_face.get_rect(center=(c.pos_personnage)))  # Affichage du personnage

                derniere_direction = "haut"

            elif touches[pygame.K_DOWN]:

                offset_carte[1] -= 4
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


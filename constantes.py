import pygame

FPS = 60

# couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# fenetre
LARGEUR = 800
HAUTEUR = 600

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
surface_pause = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)

game_state = ""

zoom_carte = 2

#assets
bouton_background = "assets/images/bouton_background.png"

# Chargement du personnage
personnage_dos = pygame.image.load("assets/images/personnage/Vu_dos.png")
personnage_dos = pygame.transform.scale(personnage_dos, (personnage_dos.get_width() * 3, personnage_dos.get_height() * 3))

personnage_dos_marche1 = pygame.image.load("assets/images/personnage/Pied_gauche_bas.png")
personnage_dos_marche1 = pygame.transform.scale(personnage_dos_marche1, (personnage_dos_marche1.get_width() * 3, personnage_dos_marche1.get_height() * 3))

personnage_dos_marche2 = pygame.image.load("assets/images/personnage/Pied_droit_bas.png")
personnage_dos_marche2 = pygame.transform.scale(personnage_dos_marche2, (personnage_dos_marche2.get_width() * 3, personnage_dos_marche2.get_height() * 3))

personnage_face = pygame.image.load("assets/images/personnage/Vu_face.png")
personnage_face = pygame.transform.scale(personnage_face, (personnage_face.get_width() * 3, personnage_face.get_height() * 3))

personnage_face_marche1 = pygame.image.load("assets/images/personnage/Vu_face_-_Pied_droit_bas.png")
personnage_face_marche1 = pygame.transform.scale(personnage_face_marche1, (personnage_face_marche1.get_width() * 3, personnage_face_marche1.get_height() * 3))

personnage_face_marche2 = pygame.image.load("assets/images/personnage/Vu_face_-_Pied_gauche_bas.png")
personnage_face_marche2 = pygame.transform.scale(personnage_face_marche2, (personnage_face_marche2.get_width() * 3, personnage_face_marche2.get_height() * 3))

personnage_droite = pygame.image.load("assets/images/personnage/Vu_cote_droite.png")
personnage_droite = pygame.transform.scale(personnage_droite, (personnage_droite.get_width() * 3, personnage_droite.get_height() * 3))

personnage_droite_marche1 = pygame.image.load("assets/images/personnage/Vu_cote_droite_-_pied_droit_arriere.png")
personnage_droite_marche1 = pygame.transform.scale(personnage_droite_marche1, (personnage_droite_marche1.get_width() * 3, personnage_droite_marche1.get_height() * 3))

personnage_droite_marche2 = pygame.image.load("assets/images/personnage/Vu_cote_droite_-_pied_gauche_arriere.png")
personnage_droite_marche2 = pygame.transform.scale(personnage_droite_marche2, (personnage_droite_marche2.get_width() * 3, personnage_droite_marche2.get_height() * 3))


personnage_gauche = pygame.image.load("assets/images/personnage/Vu_cote_gauche.png")
personnage_gauche = pygame.transform.scale(personnage_gauche, (personnage_gauche.get_width() * 3, personnage_gauche.get_height() * 3))

personnage_gauche_marche1 = pygame.image.load("assets/images/personnage/Vu_cote_gauche_-_pied_droite_arriere.png")
personnage_gauche_marche1 = pygame.transform.scale(personnage_gauche_marche1, (personnage_gauche_marche1.get_width() * 3, personnage_gauche_marche1.get_height() * 3))

personnage_gauche_marche2 = pygame.image.load("assets/images/personnage/Vu_cote_gauche_-_pied_gauche_arriere_.png")
personnage_gauche_marche2 = pygame.transform.scale(personnage_gauche_marche2, (personnage_gauche_marche2.get_width() * 3, personnage_gauche_marche2.get_height() * 3))


pos_personnage = (LARGEUR // 2, HAUTEUR // 2)

carte = pygame.image.load("assets/images/map.png")  # Assurez-vous de remplacer par le chemin de votre propre carte


pause = False



#running
running = True

#creer boutons
def creer_bouton(image, texte, taille_texte, couleur_texte, bouton_largeur, bouton_hauteur, pos_x, pos_y):

    font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", taille_texte)

    texte_surface = font.render(texte, True, couleur_texte)

    bouton_surface = pygame.Surface((bouton_largeur, bouton_hauteur))
    bouton_surface.set_alpha(0)
    bouton_surface.fill(BLANC)

    # Dessine le bouton
    fenetre.blit(bouton_surface, (pos_x, pos_y))


    # Charge et affiche l'image
    image_surface = pygame.image.load(image)
    image_surface = pygame.transform.scale(image_surface,(bouton_largeur, bouton_hauteur))  # Ajuste la taille de l'image
    fenetre.blit(image_surface, (pos_x + 10, pos_y + 10))

    # Dessine le texte au centre du bouton
    texte_x = pos_x + 10 + (bouton_largeur - texte_surface.get_width()) / 2
    texte_y = pos_y + 10 + (bouton_hauteur - texte_surface.get_height()) / 2
    fenetre.blit(texte_surface, (texte_x, texte_y))

    bouton_rect = bouton_surface.get_rect()
    bouton_rect.topleft = (pos_x, pos_y)

    return bouton_rect

def animation(sens):
    if sens == "haut":
        fenetre.blit(personnage_dos, personnage_dos.get_rect(center=(pos_personnage)))
    elif sens == "bas":
        fenetre.blit(personnage_face, personnage_face.get_rect(center=(pos_personnage)))


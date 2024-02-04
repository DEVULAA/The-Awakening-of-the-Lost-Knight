import pygame
FPS = 60
# couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

zoom_carte = 2

#assets
bouton_background = "assets/images/bouton_background.png"

# Chargement du personnage
personnage = pygame.image.load("assets/images/personnage.png")  # Assurez-vous de remplacer par le chemin de votre propre personnage
carte = pygame.image.load("assets/images/map.png")  # Assurez-vous de remplacer par le chemin de votre propre carte

#fenetre
LARGEUR = 800
HAUTEUR = 600

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

game_state = ""

verif_echap = 0

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



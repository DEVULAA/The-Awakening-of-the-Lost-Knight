# Importer le module pygame
import pygame
from constantes import *

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((800, 600))

# Définir le titre et l'icône du jeu
pygame.display.set_caption("The Awakening of the Lost Knight")



# Créer boutons
def creer_bouton(image, texte, taille_texte, bouton_largeur, bouton_hauteur, pos_x, pos_y):

    font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", taille_texte)

    texte_surface = font.render(texte, True, NOIR)

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





# Définir l'état du jeu
game_state = "menu"

# Créer une boucle principale
running = True
while running:

    # Remplir l'écran avec une couleur de fond
    fenetre.fill(BLANC)


    # Si l'état du jeu est le menu de départ, afficher les boutons
    if game_state == "menu":

        # Afficher les trois boutons
        bouton_jouer = creer_bouton(bouton_background, '       JOUER       ', 20, 220, 50, 290, 233)
        bouton_parametres = creer_bouton(bouton_background, 'PARAMÈTRES', 20, 220, 50,290, 313)
        bouton_quitter = creer_bouton(bouton_background, 'QUITTER', 20, 220, 50, 290, 393)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre, quitter le jeu
        if event.type == pygame.QUIT:
            running = False
        # Si l'utilisateur clique avec la souris, vérifier les boutons
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Si le bouton jouer est cliqué, changer l'état du jeu
            if bouton_jouer.collidepoint(mouse_x, mouse_y):
                game_state = "jouer"
            # Si le bouton paramètres est cliqué, changer l'état du jeu
            if bouton_parametres.collidepoint(mouse_x, mouse_y):
                game_state = "parametres"
            # Si le bouton quitter est cliqué, quitter le jeu
            if bouton_quitter.collidepoint(mouse_x, mouse_y):
                running = False








    # Si l'état du jeu est jouer, exécuter le code du fichier jouer.py
    if game_state == "jouer":
        # Importer le fichier jouer.py
        import jouer
        # Exécuter la fonction principale du fichier jouer.py
        jouer.main()

    # Si l'état du jeu est paramètres, exécuter le code du fichier parametres.py
    if game_state == "parametres":
        # Importer le fichier parametres.py
        import parametres
        # Exécuter la fonction principale du fichier parametres.py
        parametres.main()

    # Mettre à jour l'affichage
    pygame.display.flip()

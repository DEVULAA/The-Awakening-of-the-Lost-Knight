# Importer le module pygame
import pygame

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
screen = pygame.display.set_mode((800, 600))

# Définir le titre et l'icône du jeu
pygame.display.set_caption("Mon jeu")
font = pygame.font.Font("polices/DePixelHalbfett.ttf", 26)

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Définir les boutons
play_button = pygame.Rect(300, 200, 200, 50)
settings_button = pygame.Rect(300, 300, 200, 50)
quit_button = pygame.Rect(300, 400, 200, 50)

# Définir les textes des boutons
play_text = font.render("Jouer", True, WHITE)
settings_text = font.render("Paramètres", True, WHITE)
quit_text = font.render("Quitter", True, WHITE)

# Définir l'état du jeu
game_state = "start_menu"

# Créer une boucle principale
running = True
while running:
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
            if play_button.collidepoint(mouse_x, mouse_y):
                game_state = "play"
            # Si le bouton paramètres est cliqué, changer l'état du jeu
            if settings_button.collidepoint(mouse_x, mouse_y):
                game_state = "settings"
            # Si le bouton quitter est cliqué, quitter le jeu
            if quit_button.collidepoint(mouse_x, mouse_y):
                running = False

    # Remplir l'écran avec une couleur de fond
    screen.fill(BLACK)

    # Si l'état du jeu est le menu de départ, afficher les boutons
    if game_state == "start_menu":
        # Dessiner les boutons
        pygame.draw.rect(screen, RED, play_button)
        pygame.draw.rect(screen, GREEN, settings_button)
        pygame.draw.rect(screen, BLUE, quit_button)
        # Dessiner les textes des boutons
        screen.blit(play_text, (play_button.x + 50, play_button.y + 10))
        screen.blit(settings_text, (settings_button.x + 25, settings_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 50, quit_button.y + 10))

    # Si l'état du jeu est jouer, exécuter le code du fichier jouer.py
    if game_state == "play":
        # Importer le fichier jouer.py
        import jouer
        # Exécuter la fonction principale du fichier jouer.py
        jouer.main()

    # Si l'état du jeu est paramètres, exécuter le code du fichier parametres.py
    if game_state == "settings":
        # Importer le fichier parametres.py
        import parametres
        # Exécuter la fonction principale du fichier parametres.py
        parametres.main()

    # Mettre à jour l'affichage
    pygame.display.flip()

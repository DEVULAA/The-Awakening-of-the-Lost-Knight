# Importer les modules
import pygame
import constantes as c

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

# Définir le titre et l'icône du jeu
pygame.display.set_caption("The Awakening of the Lost Knight")
icone = pygame.image.load('assets/images/icone.png')
pygame.display.set_icon(icone)



# brillance du logo
animation_logo = [f"assets/images/logo_animation/logo_0{i}.png" for i in range(10)]
animation_logo.append("assets/images/logo_animation/logo_10.png")
animation_logo.append("assets/images/logo_animation/logo_11.png")
animation_logo.append("assets/images/logo_animation/logo_12.png")

index_animation = 0
compteur_animation = 0
animation_terminee = False


temps_derniere_animation = pygame.time.get_ticks()

# Charger l'image d'ombre
ombre = pygame.image.load('assets/images/logo_ombre.png')
ombre = pygame.transform.scale(ombre, (ombre.get_width() * 0.5, ombre.get_height() * 0.5))


# Définir l'état du jeu
c.game_state = "menu"

# Créer une boucle principale
while c.running:

    pygame.mixer.music.set_volume(c.volume / 100)

    if c.musique:

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unload()
            pygame.mixer.music.load("assets/sons/musique/menu_titre.wav")
            pygame.mixer.music.play(-1)

    if c.musique == False:

        pygame.mixer.music.pause()

    # Si l'état du jeu est le menu de départ, afficher les boutons principaux
    if c.game_state == "menu":

        # Remplir l'écran avec une couleur de fond (BLANC pour le moment)
        fenetre.blit(c.fond, (0, 0))

        logo = pygame.image.load(animation_logo[index_animation])
        logo = pygame.transform.scale(logo, (logo.get_width() * 0.5, logo.get_height() * 0.5))

        # Afficher l'ombre
        fenetre.blit(ombre, ombre.get_rect(
            center=(c.LARGEUR // 2 + 3, 150 + 3)))  # décalage de 3 pixels vers le bas et à droite

        fenetre.blit(logo, logo.get_rect(center=(c.LARGEUR//2, 150)))



        # Afficher les trois boutons principaux du menu
        bouton_jouer = c.creer_bouton(c.bouton_background, 'Jouer', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 273)
        bouton_parametres = c.creer_bouton(c.bouton_background, 'Paramètres', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 353)
        bouton_quitter = c.creer_bouton(c.bouton_background, 'Quitter', 18, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 433)

        if compteur_animation == 5 and not animation_terminee:
            index_animation += 1
            compteur_animation = 0

        if not animation_terminee:
            compteur_animation += 1

        if index_animation >= len(animation_logo):
            index_animation = 0

            animation_terminee = True

        if animation_terminee:

            if pygame.time.get_ticks() - temps_derniere_animation >= 4000:
                animation_terminee = False
                temps_derniere_animation = pygame.time.get_ticks()



    if c.game_state == "menu":

        # Gérer les événements (si cliqué ou autre)
        for event in pygame.event.get():

            # Si l'utilisateur ferme la fenêtre, quitter le jeu
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(500)
                c.running = False

            # Si l'utilisateur clique avec la souris, vérifier les boutons
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Obtenir la position de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Si le bouton jouer est cliqué, changer l'état du jeu
                if bouton_jouer.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.fadeout(500)
                    c.game_state = "jouer"


                # Si le bouton paramètres est cliqué, changer l'état du jeu
                if bouton_parametres.collidepoint(mouse_x, mouse_y):

                    c.game_state = "parametres"

                # Si le bouton quitter est cliqué, quitter le jeu
                if bouton_quitter.collidepoint(mouse_x, mouse_y):
                    c.running = False


    # Si l'état du jeu est "jouer", exécuter le code du fichier jouer.py
    if c.game_state == "jouer":

        # Importer le fichier jouer.py
        import jouer

        # Exécuter la fonction principale du fichier jouer.py
        jouer.principal()


    # Si l'état du jeu est paramètres, exécuter le code du fichier parametres.py
    if c.game_state == "parametres":

        # Importer le fichier parametres.py
        import parametres

        # Exécuter la fonction principale du fichier parametres.py
        parametres.principal()

    pygame.display.flip()

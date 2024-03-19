# Importer le module pygame
import pygame
import constantes as c
import lobby
import level1


# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

buffer_surface = pygame.Surface(fenetre.get_size(), pygame.SRCALPHA)

def principal():

    if c.musique:
        pygame.mixer.pause()

    lobby.touches_pressee["gauche"] = False
    lobby.touches_pressee["droite"] = False
    lobby.touches_pressee["haut"] = False
    lobby.touches_pressee["bas"] = False

    level1.touches_pressee["gauche"] = False
    level1.touches_pressee["droite"] = False

    c.pause = True
    fenetre.blit(c.image_pause, (0, 0))
    arriere_plan = pygame.Surface((c.LARGEUR, c.HAUTEUR), pygame.SRCALPHA)
    arriere_plan = arriere_plan.convert_alpha()
    arriere_plan.fill((128, 128, 128, 128))


    fenetre.blit(arriere_plan, (0, 0))

    while c.pause:

        font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
        texte_gros = font.render("Pause", True, c.NOIR)
        texte_rect = texte_gros.get_rect(center=(c.LARGEUR / 2, c.HAUTEUR - (c.HAUTEUR - 40)))

        fenetre.blit(texte_gros, texte_rect)

        if c.musique:
            bouton_mute = pygame.image.load("assets/images/mute.png").convert_alpha()

        else:
            bouton_mute = pygame.image.load("assets/images/unmute.png").convert_alpha()

        bouton_mute = pygame.transform.scale(bouton_mute, (bouton_mute.get_width() * 3, bouton_mute.get_height() * 3))
        rect_bouton_mute = bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))

        fenetre.blit(bouton_mute, rect_bouton_mute)


        bouton_continuer = c.creer_bouton(c.bouton_background, 'Continuer', 20, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 400)
        bouton_quitter = c.creer_bouton(c.bouton_background, 'Quitter', 20, c.BLANC, 250, 50, (c.LARGEUR//2)-250//2, 500)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(500)
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtenir la position de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Si le bouton jouer est cliqué, changer l'état du jeu
                if bouton_continuer.collidepoint(mouse_x, mouse_y):
                    c.pause = False

                if rect_bouton_mute.collidepoint(mouse_x, mouse_y):

                    c.musique = not c.musique

                if bouton_quitter.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.fadeout(500)
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.unpause()
                    c.pause = False








        pygame.display.update()
        pygame.time.Clock().tick(5)




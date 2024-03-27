# Importer le module pygame
import pygame
import constantes as c
import lobby
import level1


# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

def principal():

    if c.musique:
        pygame.mixer.music.pause()

    lobby.touches_pressee = {"gauche": False, "droite": False, "haut": False, "bas": False}
    level1.touches_pressee = {"gauche": False, "droite": False}

    c.pause = True
    fenetre.blit(c.image_pause, (0, 0))
    arriere_plan = pygame.Surface((c.LARGEUR, c.HAUTEUR), pygame.SRCALPHA)

    arriere_plan.fill((128, 128, 128, 128))
    fenetre.blit(arriere_plan, (0, 0))

    while c.pause:
        font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
        texte_gros = font.render("Pause", True, c.NOIR)
        texte_rect = texte_gros.get_rect(center=(c.LARGEUR / 2, c.HAUTEUR - (c.HAUTEUR - 40)))
        fenetre.blit(texte_gros, texte_rect)

        bouton_mute_image = "assets/images/unmute.png" if c.musique else "assets/images/mute.png"
        bouton_mute = pygame.image.load(bouton_mute_image)
        bouton_mute = pygame.transform.scale(bouton_mute.convert_alpha(), (bouton_mute.get_width() * 3, bouton_mute.get_height() * 3))
        rect_bouton_mute = bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))
        fenetre.blit(bouton_mute, rect_bouton_mute)

        bouton_continuer = c.creer_bouton(c.bouton_background, 'Continuer', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - 250//2, 400)
        bouton_quitter = c.creer_bouton(c.bouton_background, 'Quitter', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - 250//2, 500)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(500)
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if bouton_continuer.collidepoint(mouse_x, mouse_y):

                    if c.musique:
                        pygame.mixer.music.unpause()
                    c.pause = False

                if rect_bouton_mute.collidepoint(mouse_x, mouse_y):
                    c.musique = not c.musique

                if bouton_quitter.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.fadeout(500)
                    pygame.quit()

            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                if c.musique:
                    pygame.mixer.music.unpause()
                c.pause = False

        pygame.display.update()
        pygame.time.Clock().tick(5)




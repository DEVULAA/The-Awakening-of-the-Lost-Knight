import pygame
import time
import constantes as c

# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

def principal():

    fenetre.fill(c.BLANC)
    font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
    texte_gros = font.render("Paramètres", True, c.NOIR)
    texte_rect = texte_gros.get_rect(center=(c.LARGEUR // 2, c.HAUTEUR - (c.HAUTEUR - 40)))
    fenetre.blit(texte_gros, texte_rect)

    bouton_retour = c.creer_bouton(c.bouton_background, 'Retour', 20, c.BLANC, 250, 50, (c.LARGEUR//2) - (250//2), 500)

    bouton_musique = c.creer_bouton(c.bouton_background, 'Musique +10', 20, c.BLANC, 250, 50, (c.LARGEUR // 2) - (250 // 2), 250)

    bouton_mute_image = "assets/images/unmute.png" if c.musique else "assets/images/mute.png"
    bouton_mute = pygame.image.load(bouton_mute_image)
    bouton_mute = pygame.transform.scale(bouton_mute.convert_alpha(),
                                         (bouton_mute.get_width() * 3, bouton_mute.get_height() * 3))
    rect_bouton_mute = bouton_mute.get_rect(topright=(c.LARGEUR - 8, 8))
    fenetre.blit(bouton_mute, rect_bouton_mute)


    for event in pygame.event.get():
        print(c.volume)
        if event.type == pygame.QUIT:
            c.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenir la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if rect_bouton_mute.collidepoint(mouse_x, mouse_y):
                if not c.musique:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

                c.musique = not c.musique

            # Si le bouton jouer est cliqué, changer l'état du jeu
            if bouton_retour.collidepoint(mouse_x, mouse_y):
                c.game_state = "menu"



            if bouton_musique.collidepoint(mouse_x, mouse_y):

                if c.volume < 100:
                    c.volume += 10




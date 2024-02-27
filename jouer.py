import pygame
import constantes as c
import lobby
# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu
fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))


def principal():

    fenetre.fill(c.BLANC)

    pygame.mixer.music.unload()
    pygame.mixer.music.load("assets/sons/musique/lobby_intro.wav")
    pygame.mixer.music.play()

    pygame.mixer.music.set_volume(c.volume / 100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.mixer.music.fadeout(500)
            c.running = False



        lobby.principal()


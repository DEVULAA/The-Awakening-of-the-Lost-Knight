# Importer le module pygame
import pygame
import constantes as c




# Initialiser pygame
pygame.init()

# Créer la fenêtre du jeu

fenetre = pygame.display.set_mode((c.LARGEUR, c.HAUTEUR))

buffer_surface = pygame.Surface(fenetre.get_size(), pygame.SRCALPHA)

def principal():

    c.pause = True

    arriere_plan = pygame.Surface((c.LARGEUR, c.HAUTEUR))
    arriere_plan.set_alpha(128)
    arriere_plan.fill((128, 128, 128))

    fenetre.blit(arriere_plan, (0, 0))

    while c.pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtenir la position de la souris
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Si le bouton jouer est cliqué, changer l'état du jeu
                if bouton_continuer.collidepoint(mouse_x, mouse_y):
                    c.pause = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    c.pause = False




        font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 25)
        texte_gros = font.render("Pause", True, c.NOIR)
        texte_rect = texte_gros.get_rect(center=(c.LARGEUR / 2, c.HAUTEUR - (c.HAUTEUR - 40)))

        fenetre.blit(texte_gros, texte_rect)

        bouton_continuer = c.creer_bouton(c.bouton_background, 'Continuer', 20, c.BLANC, 250, 50, 275, 400)
        bouton_menu = c.creer_bouton(c.bouton_background, 'Menu', 20, c.BLANC, 250, 50, 275, 500)



        pygame.display.update()
        pygame.time.Clock().tick(5)




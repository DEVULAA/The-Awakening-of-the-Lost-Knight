import pygame
import constantes as c
from MenuPause import MenuPause
import time
pygame.init()

#full truc technique lonnnnnnnnng à expliquer
class Game:
    def __init__(self,width,height):
        self.fenetre = pygame.display.set_mode((width, height))
        self.frame = None
        self.old_frame = None
        self.last_escape = None
        self.last_fps = time.time()
        pygame.display.set_caption("The Awakening of the Lost Knight")
        icone = pygame.image.load('assets/images/icone.png').convert_alpha()
        pygame.display.set_icon(icone)
        pygame.mixer.music.set_volume(c.volume / 100)

        self.font = pygame.font.Font("assets/polices/DePixelHalbfett.ttf", 10)


        self.menu_pause = MenuPause()
        


    def setFrame(self,object):
        self.frame = object
        self.frame.setFenetre(self.fenetre)

    def getFrame(self):
        return self.frame

    def update(self):
        if self.frame != None:
            if self.frame != self.old_frame:
                if not c.pause:
                    self.old_frame = self.frame
                    self.frame.firstAction()

            if c.unpause_game:
                c.unpause_game = False
                if c.musique:
                    pygame.mixer.music.unpause()
                c.pause = False
                self.setFrame(self.old_frame)
                self.frame.unpause()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if c.musique:
                        pygame.mixer.music.fadeout(500)
                    c.running = False
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        if self.frame.pausable and not c.pause:
                            self.menu_pause.setImagePause(self.frame.pause())
                            self.setFrame(self.menu_pause)
                            c.pause = True
                            c.game_state = "menu_pause"
                            self.last_escape = pygame.time.get_ticks()
                        elif c.pause and pygame.time.get_ticks() - self.last_escape >= 500:
                            if c.musique:
                                pygame.mixer.music.unpause()
                            c.pause = False
                            self.setFrame(self.old_frame)
                            self.frame.unpause()
                self.frame.verifyEvents(event)

            
            if c.running:
                self.frame.showUpdate()
                fps = 1 / (time.time() - self.last_fps)
                self.last_fps = time.time()
                self.fps_text = self.font.render(str(round(fps)), True, c.BLANC)
                self.fps_text_rect = self.fps_text.get_rect(center=(20, 20))
                self.fenetre.blit(self.fps_text,self.fps_text_rect)

                pygame.time.Clock().tick(60)
                pygame.display.flip()





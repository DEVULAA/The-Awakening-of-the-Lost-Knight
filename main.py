# Importer les modules
import constantes as c
from Game import Game
import os
for file in os.scandir('Frames'):
    if file.is_file():
        imp = f'from Frames.{file.name[:-3]} import {file.name[:-3]}'
        exec (imp)

game = Game(c.LARGEUR,c.HAUTEUR)

menu = Menu()
c.game_frames.append(menu)
lobby = Lobby()
c.game_frames.append(lobby)
setting = Setting()
c.game_frames.append(setting)
level_pink = LevelPink()
c.game_frames.append(level_pink)
shop = Magasin()
c.game_frames.append(shop)
test = Test()
c.game_frames.append(test)

# Définir l'état du jeu
c.game_state = "menu"

# Créer une boucle principale
while c.running:

    for frame in c.game_frames:
        try:
            if frame == eval(c.game_state):
                game.setFrame(frame)
        except:
            pass

    game.update()

    
    



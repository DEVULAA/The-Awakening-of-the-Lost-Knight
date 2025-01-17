import pygame
class HitBox:
    def __init__(self,target):
        self.target = target
        self.objects = []


    def getHitboxRect(self,map):
        hitboxs_rect = [0 for i in range(len(self.objects))]
        for i in range(len(self.objects)):
            if self.objects[i][2] == "pos":
                x = map[0] + self.objects[i][0][0]
                y = map[1] + self.objects[i][0][1]
                w = (map[0] + self.objects[i][1][0]) - (map[0] + self.objects[i][0][0])
                h = (map[1] + self.objects[i][1][1]) - (map[1] + self.objects[i][0][1])
                hitboxs_rect[i] = pygame.Rect(x,y,w,h)
            elif self.objects[i][2] == "center":
                hitboxs_rect[i] = self.objects[i][3].get_rect(center=(map[0] + self.objects[i][0],map[1] + self.objects[i][1]))
        return hitboxs_rect

    
    def addHitboxByPos(self,posx,posy):
        self.objects.append((posx,posy,"pos"))
    def addHitboxByCenter(self,posx,posy,obj):
        self.objects.append((posx,posy,"center",obj))

    def getCollisions(self,map):
        collisions = {}
        hitboxs_rect = self.getHitboxRect(map)
        for hitbox in hitboxs_rect:
            if self.target.colliderect(hitbox):
                cote = self.determinerCote(hitbox)
                if "bas" in cote:
                    dist = abs(self.target.bottom - hitbox.top)
                    collisions["bas"] = dist
                if "haut" in cote:
                    dist = abs(self.target.top - hitbox.bottom)
                    collisions["haut"] = dist
                if "gauche" in cote:
                    dist = abs(self.target.left - hitbox.right)
                    collisions["gauche"] = dist
                if "droite" in cote:
                    dist = abs(self.target.right - hitbox.left)
                    collisions["droite"] = dist
                
                
        return collisions
    
    
    def determinerCote(self, obj):
        cotes = []
        if self.target.midbottom[1] <= obj.midtop[1] + 7:
            cotes.append("bas")

        elif self.target.midtop[1] >= obj.midbottom[1] - 7:
            cotes.append("haut")

        if self.target.midleft[0] > obj.midleft[0]:
            cotes.append("gauche")
        elif self.target.midright[0] < obj.midright[0]:
            cotes.append("droite")
        return cotes
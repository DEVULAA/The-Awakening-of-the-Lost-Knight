"""
import pygame
import level1 as l
import constantes as c

def principal():

    if l.victoire == "joueur":
        c.score += 100
    elif l.victoire == "boss" and c.score >= 20:
        c.score -= 20
"""


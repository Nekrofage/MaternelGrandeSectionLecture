# -*- coding: utf-8 -*-
import pygame
import random
import sys
import os
import webbrowser
import time
import sqlite3 as lite
import subprocess

sys.path.append('./package')

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


class FruitClass:
    name = ""
    x = 0
    y = 0

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    
    def setImage(self, name):   
        self.image = pygame.image.load(name).convert_alpha()
        self.image.set_colorkey(white)
        self.image_width  = self.image.get_width()
        self.image_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.image_width/2, self.image_height/2))

    def getImage(self):
        return self.image

    def getName(self):
        return self.name
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y


def fruitImage(imageFile):
    fruit_image = pygame.image.load(imageFile).convert_alpha()
    fruit_image.set_colorkey(white)
    fruit_image_width = fruit_image.get_width()
    fruit_image_height = fruit_image.get_height()
    fruit_image = pygame.transform.scale(fruit_image, (fruit_image_width/2, fruit_image_height/2))

    return fruit_image


def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()

    screen_width = 1024
    screen_height = 768
    screen=pygame.display.set_mode([screen_width,screen_height])

    font = pygame.font.Font(None, 25)

    pygame.display.set_caption("Ecouter les mots")

    done = False

    clock=pygame.time.Clock()

    file = open("fruit/fruit.list", "r")
    line_list = file.readlines()
    file.close()

    fruit_list = []

    for line in line_list:
        line = line[:-1]
        fruit = FruitClass(line, random.randint(1, 10) * 100, random.randint(1, 70)*10)
        fruit.setImage("fruit/" + line + ".png")
        fruit_list.append(fruit)


    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    numberFruit = random.randint(1, len(fruit_list)) - 1
                    fruit = pygame.mixer.Sound(os.path.join('fruit', fruit_list[numberFruit].getName() + '.wav'))
                    fruit.play()                   
                    for fruit in fruit_list:
                        fruit.setX(random.randint(1, 10) * 100)
                        fruit.setY(random.randint(1, 70) * 10)




        screen.fill(white)

        gameText = font.render("Ecouter les mots", True, ( 255, 0, 0))
        screen.blit(gameText, [10, 10])
        
        infoText = font.render(u"Appuyer sur la touche [Espace] pour écouter un nouveau mot", True, ( 255, 0, 0))
        screen.blit(infoText, [10, 30])
 
        for fruit in fruit_list:
            screen.blit(fruit.getImage(), [fruit.getX() ,fruit.getY()])

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

if __name__ == "__main__":
    main()

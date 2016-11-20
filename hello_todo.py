'''
Created on May 24, 2012
@author: Brian Borowski
Simple pygame to illustrate the basics in true OO style.
'''

import pygame
import sys
import os
import gradients

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
YELLOW = (255, 255, 0)
PURPLE = (38, 47, 145, 255)
BLACK = (0, 0, 0, 255)

class Message(object):
    def __init__(self, message):
        self.__font = pygame.font.Font(None, 60)
        (self.__text_width, self.__text_height) = self.__font.size(message)
        self.x = (SCREEN_WIDTH - self.__text_width) // 2
        self.y = (SCREEN_HEIGHT - self.__text_height) // 2
        self.image = self.__font.render(message, True, YELLOW)

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.__text_width:
            self.x +=1

    def move_up(self):
        if self.y > 0:
            self.y -=1

    def move_down(self):
        if self.y < SCREEN_HEIGHT - self.__text_height:
            self.y +=1

class Game(object):
    TEXT = "Hello, pygame!"

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(Game.TEXT)
        self.message = Message(Game.TEXT)
        self.background = \
            gradients.vertical((SCREEN_WIDTH, SCREEN_HEIGHT), PURPLE, BLACK)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.message.move_left()
        if pressed[pygame.K_RIGHT]:
            self.message.move_right()
        if pressed[pygame.K_UP]:
            self.message.move_up()
        if pressed[pygame.K_DOWN]:
            self.message.move_down()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(
            self.message.image, (self.message.x, self.message.y))
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.update()
            self.render()

if __name__ == '__main__':
    game = Game()
    game.run()

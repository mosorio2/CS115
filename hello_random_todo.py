'''
Created on May 24, 2012
@author: Brian Borowski
Simple pygame to illustrate the basics in true OO style.
'''
import pygame
import sys
import os
import random
import gradients

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
YELLOW = (255, 255, 0)
PURPLE = (38, 47, 145, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255)

class Message(object):
    PAUSED = 0
    MOVING = 1
    HIT = 2

    def __init__(self, message):
        self.__message = message
        self.__font = pygame.font.Font(None, 60)
        (self.__text_width, self.__text_height) = self.__font.size(message)
        self.__x = (SCREEN_WIDTH - self.__text_width) // 2
        self.__y = (SCREEN_HEIGHT - self.__text_height) // 2
        self.__image = self.__font.render(message, True, YELLOW).convert_alpha()
        self.__status = Message.PAUSED
        self.__delta_x = 0
        self.__delta_y = 0
        self.__speed = 100
        self.__num_times_hit = 0

    @property
    def image(self):
        return self.__image

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def num_times_hit(self):
        return self.__num_times_hit

    def move_left(self, seconds):
        distance = self.__speed * seconds
        if self.__x >= distance:
            self.__x -= distance
        else:
            self.__x = 0
            self.__status = Message.HIT
            self.__num_times_hit +=1

    def move_right(self, seconds):
        distance = self.__speed * seconds
        rightmost = (SCREEN_WIDTH - self.__text_width)
        if self.__x < rightmost - distance:
            self.__x += distance
        else:
            self.__x = rightmost
            self.__status = Message.HIT
            self.__num_times_hit +=1

    def move_up(self, seconds):
        distance = self.__speed * seconds
        if self.__y >= distance:
            self.__y -= distance
        else:
            self.__y = 0
            self.__status = Message.HIT
            self.__num_times_hit +=1

    def move_down(self, seconds):
        # TODO
        pass

    def move_composite(self, seconds):
        if self.__status==Message.PAUSED or self.__status==Message.HIT:
            sign_x=random.randrange(-1, 2, 2)
            sign_y=random.randrange(-1, 2, 2)
            self.delta_x= random.randint(1, 3) * sign_x
            self.delta_y= random.randint(1, 3) * sign_y
            self.set_moving()
        if self.delta_x >= 1:
            for _ in range(self.delta_x):
                self.move_right(seconds)
        else:
            for _ in range(-self.delta_x):
                self.move_left(seconds)
        if self.delta_y >= 1:
            for _ in range(self.delta_y):
                self.move_down(seconds)
        else:
            for _ in range(-self.delta_y):
                self.move_up(seconds)
                

    def set_moving(self):
        self.__status = Message.MOVING

    def set_paused(self):
        self.__status = Message.PAUSED

class Game(object):
    TEXT = "Hello, pygame!"

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(Game.TEXT)
        self.game_font = pygame.font.Font(None, 20)
        self.clock = pygame.time.Clock()
        self.message = Message(Game.TEXT)
        self.background = \
            gradients.radial((SCREEN_WIDTH, SCREEN_HEIGHT), PURPLE, BLACK)
        self.paused = False
        self.fps = 0
        self.last_update = 0

    def update(self, seconds):
        pressed = pygame.key.get_pressed()

        # Check if game should be paused first.
        if pressed[pygame.K_p]:
            self.paused = True
        elif pressed[pygame.K_r]:
            self.paused = False
        if self.paused:
            return

        user_control = False
        if pressed[pygame.K_LEFT]:
            user_control = True
            self.message.move_left(seconds)
        if pressed[pygame.K_RIGHT]:
            user_control = True
            self.message.move_right(seconds)
        if pressed[pygame.K_UP]:
            user_control = True
            self.message.move_up(seconds)
        if pressed[pygame.K_DOWN]:
            user_control = True
            self.message.move_down(seconds)
        if not user_control:
            self.message.move_composite(seconds)

        self.last_update += seconds
        if self.last_update >= 1 or self.fps == 0:
            self.fps = self.clock.get_fps()
            fps_text = "FPS: {0:0.1f}".format(self.fps)
            self.fps_image = \
                self.game_font.render(fps_text, True, WHITE).convert_alpha()
            self.last_update = 0

        hit_text = "Hits: {0:1d}".format(self.message.num_times_hit)
        self.hit_image = \
                       self.game_font.render(hit_text, True, WHITE).convert_alpha()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(
            self.message.image, (self.message.x, self.message.y))
        self.screen.blit(self.fps_image, (10, SCREEN_HEIGHT - 20))
        self.screen.blit(self.hit_image, (10, 10))
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            time_ms = self.clock.tick()
            if time_ms < 100:
                self.update(time_ms / 1000.0)
                self.render()

if __name__ == '__main__':
    game = Game()
    game.run()

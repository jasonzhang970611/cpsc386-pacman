from typing import Type

import pygame as pg
from pygame.math import Vector2
from pacman import *
from setting import *
from pygame.sprite import Group
from pygame.sprite import Sprite
from pygame.sysfont import SysFont
from pygame import mixer
import SheetSprites

vec: Type[Vector2] = pg.math.Vector2


class Player:

    def __init__(self, screen, pos):
        self.screen = screen
        self.grid_pos = pos
        self.pix_pos = self.get_pix()
        self.direction = vec(1, 0)
        self.on_direction = None
        self.way_to_move = True
        self.telepolt = False
        self.current_score = 0
        self.player_life = 3
        self.life()
        self.pac_man = SheetSprites.sheetSprites('images/Pacman.png')


        #self.pac = [self.pac_man.image_at(0, 45)]
        # what if we use this way

    # w = pygame.sprite.Sprite()
    # w.image = pygame.image.load("Pacman.png").convert()
    # w.rect = w.image.get_rect()
    # screen.blit(w.image, w.rect)
    # self.sprites = {'right': [pg.makeSprite('Pacman.png', 12)]}

    def update(self):
        if self.way_to_move:
            self.pix_pos += self.direction
        # Pac man only can move in box
        if self.move_direction():
            if self.on_direction is not None:
                self.direction = self.on_direction
            self.way_to_move = self.can_move()

        self.grid_pos = ((self.pix_pos[0] // self.screen.cell_width),
                         (self.pix_pos[1] // self.screen.cell_height) - 3)

        if self.on_coin():
            self.eat()
        # add ai of the enemy when pac man eat power coin
        if self.on_super():
            self.supers()
        if self.tele():
            self.swich_pos()

    def draw(self):
        pg.draw.circle(self.screen.screen, YELLOW, (int(self.pix_pos.x), int(self.pix_pos.y)),
                       self.screen.cell_width // 2 + 4)
        # pg.draw.rect(self.screen.screen, RED,
        # (self.grid_pos[0]*self.screen.cell_width,
        # self.grid_pos[1]*self.screen.cell_height,
        # self.screen.cell_width, self.screen.cell_height), 1)

    def on_super(self):
        if self.grid_pos in self.screen.super:
            return True
        return False

    def supers(self):
        pg.mixer.Sound.play(self.screen.eat_sound2)
        self.screen.super.remove(self.grid_pos)
        self.current_score += 20

    def on_coin(self):

        if self.grid_pos in self.screen.coins:

            if int(self.pix_pos.x + 8) // 2 % (self.screen.cell_width - 8) == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + 8) // 2 % (self.screen.cell_height - 8) == 0:
                if self.direction == vec(0, -1) or self.direction == vec(0, 1):
                    return True
        return False

    def eat(self):
        pg.mixer.Sound.stop(self.screen.eat_sound)
        pg.mixer.Sound.play(self.screen.eat_sound)
        self.screen.coins.remove(self.grid_pos)

        self.current_score += 10

    def move(self, direction):
        self.on_direction = direction

    def get_pix(self):
        return vec((self.grid_pos.x * self.screen.cell_width + 8), (self.grid_pos.y * self.screen.cell_height + 8))
        print(self.grid_pos, self.pix_pos)

    def move_direction(self):
        if int(self.pix_pos.x + 8) // 2 % (self.screen.cell_width - 8) == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if int(self.pix_pos.y + 8) // 2 % (self.screen.cell_height - 8) == 0:
            if self.direction == vec(0, -1) or self.direction == vec(0, 1):
                return True

    def can_move(self):
        if self.is_gate():
            for wall in self.screen.wall:
                if vec(self.grid_pos + self.direction) == wall:
                    return False
            return True

    def is_gate(self):
        for gate in self.screen.gate:
            if (self.grid_pos + self.direction) == gate:
                return False
        return True

    def tele(self):
        if self.grid_pos in self.screen.a:
            return True
        if self.grid_pos in self.screen.b:
            return True
        return False

    def swich_pos(self):
        if self.grid_pos in self.screen.a:
            self.pix_pos = Vector2(428, 280)
        if self.grid_pos in self.screen.b:
            self.pix_pos = Vector2(20, 280)

    def frontplayer(self):
        if self.way_to_move:
            self.pix_pos += (3*self.direction)
            if self.pix_pos.y == 28:
                self.pix_pos -= (3*self.direction)

    def life(self):
        if self.player_life == 3:
            #self.screen.screen.blit(self.pac, (16, 560))
            pg.draw.circle(self.screen.screen, YELLOW, (16, 156), self.screen.cell_width // 2 - 2)
            pg.draw.circle(self.screen.screen, YELLOW, (36, 560), self.screen.cell_width // 2 - 2)
            pg.draw.circle(self.screen.screen, YELLOW, (56, 560), self.screen.cell_width // 2 - 2)
        else:
            if self.player_life == 2:
                pg.draw.circle(self.screen.screen, YELLOW, (16, 560), self.screen.cell_width // 2 - 2)
                pg.draw.circle(self.screen.screen, YELLOW, (36, 560), self.screen.cell_width // 2 - 2)
            else:
                if self.player_life == 1:
                    pg.draw.circle(self.screen.screen, YELLOW, (16, 560), self.screen.cell_width // 2 - 2)

    def reset(self):
        self.grid_pos = PLAYER_START
        self.pix_pos = self.get_pix()
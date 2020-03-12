import pygame
from pygame.math import Vector2 as vec
from Ghosts import Ghosts
from pygame.sprite import Group
pygame.init()
# screen
WIDTH, HEIGHT = 448, 576
FPS = 60
Maze_width, Maze_height = 448, 496

# each 口 is width 16 and height 16
null = (16, 16)

# color
BLACK = (0, 0, 0)
GOLD = (246, 253, 49)
GREY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (20, 27, 229)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (190, 190, 15)

# text size
box_size = 16
start_font = 'arial black'

# tp

A = vec(0, 280)
# player position
PLAYER_START = vec(14.5, 26)
start_position = (WIDTH // 2, 424)
fpos = vec(0, 16)

UP = vec(0, 1)
DOWN = vec(0, -1)
RIGHT = vec(1, 0)
LEFT = vec(-1, 0)

HS_file = "scorefile.txt"


screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Ghosts


right = vec(-1, 0)
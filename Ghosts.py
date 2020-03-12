import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from pygame.sysfont import SysFont
from pygame import mixer
import SheetSprites
from random import randint


def playAfraidSound():
    mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghosts_ambient.wav'))


def playDeathSound():
    mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghost_eaten.wav'))


def playRetreatSound():
    mixer.Channel(1).play(pygame.mixer.Sound('sounds/ghosts_ambient_scared1.wav'))


class Ghosts(Sprite):
    def __init__(self, screen, color):
        super(Ghosts, self).__init__()
        self.color = color  # ghost type
        self.screen = screen
        self.height = 35
        self.width = 35
        self.reset()

        Cyan_sheet = SheetSprites.sheetSprites('images/Cyan.png')
        Yellow_sheet = SheetSprites.sheetSprites('images/Yellow.png')
        Pink_sheet = SheetSprites.sheetSprites('images/Pink.png')
        Red_sheet = SheetSprites.sheetSprites('images/Red.png')
        Scared_sheet = SheetSprites.sheetSprites('images/Ghost_power.png')
        Eyes_sheet = SheetSprites.sheetSprites('images/Ghost_die.png')

        self.left_image = []
        self.right_image = []
        self.up_image = []
        self.down_image = []
        self.Scared = [Scared_sheet.image_at((0, 0, 32, 38)),
                       Scared_sheet.image_at((0, 38, 32, 38)),
                       Scared_sheet.image_at((0, 76, 32, 38)),
                       Scared_sheet.image_at((0, 114, 32, 38))]
        self.eyes = [Eyes_sheet.image_at((0, 0, 23, 12)),
                     Eyes_sheet.image_at((0, 12, 23, 12)),
                     Eyes_sheet.image_at((0, 24, 23, 12)),
                     Eyes_sheet.image_at((0, 36, 23, 12))]

        if color == "red":
            self.left_image = [Red_sheet.image_at((0, 76, 32, 38)),
                               Red_sheet.image_at((0, 228, 32, 38))]
            self.right_image = [Red_sheet.image_at((0, 190, 32, 38)),
                                Red_sheet.image_at((0, 266, 32, 38))]
            self.up_image = [Red_sheet.image_at((0, 0, 32, 38)),
                             Red_sheet.image_at((0, 114, 32, 38))]
            self.down_image = [Red_sheet.image_at((0, 38, 32, 38)),
                               Red_sheet.image_at((0, 152, 32, 38))]
        elif color == "cyan":
            self.left_image = [Cyan_sheet.image_at((0, 76, 32, 38)),
                               Cyan_sheet.image_at((0, 228, 32, 38))]
            self.right_image = [Cyan_sheet.image_at((0, 190, 32, 38)),
                                Cyan_sheet.image_at((0, 266, 32, 38))]
            self.up_image = [Cyan_sheet.image_at((0, 0, 32, 38)),
                             Cyan_sheet.image_at((0, 114, 32, 38))]
            self.down_image = [Cyan_sheet.image_at((0, 38, 32, 38)),
                               Cyan_sheet.image_at((0, 152, 32, 38))]
        elif color == "Yellow":
            self.left_image = [Yellow_sheet.image_at((0, 76, 32, 38)),
                               Yellow_sheet.image_at((0, 228, 32, 38))]
            self.right_image = [Yellow_sheet.image_at((0, 190, 32, 38)),
                                Yellow_sheet.image_at((0, 266, 32, 38))]
            self.up_image = [Yellow_sheet.image_at((0, 0, 32, 38)),
                             Yellow_sheet.image_at((0, 114, 32, 38))]
            self.down_image = [Yellow_sheet.image_at((0, 38, 32, 38)),
                               Yellow_sheet.image_at((0, 152, 32, 38))]
        elif color == "pink":
            self.left_image = [Pink_sheet.image_at((0, 76, 32, 38)),
                               Pink_sheet.image_at((0, 228, 32, 38))]
            self.right_image = [Pink_sheet.image_at((0, 190, 32, 38)),
                                Pink_sheet.image_at((0, 266, 32, 38))]
            self.up_image = [Pink_sheet.image_at((0, 0, 32, 38)),
                             Pink_sheet.image_at((0, 114, 32, 38))]
            self.down_image = [Pink_sheet.image_at((0, 38, 32, 38)),
                               Pink_sheet.image_at((0, 152, 32, 38))]

        self.rect = pygame.transform.scale(self.up_image[0], (self.height, self.width)).get_rect()
        self.rect.x, self.rect.y = 330, 315
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = [None, None]
        self.image = self.up_image

        self.moving_up = True
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.last_move = "up/down"
        self.last_intersection = None

        self.speed = 1

        # ghosts are blue
        self.afraid = False

        # ghosts are eyes
        self.DEAD = False

        self.value = 0
        self.font = SysFont(None, 16, italic=True)
        self.score_image = self.font.render(str(self.value), True, (255, 255, 255), (0, 0, 0))

        # how long to show score
        self.frames = 0

    def update(self):
        if self.moving_left == True:
            self.rect.x -= self.speed
            self.image = self.left_image
        elif self.moving_right == True:
            self.rect.x += self.speed
            self.image = self.right_image
        elif self.moving_up == True:
            self.rect.y -= self.speed
            self.image = self.up_image
        elif self.moving_down == True:
            self.rect.y += self.speed
            self.image = self.down_image

    def blitghosts(self):
        if self.DEAD:
            if self.moving_left:
                self.screen.screen.blit(self.eyes[2], self.rect)
            elif self.moving_right:
                self.screen.screen.blit(self.eyes[3], self.rect)
            elif self.moving_up:
                self.screen.screen.blit(self.eyes[1], self.rect)
            elif self.moving_down:
                self.screen.screen.blit(self.eyes[0], self.rect)
        elif self.afraid:
            if self.frames <= 720:
                if pygame.time.get_ticks() % 200 <= 50:
                    self.screen.screen.blit(self.Scared[2], self.rect)
                elif pygame.time.get_ticks() % 200 <= 100:
                    self.screen.screen.blit(self.Scared[3], self.rect)
                elif pygame.time.get_ticks() % 200 <= 150:
                    self.screen.screen.blit(self.Scared[2], self.rect)
                else:
                    self.screen.blit(self.Scared[3], self.rect)
            elif self.frames <= 960:
                if pygame.time.get_ticks() % 200 <= 50:
                    self.screen.blit(self.Scared[0], self.rect)
                elif pygame.time.get_ticks() % 200 <= 100:
                    self.screen.blit(self.Scared[1], self.rect)
                elif pygame.time.get_ticks() % 200 <= 150:
                    self.screen.blit(self.Scared[2], self.rect)
                else:
                    self.screen.blit(self.Scared[3], self.rect)
        else:
            if pygame.time.get_ticks() % 200 <= 50:
                self.screen.blit(self.image[0], self.rect)
            elif pygame.time.get_ticks() % 200 <= 100:
                self.screen.blit(self.image[1], self.rect)
            elif pygame.time.get_ticks() % 200 <= 150:
                self.screen.blit(self.image[0], self.rect)
            else:
                self.screen.blit(self.image[1], self.rect)
        if self.frames <= 60 and self.DEAD:
            self.screen.blit(self.score_image, self.rect)
            self.frames += 1
        if self.frames <= 960 and self.afraid:
            self.frames += 1
        elif self.frames > 960 and self.afraid:
            self.afraid = False
            self.frames = 0

    def resetPosition(self):
        self.moving_up = True  # Start with the ghosts going up
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.rect.x, self.rect.y = 300, 300

        self.afraid = False
        self.DEAD = False

    def reset(self):
        pass
import pygame as pg
import sys
from setting import *
from player import *
from os import path
from button import Button
from Ghosts import *

pygame.init()
vec = pg.math.Vector2
WALL = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 2, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 2, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 7, 7, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 0, 0, 0, 0, 0, 6,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
        9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
        9, 2, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 2, 9,
        9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
        9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
        9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
        9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
        9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
        9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]


def out_text(text, screen, position, size, color, font_name):
    font = pg.font.SysFont(font_name, size)
    output = font.render(text, False, color)
    output_size = output.get_size()
    screen.blit(output, position)


class Game:
    def __init__(self):
        # load the coin images
        self.highborn = 0
        self.dir = path.dirname(__file__)
        self.coin = pg.image.load('images/Coin.png')
        self.power_coin = pg.image.load('images/Power.png')
        # load the wall images
        self.background = pg.image.load('images/background.png')

        self.logo = pg.image.load('images/logo.png')
        # set screen size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.game = 'front'
        self.wall = []
        self.gate = []
        self.coins = []
        self.super = []
        self.ghosts = []

        self.load_highscour()
        # button
        self.playstation = Button(RED, 160, HEIGHT // 2 + 120, 100, 40, 'Play')
        self.scoring = Button(RED, 160, HEIGHT // 2 + 200, 100, 40, 'Height Score')
        self.menu = Button(RED, 160, HEIGHT // 2 + 200, 100, 40, 'MENU')
        # teleplot wall
        self.a = []
        self.b = []
        self.cell_width = WIDTH // 28
        self.cell_height = HEIGHT // 36
        # load player, player setting

        self.player = Player(self, PLAYER_START)
        self.front_player = Player(self, fpos)

        # self.make_ghosts()

        self.eat_sound = pg.mixer.Sound("sounds/fruit_eat.wav")
        self.eat_sound2 = pg.mixer.Sound("sounds/power_eat.wav")
        self.start_sound = pg.mixer.Sound('sounds/game_start.wav')
        pg.mixer.music.load('sounds/background.wav')
        self.load()
        self.channel = 0
        self.playmusic()
        # Ghosts
        # self.Ghosts = Ghosts(self, color=None)

        # cyanghost = Ghosts(screen, "cyan")
        # orangeghost = Ghosts(screen, "orange")
        # pinkghost = Ghosts(screen, "pink")
        # redghost = Ghosts(screen, "red")

        # Ghosts.add(cyanghost)
        # Ghosts.add(orangeghost)
        # Ghosts.add(pinkghost)
        # Ghosts.add(redghost)

    def playmusic(self):
        if self.channel == 0:
            pg.mixer.Sound.play(self.start_sound)
        if self.channel == 1:
            pg.mixer.music.play(-1)

    def run(self):
        while self.running:

            # front page  need 1. a name of game 2. moving pacman and gouse, 3.two button of playing and best scores
            if self.game == 'front':
                self.front_events()
                self.front_update()
                self.front_draw()
            if self.game == 'game':
                self.game_events()
                self.game_update()
                self.game_draw()
            if self.game == 'score':
                self.score_events()
                self.score_update()
                self.score_draw()
            if self.game == 'over':
                self.over_events()
                self.over_update()
                self.over_draw()
                pass
            self.clock.tick(FPS)
        pg.quit()
        sys.exit()

    #    ##    ###    ####    ######   #######

    def load(self):
        # load the background of the game.
        self.background = pg.transform.scale(self.background, (448, 496))
        self.power_coin = pg.transform.scale(self.power_coin, (16, 16))
        self.logo = pg.transform.scale(self.logo, (306, 57))
        # read and load the wall
        with open("wall.txt", 'r') as file:
            for yid, line in enumerate(file):
                for xid, char in enumerate(line):
                    if char == "9":
                        self.wall.append(vec(xid, yid))
                    if char == "7":
                        self.gate.append(vec(xid, yid))
                    if char == "1":
                        self.coins.append(vec(xid, yid))
                    if char == "2":
                        self.super.append(vec(xid, yid))
                    if char == "5":
                        self.a.append(vec(xid, yid))
                    if char == "6":
                        self.b.append(vec(xid, yid))

        print(self.wall)
        print(self.coins)
        print(self.super)

    def make_ghosts(self):
        self.ghosts.append(Ghosts(self, 'red'))

    def load_highscour(self):
        with open(path.join(self.dir, HS_file), 'w') as f:
            try:
                self.highborn = int(f.read())
            except:
                self.highborn = 0

    #                drawing on gaming             #

    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pg.draw.line(self.screen, GREY, (x * self.cell_width, 0), (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT // self.cell_height):
            pg.draw.line(self.screen, GREY, (0, x * self.cell_height), (WIDTH, x * self.cell_height))
        for wall in self.wall:
            pg.draw.rect(self.background, GREEN, (wall.x * self.cell_width, wall.y * self.cell_height,
                                                  self.cell_width, self.cell_height))

    def draw_coin(self):
        for coins in self.coins:
            self.screen.blit(self.coin, ((coins.x * self.cell_width - 4), (coins.y * self.cell_height + 44),
                                         self.cell_width, self.cell_height))
        for supers in self.super:
            self.screen.blit(self.power_coin, ((supers.x * self.cell_width), (supers.y * self.cell_height + 48),
                                               self.cell_width, self.cell_height))

    # game over.
    def remove_life(self):
        self.player.player_life -= 1
        if self.player.player_life == 0:
            self.game == 'over'
        else:
            self.player.reset()
            self.ghosts.reset()

    #                                                     front page                                       #

    def front_events(self):
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.playstation.isOver(pos):
                    self.game = 'game'
                    pg.mixer.Sound.stop(self.start_sound)
                    pg.mixer.music.play(-1)
                    self.channel += 1
                if self.scoring.isOver(pos):
                    self.game = 'score'

    def front_update(self):
        self.front_player.frontplayer()

    def front_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.logo, (70, 40))
        self.playstation.draw(self.screen, (0, 0, 0))
        self.scoring.draw(self.screen, (0, 0, 0))
        self.front_player.draw()
        pg.display.update()

    #                                    In game page                                   #

    def game_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            # Key movement
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.move(right)
                if event.key == pg.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pg.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pg.K_DOWN:
                    self.player.move(vec(0, 1))

    def game_update(self):
        self.player.update()

        #self.Ghosts.update()
        #for Ghost in self.ghosts:
            #if Ghost.rect == self.player.grid_pos:
                #self.remove_life()

    def game_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 48))
        self.draw_coin()
        out_text('BEST SCORE : {}'.format(self.highborn), self.screen, [2, 0], 14, WHITE, start_font)
        out_text('CURRENT SCORE: {}'.format(self.player.current_score), self.screen, [200, 0], 14, WHITE, start_font)
        if self.player.current_score > self.highborn:
            self.highborn = self.player.current_score
        self.player.draw()
        self.player.life()
        pg.display.update()

    def score_events(self):
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.menu.isOver(pos):
                    self.game = 'front'

    def score_update(self):
        pass

    def score_draw(self):
        self.screen.fill(BLACK)
        out_text('BEST SCORE : {}'.format(self.highborn), self.screen, [100, HEIGHT / 2], 25, WHITE, start_font)
        self.menu.draw(self.screen, (0, 0, 0))
        pg.display.update()

    def over_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.game = 'game'

    def over_update(self):
        pass

    def over_draw(self):
        self.screen.fill(BLACK)
        out_text('Game Over!', self.screen, [80, 200],30, YELLOW,start_font)
        out_text('SPACE TO PLAY AGAIN', self.screen, [80, HEIGHT / 2], 20, WHITE, start_font)
        pg.display.update()


def main():
    g = Game()
    g.run()


if __name__ == '__main__':
    main()

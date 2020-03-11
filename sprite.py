import pygame as pg


class spritesheet:
    def __init__(self, file, cols, rows):
        self.sheet = pg.image.load(file)
        
        self.cos = cols
        self.rows = rows
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.height / rows
        hw, hh = self.cellCenter = (w/2, h/2)

        self.cells = list([(index % cols * w, index / cols * h) for index in range(self.totalCellCount)])

import pygame as pg

class Block(pg.sprite.Sprite):
    size = (32, 32)

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pg.Surface((32, 32))
        self.image.fill((127, 127, 127))
        self.rect = self.image.get_rect()
        self.rect.center = pos
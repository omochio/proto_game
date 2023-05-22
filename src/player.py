import pygame as pg

class Player(pg.sprite.Sprite):
    delta_dict = {
        pg.K_LEFT: (-1, 0),
        pg.K_a: (-1, 0),
        pg.K_RIGHT: (1, 0),
        pg.K_d: (1, 0),
        pg.K_UP: (0, -3),
        pg.K_SPACE: (0, -3)
    }

    delta = [0, 0]

    gravity = 5
    isGround = True

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pg.Surface((128, 128))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, key_lst: dict, screen: pg.Surface):
        for d in __class__.delta_dict:
            if key_lst[d]:
                self.rect.x += self.delta_dict[d][0] * 3
                self.rect.y += self.delta_dict[d][1] * 3

        if self.isGround:
            self.rect.y += self.gravity

        screen.blit(self.image, self.rect)

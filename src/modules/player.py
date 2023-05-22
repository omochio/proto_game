import pygame as pg

class Player(pg.sprite.Sprite):
    move_dict = {
        pg.K_LEFT: (-1, 0),
        pg.K_a: (-1, 0),
        pg.K_RIGHT: (1, 0),
        pg.K_d: (1, 0),
        pg.K_UP: (0, -1),
        pg.K_SPACE: (0, -1)
    }


    gravity = 1
    isGround = False



    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pg.Surface((64, 64))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, 
        key_lst: dict, 
        screen: pg.Surface,
        blocks: pg.sprite.Group):
        for d in __class__.move_dict:
            if key_lst[d]:
                self.rect.x += self.move_dict[d][0] * 3
                self.rect.y += self.move_dict[d][1] * 3

        collide_lst = pg.sprite.spritecollide(self, blocks, False)
        if len(collide_lst) > 0:
            for b in collide_lst:
                # if self.rect.left < b.rect.right:
                #     self.rect.left = b.rect.right
                # if self.rect.right > b.rect.left:
                #     self.rect.right = b.rect.left
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.isGround = True
        else:
            self.isGround = False
        # print(self.rect.center)
        print(self.isGround)

        if not self.isGround:
            self.rect.y += self.gravity

        screen.blit(self.image, self.rect)

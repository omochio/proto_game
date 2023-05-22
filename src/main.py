import sys
import pygame as pg
import modules.player as mdl_player
import modules.block as mdl_block

WIDTH = 1024
HEIGHT = 1024

def main():
    pg.display.set_caption("proto")
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    bg_img = pg.Surface((WIDTH, HEIGHT))
    bg_img.fill((0, 0, 0))

    player = mdl_player.Player((500, 500))
    blocks = pg.sprite.Group()
    for i in range(32):
        blocks.add(mdl_block.Block((i * mdl_block.Block.size[0], HEIGHT)))

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        
        screen.blit(bg_img, (0, 0))
        blocks.draw(screen)

        key_lst = pg.key.get_pressed()

        player.update(key_lst, screen, blocks)
        pg.display.update()

        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    
import sys
import pygame as pg
import player

WIDTH = 1024
HEIGHT = 1024

def main():
    pg.display.set_caption("proto")
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    bg_img = pg.Surface((WIDTH, HEIGHT))
    bg_img.fill((0, 0, 0))

    plr = player.Player((500, 500))

    tmr = 0
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        
        screen.blit(bg_img, (0, 0))

        key_lst = pg.key.get_pressed()

        plr.update(key_lst, screen)
        pg.display.update()

        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    
import pygame as pg
import pygame.freetype
import classes
import helper_functions as hp
import copy, random, json

pg.init()

WIDTH = 600
SCREEN = pg.display.set_mode((WIDTH, WIDTH))
font = pygame.freetype.Font(None, 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
GREEN = (0, 235, 140)
RED = (255, 80, 40)
RED2 = (255, 0, 0)



def main(tot_rows, user = "Guest"):
    grid = hp.make_grid(tot_rows)
    apple = classes.Apple(grid)
    snake = classes.Snake(20, 20)
    length = 3
    old_time = pg.time.get_ticks()

    info_div = classes.Info_bar(0, WIDTH-(WIDTH//tot_rows), WHITE, user)

    run = True

    while run:
        hp.draw_grid(grid)
        apple.draw(grid)

        new_time = pg.time.get_ticks()
        if abs(old_time - new_time) > 100:
            old_time = pg.time.get_ticks()
            snake.move(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)

        if snake.head[0] < 0 or snake.head[0] == tot_rows-1 or snake.head[1] < 0 or snake.head[1] == tot_rows:
            pg.time.wait(2000)
            hp.log_top_scores("/home/brbs615/Snake/Snake/top_scores.json", length)
            run = False
        else:
             for limb in range(1, len(snake.limbs)):
                  if snake.head == [snake.limbs[limb][0], snake.limbs[limb][1]]:
                       pg.time.wait(2000)
                       hp.log_top_scores("/home/brbs615/Snake/Snake/top_scores.json", length)
                       run = False
        
        snake.draw(grid)

        if snake.head == [apple.row, apple.col]:
            snake.limbs.append([snake.limbs[-1][0], snake.limbs[-1][1]])
            apple = classes.Apple(grid)
            length += 1
        
        font.render_to(SCREEN, (10, 10), f"Length: {length}", WHITE)
        info_div.draw(length)

        if pg.display.get_init():
            pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()



if "__main__" == __name__:
    run = True
    while run:
        try: 
            main(25)
        except pg.error: 
            run = False
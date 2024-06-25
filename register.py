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
GREY = (150, 150, 150)
LIGHT_GREY = (100, 100, 100)
GREEN = (0, 235, 140)
RED = (255, 80, 40)
RED2 = (255, 0, 0)

class Register:
    def __init__(self, x, y, color):
        self.width = WIDTH//2
        self.height = WIDTH//3
        self.color = color
        self.div = pg.Rect(x, y, self.width, self.height)
        self.page = "welcome"
        self.login_button = pg.Rect(x+3, y+self.height//3, (self.width//2)-3, self.height//3)
        self.guest_button = pg.Rect(x+(self.width//2)+3, y+self.height//3, (self.width//2)-6, self.height//3)
    
    def run(self):
        pg.draw.rect(SCREEN, self.color, self.div)
        if self.page == "welcome":
            pg.draw.rect(SCREEN, GREEN, self.login_button)
            pg.draw.rect(SCREEN, LIGHT_GREY, self.guest_button)
            




def main():
    registration = Register(WIDTH//4, WIDTH//3, GREY)
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        registration.run()

        pg.display.update()

    
    pg.quit()



if "__main__" == __name__:
    main()
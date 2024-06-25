import pygame as pg
import pygame.freetype
import classes
import helper_functions as hp
import copy, random, json

pg.init()

WIDTH = 600
SCREEN = pg.display.set_mode((WIDTH, WIDTH))
font = pygame.freetype.Font(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
LIGHT_GREY = (100, 100, 100)
GREEN = (0, 235, 140)
GREEN2 = (0, 255, 100)
RED = (255, 80, 40)
RED2 = (255, 0, 0)

class Text_field:
    def __init__(self, x, y, color, div_width, div_height):
        self.x = x
        self.color = color
        self.box = pg.Rect(x, y, (div_width//3)-6, div_height//3)
        self.value = ""
    
    def draw(self):
        pg.draw.rect(SCREEN, self.color, self.box)
        font.render_to(SCREEN, self.box, self.value, WHITE)

    def make_done(self):
        self.color = WHITE
    
    def make_active(self):
        self.color = GREEN

    def is_active(self):
        return self.color == GREEN


class Register:
    def __init__(self, x, y, color):
        self.width = WIDTH//2
        self.height = WIDTH//3
        self.color = color
        self.div = pg.Rect(x, y, self.width, self.height)
        self.page = "welcome"
        self.login_button = pg.Rect(x+(self.width//2)+3, y+self.height//3, (self.width//2)-6, self.height//3)
        self.guest_button = pg.Rect(x+3, y+self.height//3, (self.width//2)-3, self.height//3)
        self.text_field1 = Text_field(x+3,                   y+(self.height//3), BLACK, self.width, self.height)
        self.text_field2 = Text_field(x+(self.width//3)+3,   y+(self.height//3), BLACK, self.width, self.height)
        self.text_field3 = Text_field(x+2*(self.width//3)+3, y+(self.height//3), BLACK, self.width, self.height)
        self.text_fields = [self.text_field1, self.text_field2, self.text_field3]
    
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            
            pg.draw.rect(SCREEN, self.color, self.div)
            if self.page == "welcome":
                pg.draw.rect(SCREEN, GREEN2, self.login_button)
                font.render_to(SCREEN, self.login_button, "Log In")
                pg.draw.rect(SCREEN, LIGHT_GREY, self.guest_button)
                font.render_to(SCREEN, self.guest_button, "As Guest")

                mouse = pg.mouse.get_pressed()

                if mouse[0]:
                
                
                print("Done")
                print(letters)
                    

                    

                    
            
            pg.display.update()
            

def main():
    registration = Register(WIDTH//4, WIDTH//3, GREY)
    
    user = registration.run()
    print(user)
    
    pg.quit()



if "__main__" == __name__:
    main()
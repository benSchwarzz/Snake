import pygame as pg
import pygame.freetype
import copy, random, json

pg.init()

WIDTH = 600
SCREEN = pg.display.set_mode((WIDTH, WIDTH))
font = pygame.freetype.Font(None, 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 235, 140)
RED = (255, 80, 40)
RED2 = (255, 0, 0)

class Node:
	def __init__(self, x, y, row, col, tot_rows):
		self.x = x
		self.y = y
		self.width = WIDTH//tot_rows
		self.row = row
		self.col = col
		self.color = BLACK
        
	def draw(self):
		pg.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.width))
    
	def is_player(self):
		return self.color == GREEN
	def is_apple(self):
		return self.color == RED
	def is_empty(self):
		return self.color == BLACK
    
	def make_player(self):
		self.color = GREEN
	def make_apple(self):
		self.color = RED
	def reset(self):
		self.color = BLACK

class Snake:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = "up"
        self.limbs = [[self.row, self.col], [self.row+1, self.col], [self.row+2, self.col]]
        self.length = len(self.limbs)
        self.head = self.limbs[0]

    def draw(self, grid):
         for limb in self.limbs:
            grid[limb[0]][limb[1]].make_player()

    def move(self, up, down, left, right):

        keys = pg.key.get_pressed()

        if keys[up] and self.direction != "down":
            self.direction = "up"
        if keys[down] and self.direction != "up":
            self.direction = "down"
        if keys[left] and self.direction != "right":
            self.direction = "left"
        if keys[right] and self.direction != "left":
            self.direction = "right"

        prev_pos = copy.deepcopy(self.limbs)

        if self.direction == "up":
            self.limbs[0][0] -= 1
        elif self.direction == "down":
            self.limbs[0][0] += 1
        elif self.direction == "left":
            self.limbs[0][1] -= 1
        elif self.direction == "right":
            self.limbs[0][1] += 1

        for limb in range(1, len(self.limbs)):
            self.limbs[limb][0] = prev_pos[limb-1][0]
            self.limbs[limb][1] = prev_pos[limb-1][1]

class Apple:
    def __init__(self, grid):
        self.row = random.randint(0, len(grid)-2)
        self.col = random.randint(0, len(grid)-2)
        self.color = RED
    
    def draw(self, grid):
        grid[self.row][self.col].make_apple()

class Info_bar:
    def __init__(self, x, y, color, user = "Guest"):
        self.color = color
        self.x = x
        self.y = y
        self.user = user
        self.box = pg.Rect(self.x, self.y, WIDTH, WIDTH-self.y)
    
    def draw(self, length):
        pg.draw.rect(SCREEN, self.color, (self.box))
        font.render_to(SCREEN, (self.x+4, self.y+4), f"Hello {self.user}", BLACK)
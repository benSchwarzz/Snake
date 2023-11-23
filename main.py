import pygame as pg
import copy, random

pg.init()

WIDTH = 600
SCREEN = pg.display.set_mode((WIDTH, WIDTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 235, 140)
RED = (255, 80, 40)

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

    def move(self, grid, tot_rows, up, down, left, right):

        for limb in self.limbs:
            grid[limb[0]][limb[1]].make_player()
           

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
        


def make_grid(tot_rows):
    grid = []

    for row in range(tot_rows+1):
        grid.append([])
        for col in range(tot_rows+1):
            node = Node((WIDTH//tot_rows)*col, (WIDTH//tot_rows)*row, row+1, col+1, tot_rows)
            pg.draw.rect(SCREEN, WHITE, ((WIDTH//tot_rows)*col, (WIDTH//tot_rows)*col, WIDTH//tot_rows, WIDTH//tot_rows), 1)
            grid[row].append(node)
    return grid

        
def draw_grid(grid):
    for row in grid:
        for node in row:
            node.draw()
            node.reset()



def main(tot_rows):
    grid = make_grid(tot_rows)
    apple = Apple(grid)
    snake = Snake(20, 20)
    run = True

    while run:
        draw_grid(grid)
        apple.draw(grid)
        snake.move(grid, 30, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)
        if snake.head[0] < 0 or snake.head[0] == tot_rows+1 or snake.head[1] < 0 or snake.head[1] == tot_rows+1:
            run = False

        if snake.head == [apple.row, apple.col]:
            snake.limbs.append([snake.limbs[-1][0], snake.limbs[-1][1]])
            apple = Apple(grid)

        pg.time.wait(40)

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    pg.quit()

if "__main__" == __name__:
    run = True
    while run:
        main(25)
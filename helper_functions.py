import pygame as pg
import pygame.freetype
import classes
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


def make_grid(tot_rows):
    grid = []

    for row in range(tot_rows):
        grid.append([])
        for col in range(tot_rows+1):
            node = classes.Node((WIDTH//tot_rows)*col, (WIDTH//tot_rows)*row, row+1, col+1, tot_rows)
            pg.draw.rect(SCREEN, WHITE, ((WIDTH//tot_rows)*col, (WIDTH//tot_rows)*col, WIDTH//tot_rows, WIDTH//tot_rows), 1)
            grid[row].append(node)
    return grid


def draw_grid(grid):
    for row in grid:
        for node in row:
            node.draw()
            node.reset()
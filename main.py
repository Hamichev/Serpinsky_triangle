import pygame
from random import randint
import math

pygame.init()

H, W = 600, 600 #H - x, W - y
sc = pygame.display.set_mode((H, W))
pygame.display.set_caption('Serpinsky triangle')

clock = pygame.time.Clock()
FPS = 60
r_circle = 250
center_x = H // 2
center_y = W // 2
x0, y0 = center_x, center_y - r_circle
x1, y1 = center_x, center_y - r_circle
x2, y2 = center_x - math.sqrt(3) * r_circle // 2, center_y + r_circle // 2
x3, y3 = center_x + math.sqrt(3) * r_circle // 2, center_y + r_circle // 2

def create_circle(x0, y0, x, y):
    circle_height = abs(x + x0) // 2
    circle_width = abs(y + y0) // 2
    pygame.draw.circle(sc, (randint(0, 255), randint(0, 255), randint(0, 255)), (circle_height, circle_width), 1)
    return circle_height, circle_width

def get_coord_point(H, W, r_circle, value, koef):
    x = H // 2 + r_circle * math.cos(math.pi * value / 90 - math.pi / 2 + koef)
    y = W // 2 + r_circle * math.sin(math.pi * value / 90 - math.pi / 2 + koef)
    return x, y

value = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill((255, 255, 255))
    for _ in range(15000):
        dot = randint(0, 2)
        if dot == 0:
            x0, y0 = create_circle(x0, y0, x1, y1)
        elif dot == 1:
            x0, y0 = create_circle(x0, y0, x2, y2)
        else:
            x0, y0 = create_circle(x0, y0, x3, y3)
    x1, y1 = get_coord_point(H, W, r_circle, value, 0)
    x2, y2 = get_coord_point(H, W, r_circle, value, - math.pi * 5 / 6)
    x3, y3 = get_coord_point(H, W, r_circle, value, math.pi * 5 / 6)
    value += 1
    pygame.display.update()
    clock.tick(FPS)
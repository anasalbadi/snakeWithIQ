#####################################################
# import the packages we need for this project
import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

print("All libraries have been loaded")

#####################################################
# Initialize pygame

pygame.init()
font = pygame.font.SysFont('arial', 25)

#####################################################
# Create a class for directions for 4 directions

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

    def describe(self):
        return f"Direction: {self.name}, Value: {self.value}"
# print(Direction.RIGHT.describe())

#####################################################
# Create a class named Point for x and y
Point = namedtuple('Point', 'x, y')

#####################################################

WHITE = (255, 255, 255)
RED =   (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 80 # Adjust the speed of teh snake to your liking

#####################################################
def _update_ui(self):
    self.display.fill(BLACK)
    for point in self.snake:
        pygame.draw.rect(self.display, BLUE1, pygame.Rect(point.x, point.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, BLUE2, pygame.Rect(point.x + 4, point.y + 4, 12, 12))

    pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

    text = font.render("Score: " + str(self.score), True, WHITE)
    self.display.blit(text, [0, 0])
    pygame.display.flip()


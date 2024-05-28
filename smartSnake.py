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
# Define colors & block size & snake speed

WHITE = (255, 255, 255)
RED =   (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 80 # Adjust the speed of teh snake to your liking

#####################################################
# Method to update game screen: snake, food, score

def _update_ui(self):
    self.display.fill(BLACK)
    for point in self.snake:
        # draws a rectangle for each snake segment in BLUE1
        pygame.draw.rect(self.display, BLUE1, pygame.Rect(point.x, point.y, BLOCK_SIZE, BLOCK_SIZE))
        # Draws a smaller rectangle inside each segment in BLUE2 - creating a layering effect
        pygame.draw.rect(self.display, BLUE2, pygame.Rect(point.x + 4, point.y + 4, 12, 12))
    pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

    text = font.render("Score: " + str(self.score), True, WHITE)
    self.display.blit(text, [0, 0])
    pygame.display.flip()

#####################################################
# Setting up the dimensions of the screen and the state of the game

def __init__(self, w=640, h=480):
    self.w = w
    self.h = h
    self.display = pygame.display.set_mode((self.w, self.h))
    pygame.display.set_caption('Snake')
    self.clock = pygame.time.Clock()

def reset(self):
    self.direction = Direction.RIGHT
    self.head = Point(self.w / 2, self.h /2)
    self.snake = [self.head, 
                  Point(self.head.x - BLOCK_SIZE, self.head.y),
                  Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
    self.score = 0
    self.food = None
    self._place_food()
    self.frame_iteration = 0


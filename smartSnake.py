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


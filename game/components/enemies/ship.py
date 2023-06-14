import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
    
class Ship2(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 8
    SPEED_Y = 3

    def __init__(self):
        self.image = ENEMY_2  # Utiliza la nueva imagen del enemigo
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
import asteroid
from constants import *

class Shot(asteroid.Asteroid):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 
import pygame,circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        vec = self.velocity.rotate(angle)
        vec_minus = self.velocity.rotate(-angle)

        frag_1 = Asteroid(self.position.x,self.position.y, radius)
        frag_2 = Asteroid(self.position.x,self.position.y, radius)

        frag_1.velocity = vec * 1.2
        frag_2.velocity = vec_minus * 1.2
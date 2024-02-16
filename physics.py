import pygame
from constants import *

class Physics:
    def __init__(self):
        return
    


    def addGravity(objects: list, gravityForce):
            for object in objects:
                if type(object) == RigidBody:
                    object.position = list(object.position)
                    object.position[1] += gravityForce
                    object.position = tuple(object.position)
                
        




class GameObject:
    def __init__(self, width, height):
        self.position = pygame.Vector2()
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
    
    def move(self):
        return


class RigidBody(GameObject):
    def __init__(self, width, height):
        super().__init__(width, height) 

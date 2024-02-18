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
    def __init__(self, width, height, list_of_game_objects):
        self.position = pygame.Vector2()
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        list_of_game_objects.append(self)
        
    
    def move(self):
        return

    def getTopPos(self):
        topPositions = []
        for x in range(self.position[0], (self.position[0] + self.width) + 1):
            topPositions.append((x, self.position[1]))

        return topPositions
    
    def getBottomPos(self):
        bottomPos = []
        for x in range(self.position[0], (self.position[0] + self.width) + 1):
            bottomPos.append((x, self.position[1] + self.height))

        return bottomPos


class RigidBody(GameObject):
    def __init__(self, width, height, list_of_game_objects):
        super().__init__(width, height, list_of_game_objects)
    
    




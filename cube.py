from utils import *
from triangle import *

class Cube:



    def __init__(self, pos: Vec3, size) -> None:
        self.triangles = [
            #TOP
            Triangle(Vec3(-1, 1, 1) + pos, Vec3(-1, 1, -1) + pos, Vec3(1, 1, 1) + pos),
            Triangle(Vec3(1, 1, 1) + pos, Vec3(1, 1, -1) + pos, Vec3(1, 1, -1) + pos),
            
            #BOTTOM
            Triangle(Vec3(-1, -1, 1) + pos, Vec3(-1, -1, -1) + pos, Vec3(1, -1, 1) + pos),
            Triangle(Vec3(1, -1, 1) + pos, Vec3(1, -1, -1) + pos, Vec3(1, -1, -1) + pos),

            #LEFT
            Triangle(Vec3(-1, 1, 1) + pos, Vec3(-1, 1, -1) + pos, Vec3(-1, -1, 1) + pos),
            Triangle(Vec3(-1, 1, -1) + pos, Vec3(-1, -1, -1) + pos, Vec3(-1, -1, 1) + pos),

            #RIGHT
            Triangle(Vec3(1, 1, 1) + pos, Vec3(1, 1, -1) + pos, Vec3(1, -1, 1) + pos),
            Triangle(Vec3(1, 1, -1) + pos, Vec3(1, -1, -1) + pos, Vec3(1, -1, 1) + pos),

            #FRONT
            Triangle(Vec3(1, 1, 1) + pos, Vec3(1, -1, 1) + pos, Vec3(-1, 1, 1) + pos),
            Triangle(Vec3(1, -1, 1) + pos, Vec3(-1, -1, 1) + pos, Vec3(-1, 1, 1) + pos),

            #BACK
            Triangle(Vec3(1, 1, -1) + pos, Vec3(1, -1, -1) + pos, Vec3(-1, 1, -1) + pos),
            Triangle(Vec3(1, -1, -1) + pos, Vec3(-1, -1, -1) + pos, Vec3(-1, 1, -1) + pos),
        ]
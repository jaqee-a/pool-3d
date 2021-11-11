from utils import *
from triangle import *

class Cube:



    def __init__(self, pos: Vec3, size) -> None:
        print(Engine.calc_normal(Vec3(1, -1, 1) , Vec3(1, 1, 1) , Vec3(-1, 1, 1)))


        self.triangles = [
            #TOP
            Triangle(Vec3(-1, 1, -1), Vec3(1, 1, -1), Vec3(-1, 1, 1)),
            Triangle(Vec3(1, 1, -1), Vec3(1, 1, 1) , Vec3(-1, 1, 1)),

            #BOTTOM
            Triangle(Vec3(-1, -1, -1), Vec3(-1, -1, 1), Vec3(1, -1, -1)),
            Triangle(Vec3(-1, -1, 1), Vec3(1, -1, 1), Vec3(1, -1, -1)),

            #LEFT
            Triangle(Vec3(-1, -1, -1), Vec3(-1, -1, 1), Vec3(-1, 1, -1)),
            Triangle(Vec3(-1, -1, 1), Vec3(-1, 1, 1), Vec3(-1, 1, -1)),

            #RIGHT
            Triangle(Vec3(1, -1, -1), Vec3(1, 1, -1), Vec3(1, -1, 1)),
            Triangle(Vec3(1, 1, -1), Vec3(1, 1, 1), Vec3(1, -1, 1)),

            #FRONT
            Triangle(Vec3(-1, -1, 1), Vec3(1, -1, 1), Vec3(-1, 1, 1)),
            Triangle(Vec3(1, -1, 1), Vec3(1, 1, 1), Vec3(-1, 1, 1)),

            #BACK
            Triangle(Vec3(-1, -1, -1), Vec3(-1, 1, -1), Vec3(1, -1, -1)),
            Triangle(Vec3(-1, 1, -1), Vec3(1, 1, -1), Vec3(1, -1, -1)),
        ]
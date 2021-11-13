import numpy as np
from utils import *
from triangle import *

class Cube(GameObject):



    def __init__(self, pos: Vec3, res: int) -> None:
        super(Cube, self).__init__()

        #print(Engine.calc_normal(Vec3(step + step * i, step * i, step + step * j) , Vec3(step + step * i, step + step * j, step + step * j) , Vec3(step * i, step + step * j, step + step * j)))
        self.position = pos
        self.triangles = []

        step = 1 / res

        for i in range(res):
            for j in range(res):
                self.triangles += [
                    #TOP
                    Triangle(Vec3(step * i, 1, step * j), Vec3(step + step * i, 1, step * j), Vec3(step * i, 1, step + step * j)),
                    Triangle(Vec3(step + step * i, 1, step * j), Vec3(step + step * i, 1, step + step * j) , Vec3(step * i, 1, step + step * j)),

                    #BOTTOM
                    Triangle(Vec3(step * i, 0, step * j), Vec3(step * i, 0, step + step * j), Vec3(step + step * i, 0, step * j)),
                    Triangle(Vec3(step * i, 0, step + step * j), Vec3(step + step * i, 0, step + step * j), Vec3(step + step * i, 0, step * j)),

                    #LEFT
                    Triangle(Vec3(0, step * i, step * j), Vec3(0, step * i, step + step * j), Vec3(0, step + step * i, step * j)),
                    Triangle(Vec3(0, step * i, step + step * j), Vec3(0, step + step * i, step + step * j), Vec3(0, step + step * i, step * j)),

                    #RIGHT
                    Triangle(Vec3(1, step * i, step * j), Vec3(1, step + step * i, step * j), Vec3(1, step * i, step + step * j)),
                    Triangle(Vec3(1, step + step * i, step * j), Vec3(1, step + step * i, step + step * j), Vec3(1, step * i, step + step * j)),
                
                    #FRONT
                    Triangle(Vec3(step * i, step * j, 1), Vec3(step + step * i, step * j, 1), Vec3(step * i, step + step * j, 1)),
                    Triangle(Vec3(step + step * i, step * j, 1), Vec3(step + step * i, step + step * j, 1), Vec3(step * i, step + step * j, 1)),

                    #BACK
                    Triangle(Vec3(step * i, step * j, 0), Vec3(step * i, step + step * j, 0), Vec3(step + step * i, step * j, 0)),
                    Triangle(Vec3(step * i, step + step * j, 0), Vec3(step + step * i, step + step * j, 0), Vec3(step + step * i, step * j, 0)),

                ]

        #SPHERE
        
        for triangle in self.triangles:
            triangle.points = [*map(lambda x:(x - Vec3(.5, .5, .5)).normalized(), triangle.points),]
        
        Engine.triangles = np.append(Engine.triangles, self.triangles)
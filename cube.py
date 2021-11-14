from mesh import Mesh
from utils import Vec3
from triangle import Triangle

class Cube(Mesh):



    def __init__(self, pos: Vec3, rot: Vec3, res: int) -> None:
        super(Cube, self).__init__(pos, rot)

        #print(Engine.calc_normal(Vec3(step + step * i, step * i, step + step * j) , Vec3(step + step * i, step + step * j, step + step * j) , Vec3(step * i, step + step * j, step + step * j)))
    
        step = 1 / res

        # (0,0) (0,1) (1,0) | (0,1) (1,1) (1,0)

        #X
        #
        #
        #X     X

        for i in range(res):
            for j in range(res):
                self.triangles += [
                    #TOP
                    Triangle(Vec3(step * i, 1, step * j), Vec3(step * i, 1, step + step * j), Vec3(step + step * i, 1, step * j)),
                    Triangle(Vec3(step * i, 1, step + step * j), Vec3(step + step * i, 1, step + step * j), Vec3(step + step * i, 1, step * j)),

                    #BOTTOM
                    Triangle(Vec3(step + step * i, 0, step * j), Vec3(step * i, 0, step + step * j), Vec3(step * i, 0, step * j)),
                    Triangle(Vec3(step + step * i, 0, step * j), Vec3(step + step * i, 0, step + step * j), Vec3(step * i, 0, step + step * j)),

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


        for triangle in self.triangles:
            triangle.points[0] -= Vec3(.5, .5, .5)
            triangle.points[1] -= Vec3(.5, .5, .5)
            triangle.points[2] -= Vec3(.5, .5, .5)
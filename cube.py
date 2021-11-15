from mesh import Mesh
from triangle import Triangle
from utils import Utils

class Cube(Mesh):



    def __init__(self, pos: tuple = [0, 0, 0], rot: tuple = [0, 0, 0], res: int = 1) -> None:
        super(Cube, self).__init__(pos, rot)

        #print(Engine.calc_normal([step + step * i, step * i, step + step * j) , [step + step * i, step + step * j, step + step * j) , [step * i, step + step * j, step + step * j)))
    
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
                    Triangle([step * i, 1, step * j], [step * i, 1, step + step * j], [step + step * i, 1, step * j]),
                    Triangle([step * i, 1, step + step * j], [step + step * i, 1, step + step * j], [step + step * i, 1, step * j]),

                    #BOTTOM
                    Triangle([step + step * i, 0, step * j], [step * i, 0, step + step * j], [step * i, 0, step * j]),
                    Triangle([step + step * i, 0, step * j], [step + step * i, 0, step + step * j], [step * i, 0, step + step * j]),

                    #LEFT
                    Triangle([0, step * i, step * j], [0, step * i, step + step * j], [0, step + step * i, step * j]),
                    Triangle([0, step * i, step + step * j], [0, step + step * i, step + step * j], [0, step + step * i, step * j]),

                    #RIGHT
                    Triangle([1, step * i, step * j], [1, step + step * i, step * j], [1, step * i, step + step * j]),
                    Triangle([1, step + step * i, step * j], [1, step + step * i, step + step * j], [1, step * i, step + step * j]),
                
                    #FRONT
                    Triangle([step * i, step * j, 1], [step + step * i, step * j, 1], [step * i, step + step * j, 1]),
                    Triangle([step + step * i, step * j, 1], [step + step * i, step + step * j, 1], [step * i, step + step * j, 1]),

                    #BACK
                    Triangle([step * i, step * j, 0], [step * i, step + step * j, 0], [step + step * i, step * j, 0]),
                    Triangle([step * i, step + step * j, 0], [step + step * i, step + step * j, 0], [step + step * i, step * j, 0]),
                    
                ]



        for triangle in self.triangles:
            Utils.sub_vec(triangle.points[0], (.5, .5, .5))
            Utils.sub_vec(triangle.points[1], (.5, .5, .5))
            Utils.sub_vec(triangle.points[2], (.5, .5, .5))
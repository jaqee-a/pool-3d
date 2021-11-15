from cube import Cube
from utils import Utils


class Sphere(Cube):

    def __init__(self, pos: tuple = [0, 0, 0], rot: tuple = [0, 0, 0], res: int = 1) -> None:
        super(Sphere, self).__init__(pos, rot, res)

        for triangle in self.triangles:
            for point in triangle.points:
                Utils.normalize(point)
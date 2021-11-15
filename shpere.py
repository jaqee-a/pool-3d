from cube import Cube
from utils import Vec3


class Sphere(Cube):

    def __init__(self, pos: Vec3, rot: Vec3, res: int) -> None:
        super(Sphere, self).__init__(pos, rot, res)

        for triangle in self.triangles:
            for point in triangle.points:
                point.normalize()
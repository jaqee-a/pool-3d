import numpy as np

from utils import *
from math import cos, sin

class Engine:

    meshes = []
    triangles = np.array([])

    @staticmethod
    def rotate(point, rotation):
        cx = cos(rotation.x)
        cy = cos(rotation.y)
        cz = cos(rotation.z)
        sx = sin(rotation.x)
        sy = sin(rotation.y)
        sz = sin(rotation.z)

        return Engine.rotate_cs(point, (cx, cy, cz), (sx, sy, sz))

    def rotate_cs(point, cos, sin):
        cx, cy, cz = cos
        sx, sy, sz = sin

        return Vec3(
            point.x * (cz*cy-sz*sx*sy) - point.y * sz * cx + point.z * (cz*sy+sz*sx*cy),
            point.x * (sz*cy+cz*sx*sy) + point.y * cz * cx + point.z * (sz*sy-cz*sx*cy),
            point.x * cx * -sy + point.y * sx + point.z * cx * cy
        )



    @staticmethod
    def calc_normal(p1: Vec3, p2: Vec3, p3: Vec3):
        return (p2 - p1).cross(p3 - p1).normalized()
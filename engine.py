import numpy as np
from math import cos, sin

from utils import Utils

class Engine:

    meshes = []
    triangles = np.array([])

    @staticmethod
    def rotate(point: tuple, rotation: tuple) -> tuple:
        cx = cos(rotation[0])
        cy = cos(rotation[1])
        cz = cos(rotation[2])
        sx = sin(rotation[0])
        sy = sin(rotation[1])
        sz = sin(rotation[2])

        return Engine.rotate_cs(point, (cx, cy, cz), (sx, sy, sz))

    def rotate_cs(point: tuple, cos: tuple, sin: tuple) -> tuple:
        cx, cy, cz = cos
        sx, sy, sz = sin

        return [
            point[0] * (cz*cy-sz*sx*sy) - point[1] * sz * cx + point[2] * (cz*sy+sz*sx*cy),
            point[0] * (sz*cy+cz*sx*sy) + point[1] * cz * cx + point[2] * (sz*sy-cz*sx*cy),
            point[0] * cx * -sy + point[1] * sx + point[2] * cx * cy
        ]



    @staticmethod
    def calc_normal(p1: tuple, p2: tuple, p3: tuple) -> tuple:
        v1 = Utils.sub_vec_r(p2, p1)
        v2 = Utils.sub_vec_r(p3, p1)
        cr = Utils.cross(v1, v2)
        Utils.normalize(cr)
        
        return cr

class V:
    def __init__(self) -> None:
        self.x = 0

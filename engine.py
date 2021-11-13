import numpy as np

from utils import *
from numpy import cos, sin

class Engine:

    game_objects = []
    triangles = np.array([])

    @staticmethod
    def rotate(point, rotation):

        _rx = np.array([
            [1, 0, 0],
            [0, cos(rotation.x), -sin(rotation.x)],
            [0, sin(rotation.x), cos(rotation.x)]
        ])

        _ry = np.array([
            [cos(rotation.y), 0, sin(rotation.y)],
            [0, 1, 0],
            [-sin(rotation.y), 0, cos(rotation.y)]
        ])

        _rz = np.array([
            [cos(rotation.z), -sin(rotation.z), 0],
            [sin(rotation.z), cos(rotation.z), 0],
            [0, 0, 1]
        ])


        val_ = np.matmul(np.matmul(_rx, _ry), _rz)

        out_ = np.matmul(val_, np.array(point.values()))

        return Vec3.to_vec3(out_)
        """
        out = Vec3(0, 0, 0)

        out.x = point.x * (cos(rotation.z) * cos(rotation.y)) + \
                     point.y * (cos(rotation.z) * sin(rotation.y) * sin(rotation.x) - sin(rotation.z) * cos(rotation.x)) + \
                     point.z * (cos(rotation.z) * sin(rotation.y) * cos(rotation.x) + sin(rotation.z) * sin(rotation.x))

        out.y = point.x * (sin(rotation.z) * cos(rotation.y)) + \
                     point.y * (sin(rotation.z) * sin(rotation.y) * sin(rotation.x) + cos(rotation.z) * cos(rotation.x)) + \
                     point.z * (sin(rotation.z) * sin(rotation.y) * cos(rotation.x) - cos(rotation.z) * sin(rotation.x))
        
        out.z = point.x * (-sin(rotation.y)) + \
                     point.y * (cos(rotation.y) * sin(rotation.x)) + \
                     point.z * (cos(rotation.y) * cos(rotation.x))
                     
        return out
        """


    @staticmethod
    def calc_normal(p1: Vec3, p2: Vec3, p3: Vec3):
        return (p2 - p1).cross(p3 - p1).normalized()
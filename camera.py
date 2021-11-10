from utils import *

from constants import FA, FB, WIDTH, HEIGHT
from math import cos, sin

class Camera:

    main = None

    @staticmethod
    def get_center_uv():
        return Vec2(WIDTH // 2, HEIGHT // 2)

    def __init__(self) -> None:
        self.position = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)

    def world_to_screen_point(self, point: Vec3) -> Vec2:
        point = point - self.position
        point = self.rotate(point, self.rotation)

        u0, v0 = Camera.get_center_uv().values()
        

        if point.z <= 0: point.z = .0005

        xz = point.x / point.z
        yz = point.y / point.z

        return Vec2(FA * xz + u0, FB * yz + v0)


    def rotate(self, point, rotation):
        
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


Camera.main = Camera()
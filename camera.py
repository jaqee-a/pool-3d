from engine import Engine
from gameobject import GameObject
from utils import *

from constants import FA, FB, WIDTH, HEIGHT

class Camera(GameObject):

    main = None

    @staticmethod
    def get_center_uv():
        return Vec2(WIDTH // 2, HEIGHT // 2)

    def world_to_screen_point(self, point: Vec3) -> Vec2:
        cam_points = point - self.position
        cam_points = Engine.rotate_cs(cam_points, self.cos, self.sin)

        u0, v0 = Camera.get_center_uv().values()
        

        if cam_points.z <= 0: cam_points.z = .0005

        xz = cam_points.x / cam_points.z
        yz = cam_points.y / cam_points.z


        uv_ = Vec2(FA * xz + u0, FB * yz + v0)

        return uv_

Camera.main = Camera()
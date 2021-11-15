from engine import Engine
from gameobject import GameObject
from utils import Utils

from constants import FA, FB, WIDTH, HEIGHT

class Camera(GameObject):

    main = None

    @staticmethod
    def get_center_uv():
        return (WIDTH // 2, HEIGHT // 2)

    def world_to_screen_point(self, point: tuple) -> tuple:
        cam_points = Utils.sub_vec_r(point, self.position)
        cam_points = Engine.rotate_cs(cam_points, self.cos, self.sin)

        u0, v0 = Camera.get_center_uv()
        
        if cam_points[2] <= 0: cam_points[2] = .0005

        xz = cam_points[0] / cam_points[2]
        yz = cam_points[1] / cam_points[2]


        uv_ = (FA * xz + u0, FB * yz + v0)

        return uv_

Camera.main = Camera()
from utils import Utils
from camera import *
from light import *

import pygame


class Triangle:

    def __init__(self, p1: tuple, p2: tuple, p3: tuple) -> None:
        self.points = [p1, p2, p3]
        self.avg_z = 0

    def get_avg_z(self):
        return self.avg_z

    def get_center(self):
        return Utils.div_r(Utils.add_r(Utils.add_r(self.points[0], self.points[1]), self.points[2]), 3)

    # TODO Delete
    def draw(self, screen):
        points = [*map(lambda x:Camera.main.world_to_screen_point(x).values(), self.points),]

        #_light_percent = max(0, -Engine.calc_normal(*self.points).dot(Light.g_light.direction))
        _light_percent = 1
        if(all(map(lambda x:x[0] > 0 and x[0] < WIDTH and x[1] > 0 and x[1] < HEIGHT, points))):
            pygame.draw.line(screen, (0, 0, 0), points[0], points[1])
            pygame.draw.line(screen, (0, 0, 0), points[1], points[2])
            pygame.draw.line(screen, (0, 0, 0), points[0], points[2])
            #pygame.draw.polygon(screen, color=[*map(abs,Vec3.mul(Engine.calc_normal(*self.points), 255 * min(1, .2 + _light_percent)).values()),], points=points)

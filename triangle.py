from utils import *
from camera import *
from light import *

import pygame


class Triangle:

    def __init__(self, p1: Vec3, p2: Vec3, p3: Vec3) -> None:
        self.points = [p1, p2, p3]


    def get_avg_z(self):
        points = [*map(lambda x:(Engine.rotate(x, Camera.main.rotation)-Camera.main.position), self.points),]
        p1, p2, p3 = points
        return (p1.z + p2.z + p3.z) / 3.0



    def draw(self, screen):
        points = [*map(lambda x:Camera.main.world_to_screen_point(x).values(), self.points),]

        _light_percent = max(0, -Engine.calc_normal(*self.points).dot(Light.g_light.direction))

        if(all(map(lambda x:x[0] > 0 and x[0] < WIDTH and x[1] > 0 and x[1] < HEIGHT, points))):
            pygame.draw.polygon(screen, color=(255 * min(1, _light_percent), 0,0), points=points)
        
        
        
        
        
        #print(points)

        '''
        pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 5)
        pygame.draw.line(screen, (255, 255, 255), points[1], points[2], 5)
        pygame.draw.line(screen, (255, 255, 255), points[0], points[2], 5)
        
        pygame.draw.line(screen, (255, 255, 255), Camera.main.world_to_screen_point(self.points[0]).values(), Camera.main.world_to_screen_point(self.points[1]).values(), 5)
        pygame.draw.line(screen, (255, 255, 255), Camera.main.world_to_screen_point(self.points[1]).values(), Camera.main.world_to_screen_point(self.points[2]).values(), 5)
        pygame.draw.line(screen, (255, 255, 255), Camera.main.world_to_screen_point(self.points[0]).values(), Camera.main.world_to_screen_point(self.points[2]).values(), 5)
        '''
from gameobject import *
from triangle import *

class Mesh(GameObject):

    def __init__(self, position = Vec3(0, 0, 0), rotation = Vec3(0, 0, 0)) -> None:
        super().__init__()

        self.position = position
        self.rotation = rotation

        self.triangles = []

        Engine.meshes += [self]



    def draw(self, screen):

        self.calc_cs()

        for triangle in self.triangles:
            rotated_p1 = Engine.rotate_cs(triangle.points[0], self.cos, self.sin)
            rotated_p2 = Engine.rotate_cs(triangle.points[1], self.cos, self.sin)
            rotated_p3 = Engine.rotate_cs(triangle.points[2], self.cos, self.sin)

            translated_1 = rotated_p1 + self.position
            translated_2 = rotated_p2 + self.position
            translated_3 = rotated_p3 + self.position

            cen = Vec3.div(translated_1 + translated_2 + translated_3, 3)

            cam_ = cen - Camera.main.position

            norm = Engine.calc_normal(translated_1, translated_2, translated_3)

            v_ = norm.dot(cam_)
            
            # _normal_line_start = Camera.main.world_to_screen_point(cen).values()
            # _normal_line_end = Camera.main.world_to_screen_point(cen + norm).values()
            
            if 0 or v_ < 0:
                #pygame.draw.line(screen, (0, 255, 0), _normal_line_start, _normal_line_end, 3)
                
                uv1 = Camera.main.world_to_screen_point(translated_1).values()
                uv2 = Camera.main.world_to_screen_point(translated_2).values()
                uv3 = Camera.main.world_to_screen_point(translated_3).values()
        
                # pygame.draw.polygon(screen, [*map(abs,Vec3.mul(norm, 255).values()),], (uv1, uv2, uv3))
                pygame.draw.line(screen, (0, 0, 0), uv1, uv2, 3)
                pygame.draw.line(screen, (0, 0, 0), uv1, uv3, 3)
                pygame.draw.line(screen, (0, 0, 0), uv3, uv2, 3)
            
import pygame
from pygame import key
from camera import Camera

from constants import HEIGHT, WIDTH, FPS
from keyboard import Keyboard
from utils import Vec3


cpoints_ = [
    []
]

class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()


        self.debut = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pool")

        self.clock = pygame.time.Clock()
        

        self.sprites = pygame.sprite.Group()


        self.running = False


    def run(self):
        running = True
    
        while running:
            self.screen.fill((0, 0, 0))
            delta_time = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    Keyboard.add_key(event.key)

                if event.type == pygame.KEYUP:
                    Keyboard.remove_key(event.key)

            

            for key_held in Keyboard.held_keys:
                #TODO Keyboard handler
                if key_held == pygame.K_z:
                    Camera.main.position += Vec3.mul(Vec3(0, 0, 1), delta_time)
                if key_held == pygame.K_s:
                    Camera.main.position += Vec3.mul(Vec3(0, 0, -1), delta_time)
                if key_held == pygame.K_d:
                    Camera.main.position += Vec3.mul(Vec3(1, 0, 0), delta_time)
                if key_held == pygame.K_q:
                    Camera.main.position += Vec3.mul(Vec3(-1, 0, 0), delta_time)
                if key_held == pygame.K_SPACE:
                    Camera.main.position += Vec3.mul(Vec3(0, 1, 0), delta_time * 5)
                if key_held == pygame.K_LCTRL:
                    Camera.main.position += Vec3.mul(Vec3(0, -1, 0), delta_time * 5)
                if key_held == pygame.K_LEFT:
                    Camera.main.rotation += Vec3.mul(Vec3(0, 1, 0), delta_time)
                if key_held == pygame.K_RIGHT:
                    Camera.main.rotation += Vec3.mul(Vec3(0, -1, 0), delta_time)

            self.sprites.update()


            ##############
            pos0=Camera.main.world_to_screen_point(Vec3(-1, 0, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 0, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, 2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, 0, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, 2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(1, 0, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, 0, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 0, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, 2, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, 0, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, 2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(1, 0, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            #DO WHAT EVER
            pos0=Camera.main.world_to_screen_point(Vec3(-1, 0, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, 0, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(1, 0, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 0, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(-1, 2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, 2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(1, 2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, 2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            ##############

            
            ##############
            pos0=Camera.main.world_to_screen_point(Vec3(-1, -4, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -4, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, -2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, -4, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, -2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(1, -4, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -2, 1)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, -4, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -4, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, -2, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(-1, -4, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, -2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            pos0=Camera.main.world_to_screen_point(Vec3(1, -4, 2)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            #DO WHAT EVER
            pos0=Camera.main.world_to_screen_point(Vec3(-1, -4, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, -4, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(1, -4, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -4, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(-1, -2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(-1, -2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)
            
            pos0=Camera.main.world_to_screen_point(Vec3(1, -2, 1)).values()
            pos1=Camera.main.world_to_screen_point(Vec3(1, -2, 2)).values()
            pygame.draw.line(self.screen, (255, 255, 255), pos0, pos1, 5)

            ##############


            self.sprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
import numpy as np
import pygame
from camera import Camera

from constants import HEIGHT, WIDTH, FPS
from keyboard import Keyboard
from shpere import Sphere
from utils import Vec3
from cube import *

class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()


        self.debut = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pool")

        self.clock = pygame.time.Clock()

        
        Cube(Vec3(0, 0,  5), Vec3(0, 0, 0), 2)
        Cube(Vec3(0, 0, 10), Vec3(0, 0, 0), 2)
        Cube(Vec3(0, 0, 15), Vec3(0, 0, 0), 2)
        Cube(Vec3(0, 0, 20), Vec3(0, 0, 0), 2)

        Sphere(Vec3(5, 0,  5), Vec3(0, 0, 0), 2)
        Sphere(Vec3(5, 0, 10), Vec3(0, 0, 0), 2)
        Sphere(Vec3(5, 0, 15), Vec3(0, 0, 0), 2)
        Sphere(Vec3(5, 0, 20), Vec3(0, 0, 0), 2)


        self.running = False

    def handle_keys(self):
        for key_held in Keyboard.held_keys:
            if key_held == pygame.K_z:
                Camera.main.position += Vec3.mul(Camera.main.forward(), self.delta_time * 5)
            if key_held == pygame.K_s:
                Camera.main.position += Vec3.mul(Camera.main.backward(), self.delta_time * 5)
            if key_held == pygame.K_d:
                Camera.main.position += Vec3.mul(Camera.main.right(), self.delta_time * 5)
            if key_held == pygame.K_q:
                Camera.main.position += Vec3.mul(Camera.main.left(), self.delta_time * 5)
            if key_held == pygame.K_SPACE:
                Camera.main.position += Vec3.mul(Vec3(0, 1, 0), self.delta_time * 5)
            if key_held == pygame.K_LCTRL:
                Camera.main.position += Vec3.mul(Vec3(0, -1, 0), self.delta_time * 5)
            if key_held == pygame.K_LEFT:
                Camera.main.rotation += Vec3.mul(Vec3(0, 1, 0), self.delta_time)
            if key_held == pygame.K_RIGHT:
                Camera.main.rotation += Vec3.mul(Vec3(0, -1, 0), self.delta_time)
            if key_held == pygame.K_UP:
                Camera.main.rotation += Vec3.mul(Vec3(1, 0, 0), self.delta_time)
            if key_held == pygame.K_DOWN:
                Camera.main.rotation += Vec3.mul(Vec3(-1, 0, 0), self.delta_time)



    def run(self):
        running = True
        image = pygame.Surface((WIDTH, HEIGHT))
        
        while running:
            image.fill((175, 255, 175))
            self.delta_time = self.clock.tick(FPS) / 1000
            print(self.clock.get_fps())
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    Keyboard.add_key(event.key)

                if event.type == pygame.KEYUP:
                    Keyboard.remove_key(event.key)

            
            self.handle_keys()



            Camera.main.calc_cs()
            for mesh in Engine.meshes:
                mesh.draw(image)


            self.screen.blit(pygame.transform.flip(image, False, True), (0, 0))
            pygame.display.flip()

        pygame.quit()
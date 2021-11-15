import pygame

from constants import HEIGHT, WIDTH, FPS

from engine import Engine
from camera import Camera
from mesh import Mesh
from keyboard import Keyboard
from objparser import ObjParser
from shpere import Sphere
from cube import Cube
from utils import Utils

class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()


        self.debut = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pool")

        self.clock = pygame.time.Clock()

        """
        Cube([0, 0,  5], [0, 0, 0], 2)
        Cube([0, 0, 10], [0, 0, 0], 2)
        Cube([0, 0, 15], [0, 0, 0], 2)
        Cube([0, 0, 20], [0, 0, 0], 2)

        Sphere([5, 0,  5], [0, 0, 0], 2)
        Sphere([5, 0, 10], [0, 0, 0], 2)
        Sphere([5, 0, 15], [0, 0, 0], 2)
        Sphere([5, 0, 20], [0, 0, 0], 2)
        """
        self.table = ObjParser.parse("assets/Btable.obj")

        self.running = False

    def handle_keys(self):
        for key_held in Keyboard.held_keys:
            if key_held == pygame.K_z:
                Utils.add_vec(Camera.main.position, Utils.mul_r(Camera.main.forward(), self.delta_time * 5))
            if key_held == pygame.K_s:
                Utils.add_vec(Camera.main.position, Utils.mul_r(Camera.main.backward(), self.delta_time * 5))
            if key_held == pygame.K_d:
                Utils.add_vec(Camera.main.position, Utils.mul_r(Camera.main.right(), self.delta_time * 5))
            if key_held == pygame.K_q:
                Utils.add_vec(Camera.main.position, Utils.mul_r(Camera.main.left(), self.delta_time * 5))
            if key_held == pygame.K_SPACE:
                Utils.add_vec(Camera.main.position, Utils.mul_r((0, 1, 0), self.delta_time * 5))
            if key_held == pygame.K_LCTRL:
                Utils.add_vec(Camera.main.position, Utils.mul_r((0, -1, 0), self.delta_time * 5))
            if key_held == pygame.K_LEFT:
                Utils.add_vec(Camera.main.rotation, Utils.mul_r((0, 1, 0), self.delta_time))
            if key_held == pygame.K_RIGHT:
                Utils.add_vec(Camera.main.rotation, Utils.mul_r((0, -1, 0), self.delta_time))
            if key_held == pygame.K_UP:
                Utils.add_vec(Camera.main.rotation, Utils.mul_r((1, 0, 0), self.delta_time))
            if key_held == pygame.K_DOWN:
                Utils.add_vec(Camera.main.rotation, Utils.mul_r((-1, 0, 0), self.delta_time))



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



            Engine.meshes.sort(key=Mesh.get_avg_z, reverse=True)

            Camera.main.calc_cs()
            
            for mesh in Engine.meshes:
                mesh.draw(image)


            self.screen.blit(pygame.transform.flip(image, False, True), (0, 0))
            pygame.display.flip()

        pygame.quit()
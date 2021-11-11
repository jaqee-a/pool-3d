from gameobject import *



class Light(GameObject):
    g_light = None

    def __init__(self) -> None:
        super().__init__()

        self.direction = Vec3(.5, 1, -.5)


Light.g_light = Light()
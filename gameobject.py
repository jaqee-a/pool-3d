from math import cos, sin
from engine import Engine
from utils import Utils


class GameObject:


    def __init__(self, pos: list = [0, 0, 0], rot: list = [0, 0, 0]) -> None:
        self.position = pos
        self.rotation = rot

        self.cos = self.sin = (0, 0, 0)


    def calc_cs(self):
        self.cos = (cos(self.rotation[0]), cos(self.rotation[1]), cos(self.rotation[2]))
        self.sin = (sin(self.rotation[0]), sin(self.rotation[1]), sin(self.rotation[2]))


    def forward(self):
        return Engine.rotate((0, 0, 1), Utils.mul_r(self.rotation, -1))


    def backward(self):
        return Utils.mul_r(self.forward(), -1)


    def right(self):
        return Engine.rotate((1, 0, 0), Utils.mul_r(self.rotation, -1))

    def left(self):
        return Utils.mul_r(self.right(), -1)


    def up(self):
        return Engine.rotate((0, 1, 0), Utils.mul_r(self.rotation, -1))

    def down(self):
        return Utils.mul_r(self.up(), -1)

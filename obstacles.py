import pyxel
import random


class Obstacle:
    def __init__(self, x, speed=None):
        self.x = x
        self.speed = speed
        self.y = 8
        self.w = 16
        self.h = 16

    def is_offscreen(self):
        return self.x + self.w < 0

    def update(self):
        self.x -= self.speed

    def draw(self):
        pyxel.rectb(self.x, self.y, self.w, self.h, pyxel.COLOR_BLACK)


class SmallCactus(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 63
        self.w = 5
        self.h = 7

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class LargeCactus(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 58
        self.w = 8
        self.h = 14

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class SpikedBush(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 59
        self.w = 16
        self.h = 11

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class Pterodactyl(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = random.choices([54, 39, 60], weights=[70, 10, 20], k=1)[0]
        self.w = 9
        self.h = 7

    def update(self):
        super().update()

    def draw(self):
        super().draw()

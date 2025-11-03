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
        self.h = 5

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x, self.y - 9, 0, 16, 32, 16, 16, pyxel.COLOR_PEACH)
        # pyxel.rectb(self.x + 5, self.y, self.w, self.h, pyxel.COLOR_RED)


class LargeCactus(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 58
        self.w = 8
        self.h = 14

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x - 3, self.y - 4, 0, 32, 32, 16, 16, pyxel.COLOR_PEACH)


class SpikedBush(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 59
        self.w = 16
        self.h = 11

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x, self.y - 3, 0, 48, 32, 16, 16, pyxel.COLOR_PEACH)


class Pterodactyl(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = random.choices([54, 39, 60], weights=[70, 10, 20], k=1)[0]
        self.w = 9
        self.h = 7

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x - 3, self.y - 8, 0, ((pyxel.frame_count // 5) %
                  2) * 16, 48, 16, 16, pyxel.COLOR_PEACH)

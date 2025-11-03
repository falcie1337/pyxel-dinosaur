import pyxel


class Obstacle:
    def __init__(self, x, speed=None):
        self.x = x
        self.vx = speed
        self.y = 8
        self.w = 16
        self.h = 16

    def is_offscreen(self):
        return self.x + self.w < 0

    def update(self):
        self.x -= self.vx

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, pyxel.COLOR_BLACK)


class SmallCactus(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 61
        self.w = 6
        self.h = 9

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class LargeCactus(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 58
        self.w = 10
        self.h = 12

    def update(self):
        super().update()

    def draw(self):
        super().draw()


class Pterodactyl(Obstacle):
    def __init__(self, x, speed=None):
        super().__init__(x, speed)
        self.y = 50
        self.w = 13
        self.h = 11

    def update(self):
        super().update()

    def draw(self):
        super().draw()

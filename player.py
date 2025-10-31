import pyxel


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = 0
        self.gravity = 0.4
        self.JUMP_FORCE = 4
        self.GROUND_Y = 100

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -self.JUMP_FORCE

        self.vy += self.gravity
        self.y += self.vy

        if self.y >= self.GROUND_Y:
            self.y = self.GROUND_Y
            self.vy = 0

    def draw(self):
        pyxel.rect(self.x, self.y, 16, 16, pyxel.COLOR_WHITE)

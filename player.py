import pyxel


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = 0
        self.gravity = 0.7
        self.hold_jump = False
        self.jump_hold_timer = 0
        self.MAX_JUMP_HOLD = 8
        self.JUMP_FORCE = 4.5
        self.GROUND_Y = 54
        self.on_ground = False
        self.can_jump = False
        pyxel.load("my_resource.pyxres")

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and self.can_jump:
            self.vy = -self.JUMP_FORCE
            self.hold_jump = True
            self.jump_hold_timer = 0

        if self.hold_jump and self.jump_hold_timer < self.MAX_JUMP_HOLD and pyxel.btn(pyxel.KEY_SPACE):
            self.vy -= 0.5
            self.jump_hold_timer += 1
        else:
            self.hold_jump = False

        self.vy += self.gravity
        self.y += self.vy

        if self.y >= self.GROUND_Y:
            self.y = self.GROUND_Y
            self.vy = 0
            self.on_ground = True
            self.can_jump = True
        else:
            self.on_ground = False
            self.can_jump = False

    def draw(self):
        pyxel.blt(self.x, self.y, u=0, v=0, img=0, w=16, h=16)

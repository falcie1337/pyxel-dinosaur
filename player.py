import pyxel


class Player:
    def __init__(self, x, y):
        # position and physics attributes
        self.x = x
        self.y = y
        self.vy = 0
        self.GRAVITY = 0.7
        self.hold_jump = False
        self.jump_hold_timer = 0
        self.hold_duck = False
        self.MAX_JUMP_HOLD = 8
        self.JUMP_FORCE = 4.5
        self.GROUND_Y = 54

        # state attributes
        self.is_ducking = False
        self.on_ground = False
        self.can_jump = False

    def update(self):

        # jumping
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.can_jump or
                pyxel.btnp(pyxel.KEY_UP) and self.can_jump):
            self.vy = -self.JUMP_FORCE
            self.hold_jump = True
            self.jump_hold_timer = 0

        if (self.hold_jump and self.jump_hold_timer < self.MAX_JUMP_HOLD
            and pyxel.btn(pyxel.KEY_SPACE) or
            self.hold_jump and self.jump_hold_timer < self.MAX_JUMP_HOLD
                and pyxel.btn(pyxel.KEY_UP)):
            self.vy -= 0.5
            self.jump_hold_timer += 1
        else:
            self.hold_jump = False

        # ducking
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.is_ducking = True

        if pyxel.btnr(pyxel.KEY_DOWN):
            self.is_ducking = False

        # applying gravity
        self.vy += self.GRAVITY
        self.y += self.vy

        # ground collision checking
        if self.y >= self.GROUND_Y:
            self.y = self.GROUND_Y
            self.vy = 0
            self.on_ground = True
            self.can_jump = True
        else:
            self.on_ground = False
            self.can_jump = False

    def draw(self):
        state = ""
        if self.on_ground and not self.is_ducking:
            state = "walking"

        if not self.on_ground and not self.is_ducking:
            state = "jumping"
            pyxel.blt(self.x, self.y, 0, 48, 0,
                      16, 16, pyxel.COLOR_LIGHT_BLUE)

        if self.is_ducking and self.on_ground:
            state = "ducking"
            index_duck = ((pyxel.frame_count // 3) % 3) * 16
            pyxel.blt(self.x, self.y, 0, index_duck, 16,
                      16, 16, pyxel.COLOR_LIGHT_BLUE)

        if self.is_ducking and not self.on_ground:
            state = "duck_jumping"
            pyxel.blt(self.x, self.y, 0, 48, 16,
                      16, 16, pyxel.COLOR_LIGHT_BLUE)

        u = 0
        v = 0
        if state == "walking":
            u = ((pyxel.frame_count // 3) % 3) * 16
            v = 0

        if state == "ducking":
            u = ((pyxel.frame_count // 3) % 3) * 16
            v = 16

        if state == "jumping":
            u = 48
            v = 0

        if state == "duck_jumping":
            u = 48
            v = 16

        pyxel.blt(self.x, self.y, 0, u, v, 16, 16, pyxel.COLOR_LIGHT_BLUE)

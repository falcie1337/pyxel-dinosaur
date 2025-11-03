import pyxel


class Player:
    def __init__(self, x, y):
        # position attributes
        self.x = x
        self.y = y

        # physics attributes
        self.vy = 0
        self.GRAVITY = 0.7
        self.hold_jump = False
        self.jump_hold_timer = 0
        self.hold_duck = False
        self.MAX_JUMP_HOLD = 4
        self.JUMP_FORCE = 3.5

        # hitbox attributes
        self.hit_width = 10
        self.hit_height = 12
        self.hit_offsetx = 2
        self.hit_offsety = 2
        self.hitbox_debug = True

        # state attributes
        self.is_ducking = False
        self.on_ground = False
        self.can_jump = False

    def update_hitbox(self):
        # update hitbox position
        if self.is_ducking:
            height = 6
            offsety = 8
            width = 14
            offsetx = 2
        else:
            height = self.hit_height
            offsety = self.hit_offsety
            width = self.hit_width
            offsetx = self.hit_offsetx

        self.hitx = int(self.x + offsetx)
        self.hity = int(self.y + offsety)
        self.hitw = int(width)
        self.hith = int(height)

    def jump(self):
        # jumping
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.can_jump or
                pyxel.btnp(pyxel.KEY_UP) and self.can_jump):
            self.vy = -self.JUMP_FORCE
            self.hold_jump = True
            self.jump_hold_timer = 0

        # variable jump height
        if (self.hold_jump and self.jump_hold_timer < self.MAX_JUMP_HOLD
            and pyxel.btn(pyxel.KEY_SPACE) or
            self.hold_jump and self.jump_hold_timer < self.MAX_JUMP_HOLD
                and pyxel.btn(pyxel.KEY_UP)):
            self.vy -= 0.5
            self.jump_hold_timer += 1
        else:
            self.hold_jump = False

    def duck(self):
        # ducking
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.is_ducking = True

        if pyxel.btnr(pyxel.KEY_DOWN):
            self.is_ducking = False

        # gravity adjustment when duck jumping
        if self.is_ducking and not self.on_ground:
            self.vy += 1

    def gravity(self):
        # applying gravity
        self.vy += self.GRAVITY
        self.y += self.vy

        # ground collision checking
        if self.y >= 54:
            self.y = 54
            self.vy = 0
            self.on_ground = True
            self.can_jump = True
        else:
            self.on_ground = False
            self.can_jump = False

    def update(self):
        self.jump()
        self.duck()
        self.gravity()
        self.update_hitbox()
        print(self.y)

    def draw(self):
        # determine animation state
        state = ""
        if self.on_ground and not self.is_ducking:
            state = "walking"

        if not self.on_ground and not self.is_ducking:
            state = "jumping"

        if self.is_ducking and self.on_ground:
            state = "ducking"

        if self.is_ducking and not self.on_ground:
            state = "duck_jumping"

        # determine which frame to draw
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

        # draw the player sprite
        pyxel.blt(self.x, self.y, 0, u, v, 16, 16, pyxel.COLOR_PEACH)

        # draw the hitbox debug
        if self.hitbox_debug:
            pyxel.rectb(self.hitx, self.hity, self.hitw,
                        self.hith, pyxel.COLOR_BLACK)

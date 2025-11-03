import pyxel
import random
from obstacles import SmallCactus, LargeCactus, Pterodactyl, SpikedBush


class GameManager:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_multiplier = 1
        self.game_speed = 3
        self.obstacles = []

        self.spawn_timer = random.randint(80, 200)

    def try_spawn(self):
        self.spawn_timer -= 1
        if self.spawn_timer <= 0:
            return

        if self.obstacles:
            last_obstacle = self.obstacles[-1]
            if last_obstacle.x > pyxel.width - random.randint(100, 250):
                return

        if self.score < 400:
            obstacle_type = random.choice(
                [SmallCactus, LargeCactus, SpikedBush])
        else:
            obstacle_type = random.choices(
                [SmallCactus, LargeCactus, SpikedBush, Pterodactyl],
                weights=[40, 45, 30, 15], k=1)[0]

        new_obstacle = obstacle_type(pyxel.width, self.game_speed)
        self.obstacles.append(new_obstacle)

        base_min, base_max = 80, 200
        scale = max(0, 3, 1.0 - (self.game_speed - 3.0) * 0.15)
        min_delay = int(base_min * scale)
        max_delay = int(base_max * scale)
        self.spawn_timer = random.randint(min_delay, max_delay)

    def aabb_check(self, player):
        for obs in self.obstacles:
            if (player.hitx < obs.x + obs.w and
                player.hitx + player.hitw > obs.x and
                player.hity < obs.y + obs.h and
                    player.hity + player.hith > obs.y):
                return True
        return False

    def update_obstacles(self):
        for obstacles in self.obstacles:
            obstacles.speed = self.game_speed
            obstacles.update()
        self.obstacles = [
            obs for obs in self.obstacles if not obs.is_offscreen()]

    def update_score(self):
        self.score += 0.3 * self.score_multiplier

        if self.score > 6400:
            self.game_speed = 5.0
            self.score_multiplier = 5
        elif self.score > 3200:
            self.game_speed = 4.5
            self.score_multiplier = 4
        elif self.score > 1600:
            self.game_speed = 4.2
            self.score_multiplier = 3.5
        elif self.score > 800:
            self.game_speed = 4.0
            self.score_multiplier = 3
        elif self.score > 400:
            self.game_speed = 3.5
            self.score_multiplier = 2.5
        elif self.score > 200:
            self.game_speed = 3.2
            self.score_multiplier = 2
        else:
            self.game_speed = 3.0

    def update(self, player):
        if player.is_dead:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                self.score = 0
                self.game_speed = 3
                self.obstacles = []
                player.is_dead = False
            return
        self.update_score()
        self.try_spawn()
        self.update_obstacles()
        if self.aabb_check(player):
            player.is_dead = True
            if self.score > self.high_score:
                self.high_score = int(self.score)

    def draw(self, player):
        for obstacles in self.obstacles:
            obstacles.draw()
        score_str = str(int(self.score)).zfill(5)
        hi_str = "HI " + str(int(self.high_score)).zfill(5)
        pyxel.text(pyxel.width - len(score_str) * 4 -
                   4, 4, score_str, pyxel.COLOR_GRAY)
        pyxel.text(pyxel.width - len(hi_str) * 4 -
                   4, 12, hi_str, pyxel.COLOR_GRAY)
        if player.is_dead:
            pyxel.text(pyxel.width // 2 - 30,
                       pyxel.height // 2 - 4,
                       "GAME OVER - PRESS UP OR SPACE", pyxel.COLOR_BLACK)

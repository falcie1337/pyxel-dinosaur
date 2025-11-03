import pyxel


class GameManager:
    def __init__(self):
        self.score = 0
        self.score_multiplier = 1
        self.game_speed = 1.5
        self.obstacles = []

        self.spawn_timer = 0

    def update_score(self):
        self.score += 0.3 * self.score_multiplier

        if self.score > 6400:
            self.game_speed = 3.0
            self.score_multiplier = 5
        elif self.score > 3200:
            self.game_speed = 2.8
            self.score_multiplier = 4
        elif self.score > 1600:
            self.game_speed = 2.5
            self.score_multiplier = 3.5
        elif self.score > 800:
            self.game_speed = 2.2
            self.score_multiplier = 3
        elif self.score > 400:
            self.game_speed = 2.0
            self.score_multiplier = 2.5
        elif self.score > 200:
            self.game_speed = 1.8
            self.score_multiplier = 2
        else:
            self.game_speed = 1.5

    def update(self, player):
        self.update_score()

    def draw(self):
        score_str = str(int(self.score)).zfill(5)
        pyxel.text(pyxel.width - len(score_str) * 4 -
                   4, 4, score_str, pyxel.COLOR_GRAY)

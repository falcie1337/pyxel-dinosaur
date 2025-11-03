import pyxel
from player import Player
from game_manager import GameManager


class Main:
    def __init__(self):
        pyxel.init(200, 70, display_scale=3, title="test")
        pyxel.load("my_resource.pyxres")
        self.player = Player(20, 10)
        self.game_manager = GameManager()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.game_manager.update(self.player)

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        self.player.draw()
        self.game_manager.draw()


def aabb(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
            )


Main()

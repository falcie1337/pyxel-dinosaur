import pyxel
from player import Player


class Main:
    def __init__(self):
        pyxel.init(160, 120, display_scale=3, title="test")
        self.player = Player(72, 60)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.player.draw()


Main()

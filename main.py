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
        self.game_manager.draw(self.player)


Main()

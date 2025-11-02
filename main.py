import pyxel
from player import Player
from obstacles import SmallCactus, LargeCactus, Pterodactyl


class Main:
    def __init__(self):
        pyxel.init(200, 70, display_scale=3, title="test")
        pyxel.load("my_resource.pyxres")
        self.player = Player(40, 10)
        self.obstacle = SmallCactus(130, 1.5)
        self.obstacle2 = LargeCactus(195, 1.5)
        self.obstacle3 = Pterodactyl(175, 1.5)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.obstacle.update()
        self.obstacle2.update()
        self.obstacle3.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        self.player.draw()
        self.obstacle.draw()
        self.obstacle2.draw()
        self.obstacle3.draw()


def aabb(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
            )


Main()

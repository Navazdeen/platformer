from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
import random
from itertools import cycle

if TYPE_CHECKING:
    from main import Game


class BoxTile(Tile):
    BOX = "box.png"
    BOXALT = "boxAlt.png"
    BOXCOIN = "boxCoin.png"
    BOXCOINALT = "boxCoinAlt.png"
    BOXCOINALT_DISABLED = "boxCoinAlt_disabled.png"
    BOXCOIN_DISABLED = "boxCoin_disabled.png"
    BOXEMPTY = "boxEmpty.png"
    BOXEXPLOSIVE = "boxExplosive.png"
    BOXEXPLOSIVEALT = "boxExplosiveAlt.png"
    BOXEXPLOSIVE_DISABLED = "boxExplosive_disabled.png"
    BOXITEM = "boxItem.png"
    BOXITEMALT = "boxItemAlt.png"
    BOXITEMALT_DISABLED = "boxItemAlt_disabled.png"
    BOXITEM_DISABLED = "boxItem_disabled.png"
    BOXWARNING = "boxWarning.png"
    tilepath: Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\box")

    def __init__(
        self,
        game: "Game",
        state: str = BOX,
        initial_position: Vector2 = Vector2(0, 0),
        color: str = None,
    ):
        super().__init__(state, game, initial_position, color)
        self.destroyed = False
        self.jitter = None

    def collide(self, other: Tile):
        super().collide(other)
        if self.state == self.BOXEXPLOSIVE:
            if not self.destroyed:
                self.game.world.destroy_tile(self, timer=2)
            self.destroyed = True
        if random.random() < 0.01:
            self.state = self.BOXEXPLOSIVE

    def _init_jitter(self, strength: int = 1):
        def _jitter_generator(strength):
            cyc = cycle([strength, 0, -strength])
            for c in cyc:
                yield c

        if self.jitter is None:
            self.jitter = _jitter_generator(strength)

    def update(self):
        self._init_jitter(2)
        if self.state == self.BOXEXPLOSIVE and self.destroyed:
            # Apply a jitter only in the x-axis between -1 and +1
            jitter_x = next(self.jitter)
            self.rect.x += jitter_x

        super().update()

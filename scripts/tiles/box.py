from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
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
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\box")
    def __init__(self, game:"Game", state: str = BOX, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


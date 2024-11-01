from utils.spriteLoader import Tile
from pathlib import Path

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

class BoxTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\box")
    def __init__(self, state: str = BOX, color: str = None):
        super().__init__(state, color)


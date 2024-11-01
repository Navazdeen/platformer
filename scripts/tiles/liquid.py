from utils.spriteLoader import Tile
from pathlib import Path

LIQUIDLAVA = "liquidLava.png"
LIQUIDLAVATOP = "liquidLavaTop.png"
LIQUIDLAVATOP_MID = "liquidLavaTop_mid.png"
LIQUIDWATER = "liquidWater.png"
LIQUIDWATERTOP = "liquidWaterTop.png"
LIQUIDWATERTOP_MID = "liquidWaterTop_mid.png"

class LiquidTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\liquid")
    def __init__(self, state: str = LIQUIDLAVA, color: str = None):
        super().__init__(state, color)


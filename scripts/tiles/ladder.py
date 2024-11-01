from utils.spriteLoader import Tile
from pathlib import Path

LADDER_MID = "ladder_mid.png"
LADDER_TOP = "ladder_top.png"

class LadderTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\ladder")
    def __init__(self, state: str = LADDER_MID, color: str = None):
        super().__init__(state, color)


from utils.spriteLoader import Tile
from pathlib import Path

TOCHLIT = "tochLit.png"
TOCHLIT2 = "tochLit2.png"

class TochTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\toch")
    def __init__(self, state: str = TOCHLIT, color: str = None):
        super().__init__(state, color)


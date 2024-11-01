from utils.spriteLoader import Tile
from pathlib import Path

ROPEATTACHED = "ropeAttached.png"
ROPEHORIZONTAL = "ropeHorizontal.png"
ROPEVERTICAL = "ropeVertical.png"

class RopeTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\rope")
    def __init__(self, state: str = ROPEATTACHED, color: str = None):
        super().__init__(state, color)


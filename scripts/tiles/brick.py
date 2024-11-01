from utils.spriteLoader import Tile
from pathlib import Path

BRICKWALL = "brickWall.png"

class BrickTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\brick")
    def __init__(self, state: str = BRICKWALL, color: str = None):
        super().__init__(state, color)


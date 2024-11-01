from utils.spriteLoader import Tile
from pathlib import Path

HILL_LARGE = "hill_large.png"
HILL_LARGEALT = "hill_largeAlt.png"
HILL_SMALL = "hill_small.png"
HILL_SMALLALT = "hill_smallAlt.png"

class HillTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\hill")
    def __init__(self, state: str = HILL_LARGE, color: str = None):
        super().__init__(state, color)


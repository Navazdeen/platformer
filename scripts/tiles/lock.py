from utils.spriteLoader import Tile
from pathlib import Path

LOCK_BLUE = "lock_blue.png"
LOCK_GREEN = "lock_green.png"
LOCK_RED = "lock_red.png"
LOCK_YELLOW = "lock_yellow.png"

class LockTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\lock")
    def __init__(self, state: str = LOCK_BLUE, color: str = None):
        super().__init__(state, color)


from utils.spriteLoader import Tile
from pathlib import Path

WINDOW = "window.png"

class WindowTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\window")
    def __init__(self, state: str = WINDOW, color: str = None):
        super().__init__(state, color)


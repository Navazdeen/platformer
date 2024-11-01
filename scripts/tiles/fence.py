from utils.spriteLoader import Tile
from pathlib import Path

FENCE = "fence.png"
FENCEBROKEN = "fenceBroken.png"

class FenceTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\fence")
    def __init__(self, state: str = FENCE, color: str = None):
        super().__init__(state, color)


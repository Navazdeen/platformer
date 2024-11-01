from utils.spriteLoader import Tile
from pathlib import Path

ROCKHILLLEFT = "rockHillLeft.png"
ROCKHILLRIGHT = "rockHillRight.png"

class RockTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\rock")
    def __init__(self, state: str = ROCKHILLLEFT, color: str = None):
        super().__init__(state, color)


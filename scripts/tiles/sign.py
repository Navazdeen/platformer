from utils.spriteLoader import Tile
from pathlib import Path

SIGN = "sign.png"
SIGNEXIT = "signExit.png"
SIGNLEFT = "signLeft.png"
SIGNRIGHT = "signRight.png"

class SignTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\sign")
    def __init__(self, state: str = SIGN, color: str = None):
        super().__init__(state, color)


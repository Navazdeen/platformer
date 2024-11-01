from utils.spriteLoader import Tile
from pathlib import Path

CASTLE = "castle.png"
CASTLECENTER = "castleCenter.png"
CASTLECENTER_ROUNDED = "castleCenter_rounded.png"
CASTLECLIFFLEFT = "castleCliffLeft.png"
CASTLECLIFFLEFTALT = "castleCliffLeftAlt.png"
CASTLECLIFFRIGHT = "castleCliffRight.png"
CASTLECLIFFRIGHTALT = "castleCliffRightAlt.png"
CASTLEHALF = "castleHalf.png"
CASTLEHALFLEFT = "castleHalfLeft.png"
CASTLEHALFMID = "castleHalfMid.png"
CASTLEHALFRIGHT = "castleHalfRight.png"
CASTLEHILLLEFT = "castleHillLeft.png"
CASTLEHILLLEFT2 = "castleHillLeft2.png"
CASTLEHILLRIGHT = "castleHillRight.png"
CASTLEHILLRIGHT2 = "castleHillRight2.png"
CASTLELEDGELEFT = "castleLedgeLeft.png"
CASTLELEDGERIGHT = "castleLedgeRight.png"
CASTLELEFT = "castleLeft.png"
CASTLEMID = "castleMid.png"
CASTLERIGHT = "castleRight.png"

class CastleTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\castle")
    def __init__(self, state: str = CASTLE, color: str = None):
        super().__init__(state, color)


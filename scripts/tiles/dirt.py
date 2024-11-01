from utils.spriteLoader import Tile
from pathlib import Path

DIRT = "dirt.png"
DIRTCENTER = "dirtCenter.png"
DIRTCENTER_ROUNDED = "dirtCenter_rounded.png"
DIRTCLIFFLEFT = "dirtCliffLeft.png"
DIRTCLIFFLEFTALT = "dirtCliffLeftAlt.png"
DIRTCLIFFRIGHT = "dirtCliffRight.png"
DIRTCLIFFRIGHTALT = "dirtCliffRightAlt.png"
DIRTHALF = "dirtHalf.png"
DIRTHALFLEFT = "dirtHalfLeft.png"
DIRTHALFMID = "dirtHalfMid.png"
DIRTHALFRIGHT = "dirtHalfRight.png"
DIRTHILLLEFT = "dirtHillLeft.png"
DIRTHILLLEFT2 = "dirtHillLeft2.png"
DIRTHILLRIGHT = "dirtHillRight.png"
DIRTHILLRIGHT2 = "dirtHillRight2.png"
DIRTLEDGELEFT = "dirtLedgeLeft.png"
DIRTLEDGERIGHT = "dirtLedgeRight.png"
DIRTLEFT = "dirtLeft.png"
DIRTMID = "dirtMid.png"
DIRTRIGHT = "dirtRight.png"

class DirtTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\dirt")
    def __init__(self, state: str = DIRT, color: str = None):
        super().__init__(state, color)


from utils.spriteLoader import Tile
from pathlib import Path

SAND = "sand.png"
SANDCENTER = "sandCenter.png"
SANDCENTER_ROUNDED = "sandCenter_rounded.png"
SANDCLIFFLEFT = "sandCliffLeft.png"
SANDCLIFFLEFTALT = "sandCliffLeftAlt.png"
SANDCLIFFRIGHT = "sandCliffRight.png"
SANDCLIFFRIGHTALT = "sandCliffRightAlt.png"
SANDHALF = "sandHalf.png"
SANDHALFLEFT = "sandHalfLeft.png"
SANDHALFMID = "sandHalfMid.png"
SANDHALFRIGHT = "sandHalfRight.png"
SANDHILLLEFT = "sandHillLeft.png"
SANDHILLLEFT2 = "sandHillLeft2.png"
SANDHILLRIGHT = "sandHillRight.png"
SANDHILLRIGHT2 = "sandHillRight2.png"
SANDLEDGELEFT = "sandLedgeLeft.png"
SANDLEDGERIGHT = "sandLedgeRight.png"
SANDLEFT = "sandLeft.png"
SANDMID = "sandMid.png"
SANDRIGHT = "sandRight.png"

class SandTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\sand")
    def __init__(self, state: str = SAND, color: str = None):
        super().__init__(state, color)


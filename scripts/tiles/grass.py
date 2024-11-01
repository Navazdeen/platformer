from utils.spriteLoader import Tile
from pathlib import Path

GRASS = "grass.png"
GRASSCENTER = "grassCenter.png"
GRASSCENTER_ROUNDED = "grassCenter_rounded.png"
GRASSCLIFFLEFT = "grassCliffLeft.png"
GRASSCLIFFLEFTALT = "grassCliffLeftAlt.png"
GRASSCLIFFRIGHT = "grassCliffRight.png"
GRASSCLIFFRIGHTALT = "grassCliffRightAlt.png"
GRASSHALF = "grassHalf.png"
GRASSHALFLEFT = "grassHalfLeft.png"
GRASSHALFMID = "grassHalfMid.png"
GRASSHALFRIGHT = "grassHalfRight.png"
GRASSHILLLEFT = "grassHillLeft.png"
GRASSHILLLEFT2 = "grassHillLeft2.png"
GRASSHILLRIGHT = "grassHillRight.png"
GRASSHILLRIGHT2 = "grassHillRight2.png"
GRASSLEDGELEFT = "grassLedgeLeft.png"
GRASSLEDGERIGHT = "grassLedgeRight.png"
GRASSLEFT = "grassLeft.png"
GRASSMID = "grassMid.png"
GRASSRIGHT = "grassRight.png"

class GrassTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\grass")
    def __init__(self, state: str = GRASS, color: str = None):
        super().__init__(state, color)


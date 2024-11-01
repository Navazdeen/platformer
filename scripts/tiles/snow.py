from utils.spriteLoader import Tile
from pathlib import Path

SNOW = "snow.png"
SNOWCENTER = "snowCenter.png"
SNOWCENTER_ROUNDED = "snowCenter_rounded.png"
SNOWCLIFFLEFT = "snowCliffLeft.png"
SNOWCLIFFLEFTALT = "snowCliffLeftAlt.png"
SNOWCLIFFRIGHT = "snowCliffRight.png"
SNOWCLIFFRIGHTALT = "snowCliffRightAlt.png"
SNOWHALF = "snowHalf.png"
SNOWHALFLEFT = "snowHalfLeft.png"
SNOWHALFMID = "snowHalfMid.png"
SNOWHALFRIGHT = "snowHalfRight.png"
SNOWHILLLEFT = "snowHillLeft.png"
SNOWHILLLEFT2 = "snowHillLeft2.png"
SNOWHILLRIGHT = "snowHillRight.png"
SNOWHILLRIGHT2 = "snowHillRight2.png"
SNOWLEDGELEFT = "snowLedgeLeft.png"
SNOWLEDGERIGHT = "snowLedgeRight.png"
SNOWLEFT = "snowLeft.png"
SNOWMID = "snowMid.png"
SNOWRIGHT = "snowRight.png"

class SnowTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\snow")
    def __init__(self, state: str = SNOW, color: str = None):
        super().__init__(state, color)


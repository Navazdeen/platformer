from utils.spriteLoader import Tile
from pathlib import Path

STONE = "stone.png"
STONECENTER = "stoneCenter.png"
STONECENTER_ROUNDED = "stoneCenter_rounded.png"
STONECLIFFLEFT = "stoneCliffLeft.png"
STONECLIFFLEFTALT = "stoneCliffLeftAlt.png"
STONECLIFFRIGHT = "stoneCliffRight.png"
STONECLIFFRIGHTALT = "stoneCliffRightAlt.png"
STONEHALF = "stoneHalf.png"
STONEHALFLEFT = "stoneHalfLeft.png"
STONEHALFMID = "stoneHalfMid.png"
STONEHALFRIGHT = "stoneHalfRight.png"
STONEHILLLEFT2 = "stoneHillLeft2.png"
STONEHILLRIGHT2 = "stoneHillRight2.png"
STONELEDGELEFT = "stoneLedgeLeft.png"
STONELEDGERIGHT = "stoneLedgeRight.png"
STONELEFT = "stoneLeft.png"
STONEMID = "stoneMid.png"
STONERIGHT = "stoneRight.png"
STONEWALL = "stoneWall.png"

class StoneTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\stone")
    def __init__(self, state: str = STONE, color: str = None):
        super().__init__(state, color)


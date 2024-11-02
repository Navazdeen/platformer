from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class DirtTile(Tile):
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
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\dirt")
    def __init__(self, game:"Game", state: str = DIRT, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


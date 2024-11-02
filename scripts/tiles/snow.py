from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class SnowTile(Tile):
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
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\snow")
    def __init__(self, game:"Game", state: str = SNOW, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


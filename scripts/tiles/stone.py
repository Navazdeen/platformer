from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class StoneTile(Tile):
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
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\stone")
    def __init__(self, game:"Game", state: str = STONE, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


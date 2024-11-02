from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class CastleTile(Tile):
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
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\castle")
    def __init__(self, game:"Game", state: str = CASTLE, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


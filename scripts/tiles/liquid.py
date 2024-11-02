from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class LiquidTile(Tile):
    LIQUIDLAVA = "liquidLava.png"
    LIQUIDLAVATOP = "liquidLavaTop.png"
    LIQUIDLAVATOP_MID = "liquidLavaTop_mid.png"
    LIQUIDWATER = "liquidWater.png"
    LIQUIDWATERTOP = "liquidWaterTop.png"
    LIQUIDWATERTOP_MID = "liquidWaterTop_mid.png"
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\liquid")
    def __init__(self, game:"Game", state: str = LIQUIDLAVA, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


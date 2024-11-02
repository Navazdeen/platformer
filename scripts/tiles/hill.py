from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class HillTile(Tile):
    HILL_LARGE = "hill_large.png"
    HILL_LARGEALT = "hill_largeAlt.png"
    HILL_SMALL = "hill_small.png"
    HILL_SMALLALT = "hill_smallAlt.png"
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\hill")
    def __init__(self, game:"Game", state: str = HILL_LARGE, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


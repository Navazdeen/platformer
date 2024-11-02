from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class LockTile(Tile):
    LOCK_BLUE = "lock_blue.png"
    LOCK_GREEN = "lock_green.png"
    LOCK_RED = "lock_red.png"
    LOCK_YELLOW = "lock_yellow.png"
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\lock")
    def __init__(self, game:"Game", state: str = LOCK_BLUE, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


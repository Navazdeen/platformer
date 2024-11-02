from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class RockTile(Tile):
    ROCKHILLLEFT = "rockHillLeft.png"
    ROCKHILLRIGHT = "rockHillRight.png"
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\rock")
    def __init__(self, game:"Game", state: str = ROCKHILLLEFT, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


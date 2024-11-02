from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class DoorTile(Tile):
    DOOR_CLOSEDMID = "door_closedMid.png"
    DOOR_CLOSEDTOP = "door_closedTop.png"
    DOOR_OPENMID = "door_openMid.png"
    DOOR_OPENTOP = "door_openTop.png"
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\door")
    def __init__(self, game:"Game", state: str = DOOR_CLOSEDMID, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)


from utils.spriteLoader import Tile
from pathlib import Path

DOOR_CLOSEDMID = "door_closedMid.png"
DOOR_CLOSEDTOP = "door_closedTop.png"
DOOR_OPENMID = "door_openMid.png"
DOOR_OPENTOP = "door_openTop.png"

class DoorTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\door")
    def __init__(self, state: str = DOOR_CLOSEDMID, color: str = None):
        super().__init__(state, color)


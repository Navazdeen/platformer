from utils.spriteLoader import Tile
from pathlib import Path

BRIDGE = "bridge.png"
BRIDGELOGS = "bridgeLogs.png"

class BridgeTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\bridge")
    def __init__(self, state: str = BRIDGE, color: str = None):
        super().__init__(state, color)


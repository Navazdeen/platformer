from utils.spriteLoader import Tile
from pathlib import Path

TORCH = "torch.png"

class TorchTile(Tile):
    tilepath:Path = Path(r"D:\programs\platform_game\Assets\tiles\parsed\torch")
    def __init__(self, state: str = TORCH, color: str = None):
        super().__init__(state, color)


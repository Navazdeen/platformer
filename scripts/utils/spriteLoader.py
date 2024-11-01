import pygame
from pygame import Vector2
from pathlib import Path
from typing import List, Dict
from collections import defaultdict
from .templates import Tile


class TileCollection:
    def __init__(self, tile_path: str, color: str = None):
        self.tile_path = Path(tile_path)
        self.tile_color = color
        self.tile_collection: Dict[str, List[Tile]] = defaultdict(list)
        self._create_tile()

    def _create_tile(self, path: Path = None):
        tile_path = path or self.tile_path
        for tile in tile_path.iterdir():
            if tile.is_dir():
                self._create_tile(tile)
            elif tile.is_file():
                _tile = Tile(tile, self.tile_color)
                self.tile_collection[tile.parent.name].append(_tile)

    def drawCollection(self, surface: pygame.Surface, collection_name: str, position: Vector2):
        for tile in self.tile_collection[collection_name]:
            tile.__move(position)
            tile.draw(surface)
            position += Vector2(tile.size.x, 0)

    def draw(self, surface):
        pass

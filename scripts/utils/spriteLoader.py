import pygame
from pygame import Vector2
from pathlib import Path
from typing import List, Dict, TYPE_CHECKING
from collections import defaultdict
from .templates import Tile
from tiles import box

if TYPE_CHECKING:
    from scripts.player import Player
    from main import Game


class World:
    def __init__(self, game: "Game") -> None:
        self.tiles: List[Tile] = []
        self.interactables: Dict[str, List[Tile]] = defaultdict(list)
        self.game = game

    def add_tile(self, tile: Tile | List[Tile]):
        if isinstance(tile, list):
            self.tiles.extend(tile)
            return
        self.tiles.append(tile)

    def track(self, player: "Player"):
        self._setPlayerOffset(player=player)
        for tile in self.tiles:
            if player.rect.colliderect(tile.rect):
                # Vertical Collision (y-direction) - prioritize y-axis first
                if (
                    player.velocity.y > 0
                    and player.rect.bottom <= tile.rect.bottom
                    and player.rect.bottom > tile.rect.top
                ):
                    player.rect.bottom = tile.rect.top
                    player.velocity.y = 0  # Stop downward movement
                    player.is_grounded = True  # Player is on the ground
                elif (
                    player.velocity.y < 0
                    and player.rect.top >= tile.rect.top
                    and player.rect.top < tile.rect.bottom
                ):
                    player.rect.top = tile.rect.bottom
                    player.velocity.y = 0

                # Horizontal Collision (x-direction) - only if not grounded on top of the tile
                if not player.is_grounded:
                    if (
                        player.velocity.x > 0
                        and player.rect.right > tile.rect.left
                        and player.rect.left < tile.rect.right
                    ):
                        player.rect.right = tile.rect.left
                        player.velocity.x = 0  # Stop horizontal movement to the right
                    elif (
                        player.velocity.x < 0
                        and player.rect.left < tile.rect.right
                        and player.rect.right > tile.rect.left
                    ):
                        player.rect.left = tile.rect.right
                        player.velocity.x = 0  # Stop horizontal movement to the left

    def draw(self, screen: pygame.Surface):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

    def move(self, offset: Vector2):
        for tile in self.tiles:
            tile.rect.topleft += offset * self.game.delta_time

    def _setPlayerOffset(self, player: "Player"):
        width, _ = self.game.WIN_SIZE
        _offset = 200
        if player.rect.centerx >= (width // 2 + _offset) and player.velocity.x > 0:
            self.move(Vector2(-player.velocity.x, 0))
            player.velocity.x = 0
        elif player.rect.centerx <= width // 2 - _offset and player.velocity.x < 0:
            self.move(Vector2(-player.velocity.x, 0))
            player.velocity.x = 0

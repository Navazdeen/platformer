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
        self.timer: List[Dict[str, float | callable]] = []

    def add_tile(self, tile: Tile | List[Tile]):
        if isinstance(tile, list):
            self.tiles.extend(tile)
            return
        self.tiles.append(tile)

    def remove_tile(self, tile: Tile):
        if tile in self.tiles:
            self.tiles.remove(tile)
            return

    def destroy_tile(self, tile: Tile, timer: float = 0, destroy_func: callable = None):
        if timer:
            self.timer.append(
                dict(
                    timer=timer,
                    func=lambda: destroy_func or self.remove_tile(tile=tile),
                ),
            )
        else:
            self.remove_tile(tile=tile)

    def update_timer(self):
        for timer in self.timer:
            timer["timer"] -= self.game.delta_time / 100
            if timer["timer"] <= 0:
                timer["func"]()

    def track(self, player: "Player"):
        self._setPlayerOffset(player=player)
        for tile in self.tiles:
            if player.rect.colliderect(tile.rect):
                tile.collide(other=player)
        self.update_timer()

    def draw(self, screen: pygame.Surface):
        for tile in self.tiles:
            # screen.blit(tile.image, tile.rect)
            tile.draw(surface=screen)

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

from typing import Dict, List
from utils.templates import Tile
from pygame.math import Vector2
import pygame
from pathlib import Path


class Player(Tile):
    tilepath: Path = None
    gravity = Vector2(0, 0)
    friction = Vector2(0.05, 0.5)
    animation_speed = 100

    def __init__(self, state: str | List[str], color: str = None):
        self.__animated = False
        self.__name = self.tilepath.name
        self.velocity = Vector2(0, 0)
        self.__state = state
        self.last_update = pygame.time.get_ticks()
        self.__update_state()
        if color:
            self.__image.fill(color)

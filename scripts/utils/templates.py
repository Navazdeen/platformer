from pathlib import Path
from typing import List
import pygame
from pygame import Vector2
from itertools import cycle


class Tile(pygame.sprite.Sprite):
    tilepath: Path = None
    gravity = Vector2(0, 3)
    friction = Vector2(0.85, 0.05)
    animation_speed = 100

    def __init__(self, state: str | List[str], color: str = None):
        super().__init__()
        self.__animated = False
        self.__name = self.tilepath.name
        self.velocity = Vector2(0, 0)
        self.__state = state
        self.last_update = pygame.time.get_ticks()
        self.__update_state()
        if color:
            self.__image.fill(color)

    def __update_state(self):
        prev_pos = self.position if hasattr(self, "__rect") else Vector2(0, 0)
        if isinstance(self.__state, list):
            self.__animated = True
            statecycles = [
                pygame.image.load(self.tilepath.joinpath(state)).convert_alpha()
                for state in self.__state
            ]
            self.__statelabel = cycle(self.__state)
            self.__stateimage = cycle(statecycles)
            self.__image = statecycles[0]
            self.__state = self.__state[0]
        else:
            self.__image = pygame.image.load(
                self.tilepath.joinpath(self.__state)
            ).convert_alpha()
        self.__rect = self.__image.get_rect()
        self.__rect.x = prev_pos.x
        self.__rect.y = prev_pos.y

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str | List[str]):
        self.__state = state
        self.__update_state()

    def move(self, velocity: Vector2):
        self.velocity += velocity + self.gravity

    @property
    def size(self):
        return Vector2(self.__rect.size)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return Vector2(self.__rect.x, self.__rect.y)

    def update(self):
        # Apply velocity and friction
        current_time = pygame.time.get_ticks()
        if self.__animated and current_time - self.last_update >= self.animation_speed:
            self.last_update = current_time
            self.__image = next(self.__stateimage)
        self.__rect = self.__rect.move(self.velocity)
        self.velocity = self.velocity.elementwise() * (self.friction)  # Apply friction
        if self.velocity.magnitude() < 0.1:  # Stop small velocities
            self.velocity = Vector2(0, 0)

    def draw(self, surface: pygame.Surface):
        # Draw the tile without applying movement
        surface.blit(self.__image, self.rect)
        self.update()


tile_template = """from utils.spriteLoader import Tile
from pathlib import Path

{states}

class {name}Tile(Tile):
    tilepath:Path = Path(r"{tilepath}")
    def __init__(self, state: str = {_default_state}, color: str = None):
        super().__init__(state, color)

"""


if __name__ == "__main__":
    _HERE = Path(__file__).parent
    # Example usage
    # Replace with the actual path to the sprite sheet image
    sprite_sheet_path = _HERE.joinpath("../../Assets/tiles/parsed/").resolve()

    for path in sprite_sheet_path.iterdir():
        if path.is_dir():
            _file = _HERE.parent.joinpath("tiles", f"{path.name}.py")
            _file.touch(exist_ok=True)
            with open(_file, "w") as f:
                file_list = [file for file in path.iterdir() if file.is_file()]
                states = "\n".join(
                    [f'{file.stem.upper()} = "{str(file.name)}"' for file in file_list]
                )
                f.write(
                    tile_template.format(
                        states=states,
                        name=path.name.capitalize(),
                        tilepath=path,
                        _default_state=file_list[0].stem.upper(),
                    )
                )

from pathlib import Path
from typing import List, TYPE_CHECKING
import pygame
from pygame import Vector2
from itertools import cycle

if TYPE_CHECKING:
    from main import Game
    from player import Player


class Tile(pygame.sprite.Sprite):
    tilepath: Path = None
    gravity = Vector2(0, 0)
    friction = Vector2(0.5, 1)
    animation_speed = 10

    def __init__(
        self,
        state: str | List[str],
        game: "Game",
        initial_position: Vector2 = Vector2(0, 0),
        color: str = None,
    ):
        super().__init__()
        self.animated = False
        self.__name = self.tilepath.name
        self.velocity = Vector2(0, 0)
        self.__state = state
        self._stateimgs: List[pygame.Surface] = []
        self.__update_state(initial_position)
        self.last_updated = 0
        self.__flipped = (False, False)
        self.game = game
        if color:
            self.__image.fill(color)

    def __update_state(self, position: Vector2 = None):
        prev_pos = position or (
            self.position if getattr(self, "rect", None) else Vector2(0, 0)
        )
        self.__flipped = (False, False)
        if isinstance(self.__state, list):
            self.animated = True
            self._stateimgs = [
                pygame.image.load(self.tilepath.joinpath(state)).convert_alpha()
                for state in self.__state
            ]
            self.__stateimage = cycle(self._stateimgs)
            self.__image = self._stateimgs[0]
        else:
            self.__image = pygame.image.load(
                self.tilepath.joinpath(self.__state)
            ).convert_alpha()
            self.animated = False
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
    def flipped(self):
        return self.__flipped

    def flipImage(self, flip_x: bool = False, flip_y: bool = False):
        self.__flipped = (
            not self.flipped[0] and flip_x,
            not self.flipped[1] and flip_x,
        )
        if self.animated:
            self.__stateimage = cycle(
                [
                    pygame.transform.flip(image, flip_x, flip_y)
                    for image in self._stateimgs
                ]
            )
        else:
            self.__image = pygame.transform.flip(self.__image, flip_x, flip_y)

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return Vector2(self.__rect.x, self.__rect.y)

    def update(self):
        # Apply velocity and friction
        self.last_updated += self.game.delta_time
        if self.animated and self.last_updated >= self.animation_speed:
            self.__image = next(self.__stateimage)
            self.last_updated = 0

        # TODO: apply velocity by calculating delta time
        # Update the position based on velocity and delta time
        self.__rect.x += self.velocity.x * self.game.delta_time
        self.__rect.y += (self.velocity.y) * self.game.delta_time

        self.velocity.y = min(
            self.gravity.y, (self.velocity.y + self.gravity.y * self.game.delta_time)
        )

    def update_player(self, player: "Player"):
        if (
            player.velocity.y > 0
            and player.rect.bottom <= self.rect.bottom
            and player.rect.bottom > self.rect.top
        ):
            player.rect.bottom = self.rect.top
            player.velocity.y = 0  # Stop downward movement
            player.is_grounded = True  # Player is on the ground
        elif (
            player.velocity.y < 0
            and player.rect.top >= self.rect.top
            and player.rect.top < self.rect.bottom
        ):
            player.rect.top = self.rect.bottom
            player.velocity.y = 0

        # Horizontal Collision (x-direction) - only if not grounded on top of the self
        if not player.is_grounded:
            if (
                player.velocity.x > 0
                and player.rect.right > self.rect.left
                and player.rect.left < self.rect.right
            ):
                player.rect.right = self.rect.left
                player.velocity.x = 0  # Stop horizontal movement to the right
            elif (
                player.velocity.x < 0
                and player.rect.left < self.rect.right
                and player.rect.right > self.rect.left
            ):
                player.rect.left = self.rect.right
                player.velocity.x = 0  # Stop horizontal movement to the left

    def collide(self, other: "Tile"):
        # Check for collision with another tile
        # Vertical Collision (y-direction) - prioritize y-axis first

        if isinstance(other, type(self.game.player)):
            self.update_player(other)

    def draw(self, surface: pygame.Surface):
        # Draw the tile without applying movement
        surface.blit(self.__image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)
        self.update()


tile_template = """from utils.spriteLoader import Tile
from pathlib import Path
from pygame import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class {name}Tile(Tile):
    {states}
    tilepath:Path = Path(r"{tilepath}")
    def __init__(self, game:"Game", state: str = {_default_state}, initial_position: Vector2 = Vector2(0, 0), color: str = None):
        super().__init__(state, game, initial_position, color)

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
                states = "\n    ".join(
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

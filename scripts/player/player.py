import pygame
from pygame.math import Vector2
from pathlib import Path
from utils.templates import Tile
from typing import List, Dict, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Player(Tile):
    PLAYER_STATE: Dict[str, List[str] | str] = {
        "idle": "p1_stand.png",
        "running": [f"p1_walk{i:02d}.png" for i in range(1, 12)],
        "jump": "p1_jump.png",
        "hurt": "p1_hurt.png",
        "front": "p1_front.png",
    }
    tilepath: Path = Path(__file__).parent.parent.parent.joinpath(
        *("Assets/player/parsed/p1".split("/"))
    )
    gravity = Vector2(0, 2)
    friction = Vector2(0.75, 0.02)
    animation_speed = 1

    def __init__(
        self,
        game: "Game",
        initial_state: Literal["idle", "front"] = "front",
        initial_position: Vector2 = Vector2(200, 200),
        color: str = None,
    ):
        # Initialize Tile
        super().__init__(
            state=self.PLAYER_STATE[initial_state],
            game=game,
            initial_position=initial_position,
            color=color,
        )
        self.current_state = initial_state
        self.jump_strength = -25
        self.speed = 3
        self.direction = "right"
        self.is_grounded = False

    def handle_input(self):
        # Determine player input and set states
        keys = pygame.key.get_pressed()

        # Movement flags
        moving_left = keys[pygame.K_LEFT]
        moving_right = keys[pygame.K_RIGHT]
        jump = keys[pygame.K_SPACE]

        # Update movement based on input
        if moving_left and moving_right:
            self.set_state("idle")
        elif moving_left:
            self.velocity.x = -self.speed
            self.set_state("running")
            self.direction = "left"
            if not self.flipped[0]:
                self.flipImage(flip_x=True)
        elif moving_right:
            self.velocity.x = self.speed
            self.set_state("running")
            self.direction = "right"
            if self.flipped[0]:
                self.flipImage(flip_x=True)
        else:
            self.velocity.x = 0  # Stop horizontal movement if no keys pressed
            self.set_state("idle")
            if self.direction == "left" and not self.flipped[0]:
                self.flipImage(flip_x=True)
            elif self.direction == "right" and self.flipped[0]:
                self.flipImage(flip_x=True)

        # Jumping
        if jump and self.is_grounded:
            self.velocity.y = self.jump_strength
            if self.direction == "left":
                self.flipImage(flip_x=True)
            self.set_state("jump")
            self.is_grounded = False
        if not self.is_grounded:
            self.set_state("jump")
            if self.direction == "left":
                self.flipImage(flip_x=True)

    def set_state(self, state: str):
        # Update the state and reset the animation cycle if it changes
        if self.current_state != state:
            self.current_state = state
            self.state = self.PLAYER_STATE[state]  # Sets the new state images

    def update(self):
        # Apply movement
        super().update()
        # Handle input and update position
        self.handle_input()

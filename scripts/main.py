import pygame
from pygame import Vector2
from tiles import box, grass
from player import Player
from utils.spriteLoader import World
from pathlib import Path


class Game:
    BG_COLOR = (0, 0, 0)
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    WIN_SIZE = (WIDTH, HEIGHT)
    _Here = Path(__file__).parent

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.WIN_SIZE)
        pygame.display.set_caption("Mystic Mountain")
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.running = True
        self.delta_time = 0
        self.setup()

    def setup(self):
        self.player = Player(initial_state="idle", game=self)
        self.world = World(game=self)
        self.world.add_tile(
            [
                box.BoxTile(
                    state=box.BoxTile.BOX,
                    game=self,
                    initial_position=Vector2(i * 70, self.HEIGHT - 70),
                )
                for i in range(100)
            ]
            + [
                grass.GrassTile(
                    state=grass.GrassTile.GRASS,
                    game=self,
                    initial_position=Vector2(i * 70 + 200, self.HEIGHT - 70 * 4),
                )
                for i in range(100)
            ]
        )

    def _handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        pass

    def _draw(self):
        pass

    def run(self):
        while self.running:
            self.delta_time = self.clock.tick(self.FPS) / 10
            self._handle_event()
            self.screen.fill(self.BG_COLOR)
            self.player.draw(self.screen)
            self.world.track(self.player)
            self.world.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

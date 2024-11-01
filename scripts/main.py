import pygame
from pygame import Vector2
from tiles import box
from pathlib import Path


class Game:
    BG_COLOR = (0, 0, 0)
    FPS = 60
    WIN_SIZE = (800, 600)
    _Here = Path(__file__).parent

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.WIN_SIZE)
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.box = box.BoxTile(state=[box.BOX, box.BOXALT, box.BOXCOIN, box.BOXCOINALT])
        self.setup()

    def setup(self):
        pass

    def _handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        move_vector = Vector2(0, 0)  # Start with no movement
        keys = pygame.key.get_pressed()  # Check the current state of all keys
        if keys[pygame.K_LEFT]:
            move_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            move_vector.x += 1
        if keys[pygame.K_UP]:
            move_vector.y -= 1
        if keys[pygame.K_DOWN]:
            move_vector.y += 1
        if keys[pygame.K_SPACE]:
            move_vector.y -= 10

        self.box.move(move_vector)

    def _update(self):
        pass

    def _draw(self):
        pass

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self._handle_event()
            self.screen.fill(self.BG_COLOR)
            self.box.draw(self.screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

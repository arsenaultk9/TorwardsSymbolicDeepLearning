from game import player_collision_pool
import pygame
from pygame.locals import *

import game.levels.level_mixed as level_mixed
from game.level_generator import LevelGenerator
from game.level import Level

import game.constants as game_constants
from game.object_pool import ObjectPool

FPS = 9
FramePerSec = pygame.time.Clock()


class Game:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.weight, self.height = game_constants.game_width, game_constants.game_height

        level_content = LevelGenerator(True).generate_level()
        self.level = Level(level_content)
        # self.level = Level(level_mixed.level)

    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.level.instantiate()
        self.level.player_surroundings()
        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        ObjectPool.update()

    def on_render(self):
        self.display_surface.fill((255, 255, 255))
        ObjectPool.draw(self.display_surface)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):
            FramePerSec.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

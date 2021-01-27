import pygame
from pygame.locals import *

from game.player import Player
import game.constants as game_constants
import game.object_pool as object_pool

FPS = 9
FramePerSec = pygame.time.Clock()
 
class Game:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.weight, self.height = game_constants.game_width, game_constants.game_height
        
        self.mainPlayer = Player(game_constants.tile_size * 10, game_constants.tile_size * 10)
 
    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        object_pool.update()

    def on_render(self):
        self.display_surface.fill((0, 0, 0))
        object_pool.draw(self.display_surface)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            FramePerSec.tick(FPS)
            pygame.display.update()

            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()
import pygame

from dino_runner.utils.constants import CLOUD, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        self.screen.blit(CLOUD, (5, 100))
        self.screen.blit(CLOUD, (30, 150))
        self.screen.blit(CLOUD, (120, 150))
        self.screen.blit(CLOUD, (140, 120))
        self.screen.blit(CLOUD, (400, 120))
        self.screen.blit(CLOUD, (430, 150))
        self.screen.blit(CLOUD, (500, 100))
        self.screen.blit(CLOUD, (545, 150))
        self.screen.blit(CLOUD, (810, 110))
        self.screen.blit(CLOUD, (850, 140))
        self.screen.blit(CLOUD, (910, 90))
        self.screen.blit(CLOUD, (970, 150))
        
        


        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

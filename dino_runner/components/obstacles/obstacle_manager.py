import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            x_position = 800  # Posição horizontal do cacto
            y_position = game.player.dino_rect.y + 30  # Posição vertical do cacto
            
            obstacles_type = random.choice([SMALL_CACTUS, LARGE_CACTUS, BIRD])
            obstacle_pos = x_position, y_position
            self.obstacles.append(Cactus(random.choice(obstacles_type)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if self.check_collision(game.player, obstacle):
                pygame.time.delay(500)
                game.playing = False
    
    def check_collision(self, player, obstacle):
        player_rect = pygame.Rect(player.dino_rect.x, player.dino_rect.y, player.dino_rect.width // 1.2, player.dino_rect.height)
        obstacle_rect = pygame.Rect(obstacle.rect.x, obstacle.rect.y + obstacle.rect.height // 2, obstacle.rect.width // 2, obstacle.rect.height // 2)
        
        return player_rect.colliderect(obstacle_rect)
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
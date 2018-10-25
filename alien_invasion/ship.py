import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_settings):
        super(Ship,self).__init__()
        
        self.screen=screen
        
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.ai_settings=ai_settings
        self.centerx=float(self.rect.centerx)
        
        self.moving_right=False
        self.moving_left=False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        self.center = self.screen_rect.centerx
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.centerx

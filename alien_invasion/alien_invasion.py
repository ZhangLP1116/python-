import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(screen,ai_settings)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    play_button = Button(ai_settings,screen,"Play")
    while True:
        
        gf.check_event(ship,bullets,ai_settings,screen,stats,play_button,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets,ai_settings,screen,ship,sb,stats)
            gf.update_alien(ai_settings,aliens,ship,bullets,screen,stats,sb)
        gf.update_screen(screen,ship,ai_settings,bullets,aliens,stats,play_button,sb)

run_game()

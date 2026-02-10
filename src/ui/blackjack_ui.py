import logging.config
from src.config import Config
import time
import pygame

from .button import Button

class blackjack_ui:
    def __init__(self, game, config):
        self.game = game
        self.config = config
        self.screen = game.screen

        self.FONT = pygame.font.SysFont("arial", 24)
        self.BIG  = pygame.font.SysFont("arial", 40)
        self.HUGE = pygame.font.SysFont("arial", 64)

        x, y, w, h = config.hit_btn
        self.hit_btn = Button("Hit", x, y, w, h, self.FONT)

        x, y, w, h = config.stand_btn
        self.stand_btn = Button("Stand", x, y, w, h, self.FONT)

        self.cache = {}


    def load_card(self, path):
        if path not in self.cache:
            img = pygame.image.load(path).convert_alpha()
            self.cache[path] = pygame.transform.scale(img, (80,120))

        return self.cache[path]

    def draw_hand(self, cards, y, label):
        if label == "Dealer":
            self.draw_text(label, self.config.card_start_x + 150, y - 50, big=True)

        elif label == "Player":
            self.draw_text(label, self.config.card_start_x + 150, y + 120, big=True)

        x = self.config.card_start_x
        for c in cards:
            img = self.load_card(c.rank_img_path)
            self.screen.blit(img, (x, y))
            x += self.config.card_spacing

    def draw_text(self, text, x, y, big=False, huge=False):
        f = self.HUGE if huge else self.BIG if big else self.FONT
        img = f.render(text, True, (255,255,255))
        self.screen.blit(img, (x,y))
        
    def draw_game(self):
        self.screen.fill(self.game.bg)
        pygame.draw.rect(self.screen, (0,90,0), self.config.dealer_box, border_radius=20)
        pygame.draw.rect(self.screen, (0,90,0), self.config.player_box, border_radius=20)

        self.draw_hand(self.game.dealer.hand.cards, self.config.dealer_y, "Dealer")
        self.draw_hand(self.game.player.hand.cards, self.config.player_y, "Player")

        self.draw_text(f"Dealer: {self.game.dealer.hand.highest_value}", 550, 250)
        self.draw_text(f"Player: {self.game.player.hand.highest_value}", 550, 355)

        self.draw_text(self.game.message, 550, 10, big=True)
        self.draw_text(
            f"Player {self.game.player_score} - Dealer {self.game.dealer_score}", 520, 300
        )

        self.hit_btn.draw(self.screen)
        self.stand_btn.draw(self.screen)

    def draw_end_screen(self):
        self.screen.fill(self.game.bg)

        self.draw_text(self.game.message, 430, 220, huge=True)
        self.draw_text(
            f"Player {self.game.player_score} - Dealer {self.game.dealer_score}", 420, 300, big=True
        )

        self.draw_text("Press R to Play Again | Q to Quit", 360, 380)

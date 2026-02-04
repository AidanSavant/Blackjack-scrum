from .config import Config

from .models.deck import Deck
from .models.player import Player
from .models.dealer import Dealer

from .ui.blackjack_ui import blackjack_ui

import pygame
from pygame import Surface, time

class Game:
    def __init__(self, config: Config) -> None:
        self._init_pygame(config.fps, config.width, config.height, config.background_rgb)

        self.deck = Deck()
        self._init_players()

        self.ui = blackjack_ui(self)

        # Delays the time for both dealer and end screen
        self.ui_state = "PLAYER_TURN"
        self.last_dealer_action = 0
        self.end_screen_time = 0

    def _init_pygame(self, fps, width, height, background_rgb) -> None:
        pygame.init()
        pygame.display.set_caption("Blackjack game (waterfall implementation)")

        self.fps: int = fps
        self.clock: time.Clock = pygame.time.Clock()

        self.bg = background_rgb
        self.screen: Surface = pygame.display.set_mode((width, height))
        self.screen.fill(background_rgb)

    def _init_players(self) -> None:
        self.dealer: Dealer = Dealer(self.deck)
        self.player: Player = Player(self.deck)

    # Round Logic
    def reset_round(self):
        self.deck.shuffle_deck()
        self._init_players()
        self.message = "Your Turn"
        self.ui_state = "PLAYER_TURN"

    def end_round(self):
        p = self.player.hand.highest_value
        d = self.dealer.hand.highest_value

        if d > 21 or p > d:
            self.message = "YOU WON!"
            self.player_score += 1
        else:
            self.message = "YOU LOST!"
            self.dealer_score += 1

        self.ui_state = "END"

    def start_game_loop(self) -> None:
        running = True

        # game state
        self.message = "Your Turn"
        self.player_score = 0
        self.dealer_score = 0
        self.ui_state = "PLAYER_TURN"  # PLAYER_TURN, DEALER, END

        while running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if self.ui_state == "PLAYER_TURN":
                        if self.ui.hit_btn.clicked(pos):
                            self.player.hit(self.deck)

                            if self.player.hand.is_bust:
                                self.message = "BUSTED!"
                                self.dealer_score += 1
                                self.ui_state = "END"

                            elif self.player.hand.is_blackjack:
                                self.message = "BLACKJACK!"
                                self.player_score += 1
                                self.ui_state = "END"

                        elif self.ui.stand_btn.clicked(pos):
                            self.message = "Dealer's Turn"
                            self.ui_state = "DEALER"

                if event.type == pygame.KEYDOWN:
                    if self.ui_state == "END":
                        if event.key == pygame.K_r:
                            self.reset_round()

                        if event.key == pygame.K_q:
                            running = False

            if self.ui_state == "DEALER":
                now = pygame.time.get_ticks()

                if now - self.last_dealer_action > 1000:
                    self.last_dealer_action = now

                    if self.dealer.has_to_hit():
                        self.dealer.hit(self.deck)
                    else:
                        self.end_round()
                        self.end_screen_time = now
                        self.ui_state = "ROUND_END"

            # ---- DRAW ----
            if self.ui_state == "ROUND_END":
                now = pygame.time.get_ticks()

                # Wait 1 seconds before showing end screen
                if now - self.end_screen_time > 1000:
                    self.ui_state = "END"

            if self.ui_state == "END":
                self.ui.draw_end_screen()
            else:
                self.ui.draw_game()

            pygame.display.flip()

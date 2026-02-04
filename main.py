from src.game import Game
from src.config import Config

if __name__ == "__main__":
    try:
        config: Config = Config()

    except Exception as e:
        print(f"Failed to setup config! Error: {e}")

    Game(config).start_game_loop()


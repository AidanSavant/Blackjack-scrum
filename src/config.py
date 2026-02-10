import os
import tomllib

class Config:
    def __init__(self, config_path: str = "config.toml") -> None:
        if not os.path.exists(config_path):
            raise FileNotFoundError("Config not found!")

        with open(config_path, 'rb') as config_handle:
            self._config = tomllib.load(config_handle)

        self.load_config()

    def load_config(self) -> None:
        config = self._config

        # NOTE: avoid config.get() to have custom key error
        try:
            window  = config["window"]
            misc    = config["misc"]
            ui      = config["ui"]
            buttons = config["buttons"]

            self.height         = window["height"]
            self.width          = window["width"]
            self.background_rgb = tuple(window["background_color_rgb"])

            self.table_x      = ui["table_x"]
            self.dealer_y     = ui["dealer_y"]
            self.player_y     = ui["player_y"]
            self.card_start_x = ui["card_start_x"]
            self.card_spacing = ui["card_spacing"]
            self.card_width   = ui["card_width"]
            self.card_height  = ui["card_height"]

            self.dealer_box   = tuple(ui["dealer_box"])
            self.player_box   = tuple(ui["player_box"])

            self.hit_btn      = tuple(buttons["hit"])
            self.stand_btn    = tuple(buttons["stand"])

            self.fps = misc["fps"]

        except KeyError as e:
            raise RuntimeError(f"Failed to load config! Missing: {e} field") from e


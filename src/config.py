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
            window = config["window"]
            misc   = config["misc"]

            self.height = window["height"]
            self.width  = window["width"]
            self.background_rgb = tuple(window["background_color_rgb"])

            self.fps = misc["fps"]

        except KeyError as e:
            raise RuntimeError(f"Failed to load config! Missing: {e} field") from e


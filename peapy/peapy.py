from .config import Config, get_default_config


class PeaPy:
    def __init__(self, config: Config = get_default_config()):
        self.config = config

    def __repr__(self):
        return f"{self.__class__.__name__}()"

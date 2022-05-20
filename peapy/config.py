from .exceptions import config as exceptions


class Config:
    """
    Used to pass configurations to the PeaPy constructor.
    """

    def __init__(self, from_dict: dict = None):
        """
        Initialize a Config object.

        :param from_dict: A dictionary to initialize the Config object with.
        """

        if from_dict is None:
            from_dict = {}

        for key, value in from_dict.items():
            if type(value) is dict:
                self.__dict__[key] = Config(value)
            else:
                self.__dict__[key] = value

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise exceptions.AttributeNotFound(name)

    def __setattr__(self, name, value):
        if type(value) is dict:
            self.__dict__[name] = Config(value)

        else:
            self.__dict__[name] = value

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            raise exceptions.AttributeNotFound(item)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def to_string(self, tab_level: int = 0) -> str:
        """
        Return a string representation of the Config object.

        :param tab_level: The number of tabs to add to the beginning of each line.
        :return: A string representation of the Config object.
        """

        output = ""
        for key, value in self.__dict__.items():
            if type(value) is Config:
                output += ("\t" * tab_level) + key + ":\n"
                output += value.to_string(tab_level + 1)

            else:
                output += ("\t" * tab_level) + key + ": " + str(value) + "\n"

        return output

    def __repr__(self):
        return self.to_string()


def get_default_config() -> Config:
    """
    Get the default configuration.

    :return: Config
    """

    return Config({
        "window": {
            "width": 800,
            "height": 600,
            "title": "Peapy",
            "icon": "icon.ico",
        },
        "colors": {
            "background": "#000000"
        }
    })

import peapy


def main():
    config = peapy.config.get_default_config()
    config.window.width = 1000
    print(config)


if __name__ == "__main__":
    main()

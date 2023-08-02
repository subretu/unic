import toml
import os


def get_path(key):
    config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "configs",
        key,
        "settings.toml",
    )

    return config_file_path


def parse_toml(key):
    file_path = get_path(key)

    with open(file_path) as f:
        obj = toml.load(f)
        return obj

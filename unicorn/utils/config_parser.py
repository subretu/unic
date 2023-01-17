import toml


def parse_toml(file_path):
    with open(file_path) as f:
        obj = toml.load(f)
        return obj

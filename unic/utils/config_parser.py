import tomli
import os


def get_path(key: str) -> str:
    config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "configs",
        key,
        "settings.toml",
    )

    return config_file_path


def parse_toml(key: str) -> dict[str, dict[str, float]]:
    file_path = get_path(key=key)

    try:
        with open(file_path, "rb") as f:
            obj = tomli.load(f)
            return obj

    except FileNotFoundError:
        raise ValueError(f"Configuration file not found: {file_path}")
    except tomli.TOMLDecodeError as e:
        raise ValueError(f"Syntax error in the TOML file: {file_path}, Error: {str(e)}")
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")

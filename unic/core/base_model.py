from abc import ABC, abstractmethod
from unic.utils import config_parser


class BaseModel(ABC):
    def __init__(self, model_name):
        self.model_config = config_parser.parse_toml(model_name)

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def convert_batch(self):
        pass

from abc import ABC, abstractmethod
from enum import Enum


class ComponentTypes(Enum):
    VIDEO_CARD = 'videocard'
    CPU = 'cpu'
    RAM = 'ram'
    ROM = 'rom'
    POWER_SUPPLY = 'powersupply'
    CASE = 'case'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ConfiguratorOptions(ABC):
    price: int
    type: str
    power: float


class ConfiguratorInterface(ABC):
    @abstractmethod
    def createAssembly(self, params: ConfiguratorOptions):
        pass
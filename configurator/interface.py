from enum import Enum


class ComponentType(Enum):
    CPU = 'cpu'
    GPU = 'video_card'
    MOTHERBOARD = 'motherboard'
    RAM = 'ram'
    HDD = 'hdd'
    SSD = 'ssd'
    POWER_SUPLY = 'power_supply'
    COOLING_SYSTEM = 'cooling_system'
    CASE = 'case'



    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)




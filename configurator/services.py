from __future__ import annotations

from configurator.interfaces import ConfiguratorInterface, ConfiguratorOptions, ComponentTypes
from configurator.models import Assembly, Component
from configurator.exceptions import WrongComponentType, NotEnoughComponents


class AssemblyBuilder:
    def __init__(self):
        self.assembly = Assembly()

    def set_video_card(self, component: Component) -> AssemblyBuilder:

        if component.type != ComponentTypes.VIDEO_CARD.value:
            raise WrongComponentType(f"expected type CPU but {component.type} given")
        self.assembly.components.add(component)
        return self

    def set_cpu(self, component: Component) -> AssemblyBuilder:
        if component.type != ComponentTypes.CPU:
            raise WrongComponentType(f"expected type CPU but {component.type} given")
        self.assembly.components.add(component)
        return self


class ConfiguratorService(ConfiguratorInterface):

    def createAssembly(self, params: ConfiguratorOptions):
        pass

    def __init__(self, builder: AssemblyBuilder):
        self.builder = builder


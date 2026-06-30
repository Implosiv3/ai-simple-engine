from ai_simple_engine.resources.abstract import Resource
from ai_simple_engine.device.base import Device
from typing import Union
from abc import ABC, abstractmethod


class ResourceBuilder(
    ABC
):

    @abstractmethod
    def is_supported(
        self,
        value: object
    ) -> bool:
        ...

    @abstractmethod
    def create(
        self,
        value: object,
        *,
        device: Union[Device, None]
    ) -> Resource:
        ...
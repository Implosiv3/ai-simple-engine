from ai_simple_engine.resources.resource import Resource
from ai_simple_engine.resources.resource_key import ResourceKey


class MusicGenResource(
    Resource
):

    @property
    def key(
        self
    ) -> ResourceKey:
        return ResourceKey(
            type = 'musicgen',
            identifier = self.model,
            device = self.device
        )

    def __init__(
        self,
        model: str,
        device: str
    ):
        self.model = model
        self.device = device

    async def load(
        self
    ):
        return MusicGen.load(
            self.model,
            device = self.device
        )

    async def unload(
        self,
        instance
    ):
        del instance
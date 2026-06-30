from dataclasses import dataclass


@dataclass(frozen = True)
class ModelFamily:

    name: str

    def __str__(
        self
    ):
        return self.name
    

MUSICGEN = ModelFamily('musicgen')
WHISPER = ModelFamily('whisper')
STABLE_DIFFUSION = ModelFamily('stable_diffusion')
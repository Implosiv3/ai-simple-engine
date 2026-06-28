"""
TODO: Maybe this will be transformed in the future
to be able to handle something stored in the disk.
"""
from ai_simple_engine.types.image import Image
from dataclasses import dataclass


@dataclass(frozen = True)
class Video:

    frames: list[Image]
    fps: float
from dataclasses import dataclass, field
from pathlib import Path

import tempfile
import os


@dataclass
class EngineSettings:
    """
    Global configuration shared by the engine and
    all plugins.
    """

    models_directory: Path = field(
        # default_factory = lambda: Path.home() / '.ai_simple_engine' / 'models'
        default_factory = lambda: os.getenv('MODELS_DIRECTORY', Path.home() / '.ai_simple_engine' / 'models')
    )

    cache_directory: Path = field(
        # default_factory = lambda: Path.home() / '.ai_simple_engine' / 'cache'
        default_factory = lambda: os.getenv('CACHE_DIRECTORY', Path.home() / '.ai_simple_engine' / 'cache')
    )

    temporary_directory: Path = field(
        # default_factory = lambda: Path(tempfile.gettempdir()) / 'ai_simple_engine'
        default_factory = lambda: os.getenv('TEMPORARY_DIRECTORY', Path(tempfile.gettempdir()) / 'ai_simple_engine')
    )
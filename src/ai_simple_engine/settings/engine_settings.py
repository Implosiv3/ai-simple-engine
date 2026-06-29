from dataclasses import dataclass, field
from pathlib import Path

import tempfile


@dataclass
class EngineSettings:
    """
    Global configuration shared by the engine and
    all plugins.
    """

    # TODO: Use environment variables here (?)
    models_directory: Path = field(
        default_factory = lambda: Path.home() / '.ai_simple_engine' / 'models'
    )

    cache_directory: Path = field(
        default_factory = lambda: Path.home() / '.ai_simple_engine' / 'cache'
    )

    temporary_directory: Path = field(
        default_factory = lambda: Path(tempfile.gettempdir()) / 'ai_simple_engine'
    )
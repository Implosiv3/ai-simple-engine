from ai_simple_engine.settings.engine_settings import EngineSettings
from ai_simple_engine.services.service_registry import ServiceRegistry
from dataclasses import dataclass


@dataclass(frozen = True)
class PluginContext:
    """
    Shared context passed to all plugin components.
    """

    settings: EngineSettings
    services: ServiceRegistry
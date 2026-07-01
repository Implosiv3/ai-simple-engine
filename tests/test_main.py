"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
def test_main_flow():
    from ai_simple_engine.engine_builder import EngineBuilder
    from ai_simple_engine.models.backends.abstract import ModelBackend
    from ai_simple_engine.models.loaders.abstract import ModelLoader
    from ai_simple_engine.execution.runtime_value_resolver.abstract import RuntimeValueResolver

    """
        Mocked classes to test below
    """

    class TestModelBackend(
        ModelBackend
    ):
        
        @property
        def provider(
            self
        ):
            return 'test_provider'
        
        def install(
            self,
            spec
        ):
            ...

    class TestModelLoader(
        ModelLoader
    ):
        
        @property
        def family(
            self
        ):
            return 'test_family'
        
        def load(
            self,
            installed_model,
            device
        ):
            ...

    class TestRuntimeValueResolver(
        RuntimeValueResolver
    ):
        
        def is_supported(
            self,
            value
        ):
            return True
        
        def resolve(
            self,
            value,
            context
        ):
            ...
        

    """
        Mocked classes to test above
    """

    engine_builder = EngineBuilder()

    engine_builder.add_model_backend(
        TestModelBackend()
    )

    engine_builder.add_model_loader(
        TestModelLoader()
    )

    engine_builder.add_runtime_value_resolver(
        TestRuntimeValueResolver()
    )
    # TODO: Do this
    # engine_builder.add_service(

    # )
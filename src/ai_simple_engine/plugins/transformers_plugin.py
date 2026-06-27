"""
TODO: I think this has to be in the other
project that implements this functionality.
"""
from ai_simple_engine.plugins.plugin import Plugin


# TODO: Create this below where it should be
class TransformersOperations:
    
    def register(
        self,
        builder
    ):
        for operation in self.operations():
            builder.add_operation(operation)

class TransformersModelLoaders:
    pass

class TransformersModelProviders:
    pass

class TransformersDataTypes:
    pass


class TransformersPlugin(
    Plugin
):
    
    def providers(
        self
    ):
        return [
            TransformersOperations(),
            TransformersModelLoaders(),
            TransformersModelProviders(),
            TransformersDataTypes()
        ]
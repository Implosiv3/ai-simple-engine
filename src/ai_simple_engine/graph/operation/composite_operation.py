from ai_simple_engine.graph.operation.base import Operation
from abc import abstractmethod


class CompositeOperation(
    Operation
):
    """
    An operation that is actually a set of
    different operations. For example, when
    we want to generate an Image, we must
    follow 4 steps:

    1. LoadModel
    2. EncodePrompt
    3. Sample
    4. DecodeVAE

    This will encapsulate those operations
    so we don't need to define them again
    individually if we will perform the
    same set of operations.

    This class will be resolved as a set of
    operations in which each individual
    operation will be checked and evaluated.
    """

    @classmethod
    @abstractmethod
    def build(
        cls
    ):
        """
        Build the internal workflow including all
        the different operations that must be
        performed.

        This is to encapsulate a workflow, such as
        `CreateImage`, to reuse a set of operations
        again and again.
        """
        ...
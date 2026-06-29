from abc import ABC


class ModelExecutor(
    ABC
):
    """
    Base class for all inference runners that
    will execute the code to actually perform
    an operation.

    This is the specialist who knows how to use
    a `LoadedModel` to obtain the expected
    results.

    It doesn't download nor load the model, it
    just receives and uses it.
    """
from dataclasses import dataclass


@dataclass(frozen = True, slots = True)
class PortReference:
    """
    A basic reference to a port that uses
    its `name` and `type` to identify it.
    """

    operation: 'Operation'
    output: 'Output'

    @property
    def name(
        self
    ) -> str:
        return self.output.name

    @property
    def type(
        self
    ):
        return self.output.type
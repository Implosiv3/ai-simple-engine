"""
TODO: Maybe this module shouldn't be here.
"""
class Cache:

    def __init__(
        self
    ):
        self._entries: dict[str, dict[str, object]] = {}

    def contains(
        self,
        fingerprint: str
    ) -> bool:
        return fingerprint in self._entries

    def get(
        self,
        fingerprint: str
    ) -> dict[str, object]:
        return self._entries[fingerprint]

    def put(
        self,
        fingerprint: str,
        outputs: dict[str, object]
    ) -> None:
        self._entries[fingerprint] = outputs
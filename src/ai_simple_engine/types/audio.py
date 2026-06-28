from dataclasses import dataclass

# TODO: I don't want the import by now
# import numpy as np


@dataclass(frozen = True)
class Audio:

    samples: 'np.ndarray'
    sample_rate: int
from math import cos, sin

import numpy as np
from numpy.typing import ArrayLike


def rotation(angle: float):  # in rad
    c = cos(angle)
    s = sin(angle)

    return np.array([[c, -s], [s, c]])


class Polygon:
    def __init__(self, vertices: list[ArrayLike]) -> None:
        self.vertices = vertices
        self.angle: float = 0  # rad
        self.offset: ArrayLike = np.array([0.0, 0.0])

    def support(self, direction: ArrayLike) -> ArrayLike:
        m = rotation(self.angle)
        points = [m * v + self.offset for v in self.vertices]

        score: float = points[0] @ direction
        result = points[0]
        for p in points[1:]:
            if score < p @ direction:
                result = p

        return result

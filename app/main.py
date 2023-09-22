from __future__ import annotations


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)

    def __iadd__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        if isinstance(other, (int, float)):
            self.km = self.km + other
            return self

    def __mul__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km * other.km)
        if isinstance(other, (int, float)):
            # if other == 0:
            #     return None
            return Distance(self.km * other)

    def __truediv__(self, other: (int, float, Distance)) -> Distance:
        if isinstance(other, Distance) and other.km > 0 :
            return Distance(round(self.km / other.km, 2))
        if isinstance(other, (int, float)) and other > 0:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other

    def __gt__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other

    def __le__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: (int, float, Distance)) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other

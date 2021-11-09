"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730163077"


class Simpy:
    """Simpy utility."""
    values: list[float]
    x: float
    limit: int
    start: float
    stop: float
    step: float

    def __init__(self, values: list[float]):
        """Initizalizes constructor."""
        self.values = values

    def __repr__(self) -> str:
        """Method to represent object as string."""
        return f"Simpy({self.values})"

    def fill(self, x: float, limit: int) -> None:
        """Fills values with a specific number of repeating values."""
        self.values = []
        for i in range(limit):
            self.values.append(x)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values with range of values."""
        assert step != 0.0
        self.values = []
        r = start
        if r < stop:
            while r < stop:
                self.values.append(r)
                r += step
        else:
            while r > stop: 
                self.values.append(r)
                r += step
    
    def sum(self) -> float:
        """Compute and returns the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds up items in lists."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Takes two lists or a float and puts one to the exponent of the other."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes the remainder."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use for equal operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use for greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values) 
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            assert len(self.values) == len(rhs) 
            results: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    results.append(self.values[i])
            return Simpy(results)
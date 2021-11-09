"""Examples of vectorized operations on StrArray."""

from __future__ import annotations

from typing import Union

class StrArray:
    """Utility class for common string column operations."""

    values: list[str]

    def __init__(self, values: list[str]):
        self.values = values

    def __repr__(self) -> str:
        return f"StrArray({self.values})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        # result: list[str] = []
        #for item in self.values: this works when it was just for str
            #result.append(item + rhs)
        #return StrArray(result)
        ## print(f"__add__({self}, {rhs})") #shows how many times add was evalutated.
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values) # makes sure they are the same length or else program will fail
            for i in range(len(self.values)): # starts at 0 but stops at n-1, in s it would stop at 2
                result.append(self.values[i] + rhs.values[i])

        return StrArray(result)




s: StrArray = StrArray(["a", "b", "c"])
t = StrArray(["d", "e", "f"])
print(s + "!")
print(s + t)
print(s + s + s)
print(s + " " + s + "!")
first = StrArray(["Kris", "Kaki", "Jenna"])
last = StrArray(["Jordan", "Ryan", "Zottoli"])
full_name = last + ", " + first
print(full_name)
other_name = first + " " + last
print(other_name)
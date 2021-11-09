"""EX03 - avoid_fifth function."""

__author__: str = "730163077"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    print(avoid_fifth("hello world, my name is EEEEEEEEEdgar."))


def avoid_fifth(x: str) -> str:
    """This function will remove the character "e" or "E" from a string."""
    i: int = 0
    empty_string: str = ""
    while i < len(x):
        if x[i] == "e" or x[i] == "E":
            i += 1
        else:
            empty_string += x[i]
            i += 1
    return empty_string


if __name__ == "__main__":
    main()
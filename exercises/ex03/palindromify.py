"""EX03 - palindromify function."""

__author__: str = "730163077"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))

    
def palindromify(word: str, is_odd: bool) -> str:
    """This will palindromify a str."""
    if is_odd:
        chars = ""
        counter = len(word) - 1
        while counter > -1:
            chars += word[counter]
            counter -= 1
        return word + chars
    else:
        chars = ""
        counter = len(word) - 2
        while counter > - 1:
            chars += word[counter]
            counter -= 1
        return word + chars
        

if __name__ == "__main__":
    main()
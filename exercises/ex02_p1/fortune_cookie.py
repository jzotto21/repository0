"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730163077"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Returns a fortune."""
    fortune = randint(1, 400)
    if fortune < 100:
        return "Make peace with the universe."
    else:
        if fortune < 200:
            return "Keep trying and wipe your tears."
        else:
            if fortune < 300:
                return "Crying is good for the soul."
            else:
                if fortune < 400: 
                    return "Thank the gods this worked."
    return "fortune"
    

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
"""Abbreviation"""

def find_capitals(word: str) -> str:
    capitals: str = ""
    #i is going from 0 up to len - 1
    for i in range(len(word)):
        if word[i].lower() != word[i]:
            captials += word[i]
    return capitals


def abbreviate(strings: list[str]) -> dict[str, str]:
    abbrievations: dict[str, str] = {}

    for fun_word in strings:
        abbreviated: str = find_capitals(fun_word)
        abbrievations[fun_word] = abbreviated
    return abbreviated




def phonebook(phone_num: list[int], names: list[str]) -> dict[int, str]:
    book: dict[int, str] = {}

    for i in range(len(phone_num)):
        abbrieviation = find_capitals(names[i])
        book[phone_num[i]] = abbrieviation
    return book
"""Utility functions for wrangling data."""

__author__ = "730163077"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        print(row)
        rows.append(row)
    
    file_handle.close()
    return rows


# TODO: Define the other functions here.
def column_values(table: list[dict[str, str]], string: str) -> list[str]:
    """Returns subject_age column values."""
    column_values: list[str] = []

    for row in table: 
        column_values.append(str(row[string]))
    return column_values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforming a table."""
    empty_dict: dict[str, list[str]] = {}
    for i in table[0]:
        empty_dict[i] = column_values(table, i)
    return empty_dict


def head(table1: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Making a table."""
    empty_dict1: dict[str, list[str]] = {}
    for col in table1:
        list2: list[str] = []
        if N > len(table1[col]):
            N = len(table1[col])
        for i in range(N):
            list2.append(table1[col][i])
        empty_dict1[col] = list2
    return empty_dict1


def select(table2: dict[str, list[str]], list3: list[str]) -> dict[str, list[str]]:
    """Select."""
    empty_dict2: dict[str, list[str]] = {}
    for col in list3:
        empty_dict2[col] = table2[col]
    return empty_dict2


def count(values: list[str]) -> dict[str, int]:
    """Counting the frequency of values."""
    empty_dict3: dict[str, int] = {}
    for i in values:
        if i in empty_dict3:
            empty_dict3[i] += 1
        else: 
            empty_dict3[i] = 1
    return empty_dict3
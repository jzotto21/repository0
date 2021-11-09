"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730163077"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    x: int = int(days_to_target(population, doses, doses_per_day, target))
    y: str = str(future_date(x))
    print("We will reach " + str(target) + "% vaccination" + " in " + str(x) + " days, " "which falls on ")
    print(str(y) + ".")
    

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns days to target."""
    percent_to_be_vac: int = int(population * ((target / 100)))
    ppl_left_to_vac: int = int(percent_to_be_vac - (doses) / 2)
    doses_need: int = int(ppl_left_to_vac * 2)
    days_to_goal: int = int(doses_need / doses_per_day)
    return days_to_goal


def future_date(w: int) -> str:
    """Returns the future."""
    today: datetime = datetime.today()
    days_to_target: timedelta = timedelta(w)
    future: datetime = today + days_to_target
    return future.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()   
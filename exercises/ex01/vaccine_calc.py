"""A vaccination calculator."""

__author__ = "730163077"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

# Begin your solution here...
today: datetime = datetime.today()

pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))

percent_to_be_vac: int = int(pop * ((target / 100)))
ppl_left_to_vac: int = int(percent_to_be_vac - (doses_admin) / 2)
doses_need: int = int(ppl_left_to_vac * 2)
days_to_goal: int = int(doses_need / doses_per_day)


days: timedelta = timedelta((days_to_goal))
future: datetime = today + days

print("We will reach " + str(target) + "% vaccination" + " in " + str(days_to_goal) + " days, " "which falls on ")
print((future.strftime("%B %d, %Y")) + ".")

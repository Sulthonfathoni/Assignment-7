class Date:
  """A class representing a date."""

  def __init__(self, day, month, year):
    """Initializes the date.

    Args:
      day: The day of the month.
      month: The month of the year.
      year: The year.
    """
    self.day = day
    self.month = month
    self.year = year

  def __repr__(self):
    """Returns a string representation of the date."""
    return f"{self.day}/{self.month}/{self.year}"

  def show(self):
    """Displays the date."""
    print(self)

  def add(self, other):
    """Adds two dates.

    Args:
      other: The other date to add.

    Returns:
      The sum of the two dates.
    """
    days = self.day + other.day
    months = self.month + other.month
    years = self.year + other.year

    # Check if the days are more than 30.
    if days > 30:
      months += 1
      days -= 30

    # Check if the months are more than 12.
    if months > 12:
      years += 1
      months -= 12

    return Date(days, months, years)

  def sub(self, other):
    """Subtracts two dates.

    Args:
      other: The other date to subtract.

    Returns:
      The difference of the two dates.
    """
    days = self.day - other.day
    months = self.month - other.month
    years = self.year - other.year

    # Check if the days are less than 1.
    if days < 1:
      months -= 1
      days += 30

    # Check if the months are less than 1.
    if months < 1:
      years -= 1
      months += 12

    return Date(days, months, years)

def main():
  """The main function."""
  date1 = Date(1, 1, 2023)
  date2 = Date(31, 12, 2022)

  date1.show()
  date2.show()

  date3 = date1.add(date2)
  date3.show()

  date4 = date1.sub(date2)
  date4.show()

if __name__ == "__main__":
  main()
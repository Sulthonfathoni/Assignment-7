class Fraction:
  """A class representing a fraction."""

  def __init__(self, numerator, denominator):
    """Initializes the fraction.

    Args:
      numerator: The numerator of the fraction.
      denominator: The denominator of the fraction.
    """
    self.numerator = numerator
    self.denominator = denominator

  def __repr__(self):
    """Returns a string representation of the fraction."""
    return f"{self.numerator}/{self.denominator}"

  def __add__(self, other):
    """Adds two fractions.

    Args:
      other: The other fraction to add.

    Returns:
      The sum of the two fractions.
    """
    numerator = self.numerator * other.denominator + self.denominator * other.numerator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)

  def __sub__(self, other):
    """Subtracts two fractions.

    Args:
      other: The other fraction to subtract.

    Returns:
      The difference of the two fractions.
    """
    numerator = self.numerator * other.denominator - self.denominator * other.numerator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)

  def __truediv__(self, other):
    """Divides two fractions.

    Args:
      other: The other fraction to divide by.

    Returns:
      The quotient of the two fractions.
    """
    numerator = self.numerator * other.denominator
    denominator = self.denominator * other.numerator
    return Fraction(numerator, denominator)

def main():
  """The main function."""
  fraction1 = Fraction(1, 2)
  fraction2 = Fraction(3, 4)

  print("Adding two fractions:", fraction1 + fraction2)
  print("Subtracting two fractions:", fraction1 - fraction2)
  print("Dividing two fractions:", fraction1 / fraction2)

if __name__ == "__main__":
  main()
class Time:
  """A class representing a time."""

  def __init__(self, hours, minutes, seconds):
    """Initializes the time.

    Args:
      hours: The number of hours.
      minutes: The number of minutes.
      seconds: The number of seconds.
    """
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def __repr__(self):
    """Returns a string representation of the time."""
    return f"{self.hours}:{self.minutes}:{self.seconds}"

  def to_seconds(self):
    """Converts the time to seconds.

    Returns:
      The number of seconds.
    """
    return self.hours * 3600 + self.minutes * 60 + self.seconds

  @classmethod
  def from_seconds(cls, seconds):
    """Converts seconds to a time.

    Args:
      seconds: The number of seconds.

    Returns:
      A Time object.
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return cls(hours, minutes, seconds)

def main():
  """The main function."""
  time = Time(1, 2, 3)
  print("Time:", time)

  seconds = time.to_seconds()
  print("Seconds:", seconds)

  time2 = Time.from_seconds(seconds)
  print("Time2:", time2)

if __name__ == "__main__":
  main()
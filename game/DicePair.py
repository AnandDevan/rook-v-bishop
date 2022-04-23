import random

class DicePair:
  @staticmethod
  # simulate dice roll with a single call to randint
  def roll():
    return random.randint(2, 12)

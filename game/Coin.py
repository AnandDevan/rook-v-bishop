import random

class Coin:
  @staticmethod
  # probably can introduce an enum here instead of strings
  def flip():
    return 'Tail' if random.randint(0,1) else 'Head' 

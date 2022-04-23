import random

class Coin:
  @staticmethod
  def flip():
    return 'Tail' if random.randint(0,1) else 'Head' 

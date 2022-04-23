class Position:
  def __init__(self, x , y):
    self.set(x,y)

  def set(self, x, y):
    if x > 7 or x < 0:
      raise RuntimeError('x position out of bounds')
    if y > 7 or y < 0:
      raise RuntimeError('y position out of bounds')
    self.x = x
    self.y = y
  def getString(self):
    file = chr(ord('a') + self.x)
    row = self.y + 1
    return ("file: %s, row: %s" %(file, row))

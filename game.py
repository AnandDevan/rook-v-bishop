import random

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

class ChessPiece:
  def __init__(self, type, pos):
    self.type = type
    self.pos = pos

  def move(delX, delY):
    raise NotImplementedError("Implement move method for class %s" % (type(self).__name__))

  def willCapture(self, targetPiece):
    raise NotImplementedError("Implement willCapture method for class %s" % (type(self).__name__))

class ChessPieceRook(ChessPiece):
  def __init__(self, pos):
    super().__init__('rook', pos)

  def move(self, delX, delY):
    self.pos.x = (self.pos.x + delX) % 8 
    self.pos.y = (self.pos.y + delY) % 8

class ChessPieceBishop(ChessPiece):
  def __init__(self, pos):
    super().__init__('bishop', pos)

  def willCapture(self, targetPiece):
    if abs(targetPiece.pos.x - self.pos.x) \
      == abs(targetPiece.pos.y - self.pos.y):
      return True
    else:
      return False

class DicePair:
  @staticmethod
  def roll():
    return random.randint(2, 12)

class Coin:
  @staticmethod
  def flip():
    return 'Tail' if random.randint(0,1) else 'Head' 

class ChessBoardState:
  def __init__(self, bishop, rook):
    self.bishop = bishop
    self.rook = rook

  def print(self):
    for p in self.pieces:
      p.print()

  def getNextMove(self):
    delX, delY = 0,0
    moves = DicePair.roll()
    coinFlip  = Coin.flip()
    if coinFlip == 'Head':
      delY = moves
    else:
      delX = moves

    print("Dice roll total: %s" % moves)
    print("Coin Flip: %s" % coinFlip)
    print("Move delX: %s, delY: %s" % (delX, delY))

    return delX, delY

  def play(self):
    print(self.bishop.pos.getString())
    for i in range(0,15):
      print("-" * 50)
      print("Move # %s" % i)
      print("Start: %s" % self.rook.pos.getString())
      delX, delY = self.getNextMove()
      self.rook.move(delX, delY)
      print("End: %s" % self.rook.pos.getString())
      if self.bishop.willCapture(self.rook):
        print('\nGame Over - bishop won')
        return
    print('\nGame over - rook won')

if __name__ == '__main__':
  rook = ChessPieceRook(Position(7,0))
  bishop = ChessPieceBishop(Position(2,2))

  board = ChessBoardState(bishop, rook)
  board.play()

from .ChessPieceBishop import *
from .ChessPieceRook import *
from .Coin import *
from .DicePair import *
from .Position import *

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

from .ChessPiece import *

class ChessPieceBishop(ChessPiece):
  def __init__(self, pos):
    super().__init__('bishop', pos)

  def willCapture(self, targetPiece):
    if abs(targetPiece.pos.x - self.pos.x) \
      == abs(targetPiece.pos.y - self.pos.y):
      return True
    else:
      return False

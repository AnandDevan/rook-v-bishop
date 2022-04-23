from .ChessPiece import *

class ChessPieceRook(ChessPiece):
  def __init__(self, pos):
    super().__init__('rook', pos)

  def move(self, delX, delY):
    self.pos.x = (self.pos.x + delX) % 8 
    self.pos.y = (self.pos.y + delY) % 8

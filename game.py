from game.ChessBoardState import *
from game.ChessPieceBishop import *
from game.ChessPieceRook import *
from game.Position import *

if __name__ == '__main__':
  rook = ChessPieceRook(Position(7,0))
  bishop = ChessPieceBishop(Position(2,2))

  board = ChessBoardState(bishop, rook)
  board.play()

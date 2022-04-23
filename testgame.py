import unittest
from game.ChessPieceBishop import *
from game.ChessPieceRook import *
from game.Position import *

class TestGameMethods(unittest.TestCase):
  # test willCapture (one piece can capture another)
  def test_willCapture(self):
    bishop = ChessPieceBishop(Position(2,3))
    rook = ChessPieceRook(Position(4,6))
    self.assertFalse(bishop.willCapture(rook))

    bishop.pos.set(3,2)
    rook.pos.set(2,1)
    self.assertTrue(bishop.willCapture(rook))

    bishop.pos.set(3,2)
    rook.pos.set(6,5)
    self.assertTrue(bishop.willCapture(rook))

    bishop.pos.set(3,2)
    rook.pos.set(0,0)
    self.assertFalse(bishop.willCapture(rook))

    bishop.pos.set(3,2)
    rook.pos.set(4,3)
    self.assertTrue(bishop.willCapture(rook))

  # test move (move piece by x, y offset)
  def test_move(self):
    rook = ChessPieceRook(Position(0,7))
    rook.move(0,1)
    self.assertTrue(rook.pos.y == 0)

    rook.pos.set(0,7)
    rook.move(0,3)
    self.assertTrue(rook.pos.y == 2)

    rook.pos.set(0,2)
    rook.move(0,-3)
    self.assertTrue(rook.pos.y == 7)

    rook.pos.set(6,2)
    rook.move(3,0)
    self.assertTrue(rook.pos.x == 1)

    rook.pos.set(2,2)
    rook.move(-3,0)
    self.assertTrue(rook.pos.x == 7)

    rook.pos.set(2,2)
    with self.assertRaises(RuntimeError) as cm:
      rook.move(3,1)

  # test out of bounds, for Position class
  def test_Position(self):
    with self.assertRaises(RuntimeError) as cm:
      p = Position(3,10)
    p = Position(0,0)
    with self.assertRaises(RuntimeError) as cm:
      p.set(8,1)
    p = Position(1,3)
    self.assertTrue(p.x == 1)
    self.assertTrue(p.y == 3)



if __name__ == '__main__':
    unittest.main()


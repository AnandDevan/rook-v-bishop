import unittest
import game

class TestGameMethods(unittest.TestCase):
  def test_willCapture(self):
    bishop = game.ChessPieceBishop(game.Position(2,3))
    rook = game.ChessPieceRook(game.Position(4,6))
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

  def test_move(self):
    rook = game.ChessPieceRook(game.Position(0,7))
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

  def test_Position(self):
    with self.assertRaises(RuntimeError) as cm:
      p = game.Position(3,10)
    p = game.Position(0,0)
    with self.assertRaises(RuntimeError) as cm:
      p.set(8,1)
    p = game.Position(1,3)
    self.assertTrue(p.x == 1)
    self.assertTrue(p.y == 3)



if __name__ == '__main__':
    unittest.main()


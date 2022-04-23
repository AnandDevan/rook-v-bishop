class ChessPiece:
  def __init__(self, type, pos):
    self.type = type
    self.pos = pos

  def move(delX, delY):
    raise NotImplementedError("Implement move method for class %s" % (type(self).__name__))

  def willCapture(self, targetPiece):
    raise NotImplementedError("Implement willCapture method for class %s" % (type(self).__name__))

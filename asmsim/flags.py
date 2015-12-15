class Flags(object):
  """ The object that stores current flags. """
  def __init__(self, N = 0, Z = 0, C = 0, V = 0):
    super(Flags, self).__init__()
    self.N = N
    self.Z = Z
    self.C = C
    self.V = V


  def update(self, N = None, Z = None, C = None, V = None):
    """ Update the flags attributes all at once. """
    if N != None: self.N = N
    if Z != None: self.Z = Z
    if C != None: self.C = C
    if V != None: self.V = V


if __name__ == "__main__":
  flags = Flags()
  print(flags.N, flags.Z, flags.C, flags.V)
  flags.update(N = 1, C = 1)
  print(flags.N, flags.Z, flags.C, flags.V)

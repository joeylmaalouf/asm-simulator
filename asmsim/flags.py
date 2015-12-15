class Flags(object):
  """ The object that stores current flags. """
  def __init__(self, N = 0, Z = 0, C = 0, V = 0):
    super(Flags, self).__init__()
    self.Nflag = N
    self.Zflag = Z
    self.Cflag = C
    self.Vflag = V


  def update(self, N = None, Z = None, C = None, V = None):
    """ Update the flags attributes all at once. """
    if N != None: self.Nflag = N
    if Z != None: self.Zflag = Z 
    if C != None: self.Cflag = C 
    if V != None: self.Vflag = V 


if __name__ == "__main__":
  flags = Flags("0, 0, 0, 0")
  print(flags.raw)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)
  flags.update(N = 1, C = 1)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)

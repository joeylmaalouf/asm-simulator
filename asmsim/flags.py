class Flags(object):
  """ The object that stores current flags. """
  def __init__(self, text):
    super(Flags, self).__init__()
    words = text.replace(",", " ").split()
    self.raw = text
    self.Nflag = words[0]
    self.Zflag = words[1] if len(words) > 1 else None
    self.Cflag = words[2] if len(words) > 2 else None
    self.Vflag = words[3] if len(words) > 3 else None

  #def update(self,*flag):
  def update(self, N = None, Z = None, C = None, V = None):
    """ Update the flags attributes all at once. Format is N/Z/V/C = (a number) """
    if N != None: self.Nflag = N
    if Z != None: self.Zflag = Z 
    if C != None: self.Cflag = C 
    if V != None: self.Vflag = V 

if __name__ == "__main__":
  flags = Flags("0, 0, 0, 0")
  print(flags.raw)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)
  flags.update(1, None, 1, None)
  flags.update(N = 1, C = 1)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)
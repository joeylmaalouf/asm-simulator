class Flags(object):
  """ The object that stores current flags. """
  def __init__(self, text):
    super(Flags, self).__init__()
    words = text.replace(",", "").split()
    self.raw = text
    self.Nflag = words[0]
    self.Zflag = words[1]
    self.Cflag = words[2]
    self.Vflag = words[3]

  def update(self, Nflag, Zflag, Cflag, Vflag):
    """ Update the flags attributes all at once. """
    self.Nflag = Nflag
    self.Zflag = Zflag
    self.Cflag = Cflag
    self.Vflag = Vflag

if __name__ == "__main__":
  flags = Flags("1, 0, 1, 1")
  print(flags.raw)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)
  flags.update(0,0,0,0)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)

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
    

  # def update(self, Nflag, Zflag, Cflag, Vflag):
  #   """ Update the flags attributes all at once. """
  #   if Nflag != None: self.Nflag = Nflag
  #   if Zflag != None: self.Zflag = Zflag
  #   if Cflag != None: self.Cflag = Cflag
  #   if Vflag != None: self.Vflag = Vflag
  
  def update(self,*flag):
    """ Update the flags attributes all at once. """
    if flag[0] != None: self.Nflag = flag[0]
    if len(flag) > 1 and flag[1] != None: self.Zflag = flag[1] 
    if len(flag) > 2 and flag[2] != None: self.Cflag = flag[2] 
    if len(flag) > 3 and flag[3] != None: self.Vflag = flag[3] 


  def updateN(self, Nflag):
  	if Nflag != None: self.Nflag = Nflag

  def updateZ(self, Zflag):
  	if Zflag != None: self.Zflag = Zflag

  def updateC(self, Cflag):
  	if Cflag != None: self.Cflag = Cflag

  def updateV(self, Vflag):
  	if Vflag != None: self.Vflag = Vflag
  

if __name__ == "__main__":
  flags = Flags("0, 0, 0, 0")
  print(flags.raw)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)
  flags.update(1, , 1, None)
  print(flags.Nflag, flags.Zflag, flags.Cflag, flags.Vflag)

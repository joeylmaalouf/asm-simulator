def getval(hexstring, signed = True):
  if signed: return twoscomp(hexstring)
  else:      return int(hexstring, 16)


def twoscomp(hexstring):
  val = int(hexstring, 16)
  binstring = "{0:0{1}b}".format(int(hexstring, 16), 32)
  if binstring[0] == "1":
    val -= (1 << 32)
  return val


if __name__ == "__main__":
  print(getval("00000000", True))
  print(getval("7FFFFFFF", True))
  print(getval("80000000", True))
  print(getval("FFFFFFFF", True))
  print("")
  print(getval("00000000", False))
  print(getval("7FFFFFFF", False))
  print(getval("80000000", False))
  print(getval("FFFFFFFF", False))

def getval(hexstring, signed = True):
  if signed: return twoscomp(hexstring)
  else:      return int(hexstring, 16)


def twoscomp(hexstring):
  val = int(hexstring, 16)
  binstring = "{0:0{1}b}".format(int(hexstring, 16), 32)
  if binstring[0] == "1":
    val -= (1 << 32)
  return val


def syscall(v0):
  if v0 == 1:
    print a0
  elif v0 in [2, 3]:
    print fl2
  elif v0 == 4:
    print a0
  elif v0 == 5:
    pass
  elif v0 == 6:
    pass
  elif v0 == 7:
    pass
  elif v0 == 8:
    pass
  elif v0 == 9:
    pass
  elif v0 == 10:
    return True
  elif v0 == 11:
    pass
  elif v0 == 12:
    pass
  elif v0 == 13:
    pass
  elif v0 == 14:
    pass
  elif v0 == 15:
    pass
  elif v0 == 16:
    pass
  elif v0 == 17:
    pass
  elif v0 == 30:
    pass
  elif v0 == 31:
    pass
  elif v0 == 32:
    sleep(a0*.001)
  elif v0 == 33:
    pass
  elif v0 == 34:
    pass
  elif v0 == 35:
    pass
  elif v0 == 36:
    pass
  elif v0 in [37, 38, 39, 45, 46, 47, 48, 49]:
    pass
  elif v0 == 40:
    pass
  elif v0 == 41:
    pass
  elif v0 == 42:
    pass
  elif v0 == 43:
    pass
  elif v0 == 44:
    pass
  elif v0 == 50:
    pass
  elif v0 == 51:
    pass
  elif v0 == 52:
    pass
  elif v0 == 53:
    pass
  elif v0 == 54:
    pass
  elif v0 == 55:
    pass
  elif v0 == 56:
    pass
  elif v0 == 57:
    pass
  elif v0 == 58:
    pass
  elif v0 == 59:
    pass


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

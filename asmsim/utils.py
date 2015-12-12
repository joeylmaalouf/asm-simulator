import time
from modes import mode_dict


def num_upper(val):
  """ Get a hex string of the upper 16 bits in a 32 bit number. """
  return hex(int(bin(val)[:-16], 2))


def num_lower(val):
  """ Get a hex string of the lower 16 bits in a 32 bit number. """
  return hex(int(bin(val)[-16:], 2))


def getval(hexstring, signed = True):
  """ Get the value of the inputted hex string based on whether or not the input is signed. """
  if signed: return twoscomp(hexstring)
  else:      return int(hexstring, 16)


def twoscomp(hexstring):
  """ Return the two's complement value of a hex string. """
  val = int(hexstring, 16)
  binstring = "{0:0{1}b}".format(int(hexstring, 16), 32)
  if binstring[0] == "1":
    val -= (1 << 32)
  return val


def parseaddress(hexstring):
  """ Parse a register/offset string for its individual values. """
  leftpars, rightpars = hexstring.count("("), hexstring.count(")")
  if leftpars == 1 and rightpars == 1:
    offset, register = hexstring.replace(")", "").split("(")
    for d in mode_dict.values():
      if offset in d:
        register, offset = offset, register
        break
    if offset == "":
      offset = "0"
    return register, offset
  elif leftpars == 0 and rightpars == 0:
    return hexstring, "0"
  elif leftpars != rightpars:
    raise ValueError("Unbalanced parentheses: {0}".format(hexstring))
  else:
    raise ValueError("More than one pair of parentheses: {0}".format(hexstring))


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
    time.sleep(a0*.001)
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
  print("")
  print(parseaddress("A($t0)"))
  print(parseaddress("$t0(A)"))
  print(parseaddress("($t0)"))
  print(parseaddress("$t0"))
  print(parseaddress("0"))

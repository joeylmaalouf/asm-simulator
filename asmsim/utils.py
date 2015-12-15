import time


def num_upper(val):
  """ Get a hex string of the upper 16 bits in a 32 bit number. """
  return hex(int(bin(val)[:-16], 2))


def num_lower(val):
  """ Get a hex string of the lower 16 bits in a 32 bit number. """
  return hex(int(bin(val)[-16:], 2))


def getimm(hexstring, signed = True):
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


def getval(registers, operand):
  if operand[0] == "#": return getimm(operand[1:], False)
  else:                 return registers[operand]


def parse_address(hexstring):
  """ Parse an address/offset string for its individual values. """
  leftpars, rightpars = hexstring.count("("), hexstring.count(")")
  if leftpars == 1 and rightpars == 1:
    outside, inside = hexstring.replace(")", "").split("(")
    if outside == "": outside = "0"
    if inside == "":  inside = "0"
    return outside, inside
  elif leftpars == 0 and rightpars == 0:
    return hexstring, "0"
  elif leftpars != rightpars:
    raise ValueError("Unbalanced parentheses: {0}".format(hexstring))
  else:
    raise ValueError("More than one pair of parentheses: {0}".format(hexstring))


def calcval(value, assembler):
  """ Determine whether a value is a data label, register,
  or number address, and return the corresponding value. """
  if value in assembler.memory.labels:          return assembler.memory.labels[value]
  elif value in assembler.registers.conversion: return assembler.registers[value]
  else:                                         return getimm(value, True)


def parse_arm_instr(instr):
  conditions = [
    "eq",
    "ne",
    "cs", "hs",
    "cc", "lo",
    "mi",
    "pl",
    "vs",
    "vc",
    "hi",
    "ls",
    "ge",
    "lt",
    "gt",
    "le",
    "al"
  ]
  sets_flags = instr[-1] == "s" and instr[-2:] not in conditions
  if sets_flags: instr = instr[:-1]
  condition = instr[-2:] if instr[-2:] in conditions else ""
  operation = instr[:-2] if condition else instr
  return operation, condition, sets_flags


def mips_syscall(v0):
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
  print(getimm("00000000", True))
  print(getimm("7FFFFFFF", True))
  print(getimm("80000000", True))
  print(getimm("FFFFFFFF", True))
  print("")
  print(getimm("00000000", False))
  print(getimm("7FFFFFFF", False))
  print(getimm("80000000", False))
  print(getimm("FFFFFFFF", False))
  print("")
  print(parse_address("A($t0)"))
  print(parse_address("$t0(A)"))
  print(parse_address("($t0)"))
  print(parse_address("$t0"))
  print(parse_address("0"))
  print("")
  print(parse_arm_instr("add"))
  print(parse_arm_instr("addal"))
  print(parse_arm_instr("adds"))
  print(parse_arm_instr("teqeq"))
  print(parse_arm_instr("subeq"))
  print(parse_arm_instr("teqls"))
  print(parse_arm_instr("addnes"))

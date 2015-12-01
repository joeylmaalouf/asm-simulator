from modes import mode_dict


class Registers(object):
  """ The registers object that contains the register values and proper getting/setting methods. """
  def __init__(self, mode = "MIPS"):
    super(Registers, self).__init__()
    if mode.upper() in mode_dict:
      self.conversion = mode_dict[mode.upper()]
    else:
      raise ValueError("Assembler mode must be one of the following: {0}. Invalid mode: {1}".format(", ".join(mode_dict.keys()), mode))
    self.data = [0] * (max(self.conversion.values()) + 1)
    # data is of length equal to the total number of registers;
    # len() won't do because the conversion dict can have multiple string aliases for the same register

  def __str__(self):
    """ String representation of the registers. """
    return "\n".join(str(d) for d in self.data)

  def __getitem__(self, key):
    """ Indexes directly if key is an int, or via the conversion dict if it's a string. """
    if type(key) == int:
      return self.data[key]
    elif type(key) == str:
      return self.data[self.conversion[key]]
    else:
      raise ValueError("Register must be accessed at an integer or a keyword string. Invalid key: {0}".format(key))

  def __setitem__(self, key, value):
    """ Indexes directly if key is an int, or via the conversion dict if it's a string. """
    if type(key) == int:
      self.data[key] = value
    elif type(key) == str:
      self.data[self.conversion[key]] = value
    else:
      raise ValueError("Register must be accessed at an integer or a keyword string. Invalid key: {0}".format(key))


if __name__ == "__main__":
  regs = Registers("MIPS")
  print(regs[8])
  regs[8] += 1
  print(regs["$t0"])

from modes import mode_dict


class Registers(object):
  def __init__(self, mode = "MIPS"):
    if mode.upper() in mode_dict:
      self.conversion = mode_dict[mode.upper()]
    else:
      raise ValueError("Assembler mode must be one of the following: {0}. Invalid mode: {1}".format(", ".join(mode_dict.keys()), mode))
    self.data = [0] * (max(self.conversion.values()) + 1)

  def __str__(self):
    return "\n".join(str(d) for d in self.data)

  def __getitem__(self, key):
    if type(key) == int:
      return self.data[key]
    elif type(key) == str:
      return self.data[self.conversion[key]]
    else:
      raise ValueError("Register must be accessed at an integer or a keyword string. Invalid key: {0}".format(key))

  def __setitem__(self, key, value):
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

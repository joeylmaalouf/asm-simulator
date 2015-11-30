from modes import mode_dict


class Registers(object):
  def __init__(self, mode = "MIPS"):
    #Converts input mode to upper case so it can work with the program regardless of caps
    if mode.upper() in mode_dict:
      self.conversion = mode_dict[mode.upper()]
    else:
      #If the mode isn't spelled correctly or isn't supported, returns an error containing the invalid string and the usable strings
      raise ValueError("Assembler mode must be one of the following: {0}. Invalid mode: {1}".format(", ".join(mode_dict.keys()), mode))
    #Takes the max registers of the specified mode and creates a list with their length made up of zeroes
    self.data = [0] * (max(self.conversion.values()) + 1)

  def __str__(self):
    #Puts each register value on its own line
    return "\n".join(str(d) for d in self.data)

  def __getitem__(self, key):
    #Checks to see if the key is an integer and passes it through if it is
    if type(key) == int:
      return self.data[key]
    #If the key is a string, it is converted into the int value and passed
    elif type(key) == str:
      return self.data[self.conversion[key]]
    #If it fits neither, returns an error detailing the incorrect input
    else:
      raise ValueError("Register must be accessed at an integer or a keyword string. Invalid key: {0}".format(key))

  def __setitem__(self, key, value):
    #If the key (register) is an int, sets the data to the key (register) immediately)
    if type(key) == int:
      self.data[key] = value
    #If the key is a string, convert it then set the data to the correct key 
    elif type(key) == str:
      self.data[self.conversion[key]] = value
    #If the key is not recognized, return an error detailing the problem
    else:
      raise ValueError("Register must be accessed at an integer or a keyword string. Invalid key: {0}".format(key))


if __name__ == "__main__":
  regs = Registers("MIPS")
  print(regs[8])
  regs[8] += 1
  print(regs["$t0"])

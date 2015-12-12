from utils import getval


class Memory(object):
  """ The memory object that stores our data. """
  def __init__(self, offset = "0xFFFF"):
    super(Memory, self).__init__()
    self.data = {}
    self.labels = {}
    try:              self.offset = int(offset, 16)
    except TypeError: self.offset = offset

  def __str__(self):
    """ String representation of the memory. """
    return str(self.data)

  def __getitem__(self, key):
    """ Getter for internal values. """
    try:             return self.data[key]
    except KeyError: raise ValueError("No stored value found in memory at the following address: {0}".format(key))

  def __setitem__(self, key, value):
    """ Setter for internal values. """
    self.data[key] = value

  def insert(self, line):
    """ Parse the given data line and insert its values in our memory. """
    name, dtype, values = line.split(None, 2)
    name, dtype, values = name[:-1], dtype[1:].lower(), [v.strip() for v in values.split(",")]
    if dtype not in ["ascii", "asciiz", "byte", "halfword", "word", "space"]:
      raise ValueError("Invalid data type: {0}".format(dtype))
    self.labels[name] = self.offset
    if dtype == "space":
      self.offset += getval(values[0], True)
    else:
      for value in values:
        self[self.offset] = value if "ascii" in dtype else getval(value, True)
        self.offset += 1


if __name__ == "__main__":
  mem = Memory()
  mem.insert("values: .byte 0x01, 0x02")
  mem.insert("empty: .space 0x04")
  mem.insert("strings: .ascii hello, world, hello world")
  print(mem)
  print(mem.labels)

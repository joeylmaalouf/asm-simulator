class Memory(object):
  """ An instruction that consists of an operation and 0-3 operands. """
  def __init__(self):
    super(Memory, self).__init__()
    self.data = {}

  def __str__(self):
    """ String representation of the memory. """
    return self.data.__str__()

  def __getitem__(self, key):
    """ Getter for internal values. """
    return self.data[key]

  def __setitem__(self, key, value):
    """ Setter for internal values. """
    self.data[key] = value

  def insert(self, line):
    """"""
    print(line)


if __name__ == "__main__":
  mem = Memory()

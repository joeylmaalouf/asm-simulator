class Instruction(object):
  """ An instruction that consists of an operation, an output, and 0-2 inputs. """
  def __init__(self, text):
    super(Instruction, self).__init__()
    self.raw = text
    words = text.replace(",", "").split()
    self.operation = words[0]
    self.output = words[1] if len(words) > 1 else None
    self.input0 = words[2] if len(words) > 2 else None
    self.input1 = words[3] if len(words) > 3 else None

  def __str__(self):
    """ String representation of the instruction. """
    return "{0} {1}".format(self.operation, ", ".join([v for v in [self.output, self.input0, self.input1] if v is not None]))

  def run(self, registers):
    """ Execute the instruction on the given registers. """
    # TODO
    return self


if __name__ == "__main__":
  instr = Instruction("addu $t2, $t0, $t1")
  print(instr.raw)
  print(instr.operation, instr.output, instr.input0, instr.input1)

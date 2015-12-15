class Instruction(object):
  """ An instruction that consists of an operation and 0-3 operands. """
  def __init__(self, text):
    super(Instruction, self).__init__()
    self.raw = text
    words = text.lower().replace(",", "").split()
    self.operation = words[0]
    self.operand0 = words[1] if len(words) > 1 else None
    self.operand1 = words[2] if len(words) > 2 else None
    self.operand2 = words[3] if len(words) > 3 else None

  def __str__(self):
    """ String representation of the instruction. """
    return "{0} {1}".format(self.operation, ", ".join([v for v in [self.operand0, self.operand1, self.operand2] if v is not None]))

  def update(self, operation, operand0, operand1, operand2):
    """ Update the instruction's attributes all at once. """
    self.operation = operation
    self.operand0 = operand0
    self.operand1 = operand1
    self.operand2 = operand2


if __name__ == "__main__":
  instr = Instruction("addu $t2, $t0, $t1")
  print(instr.raw)
  print(instr.operation, instr.operand0, instr.operand1, instr.operand2)

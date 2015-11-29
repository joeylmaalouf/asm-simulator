class Instruction(object):
  def __init__(self, text):
    super(Instruction, self).__init__()
    self.raw = text
    words = text.replace(",", "").split()
    if len(words) < 2:
      raise ValueError("Instruction must have at least two components. Invalid instruction: {0}".format(text))
    self.operation = words[0]
    self.output = words[1]
    self.input1 = words[2] if len(words) > 2 else None
    self.input2 = words[3] if len(words) > 3 else None

  def __str__(self):
    return self.raw

  def run(self, registers):
    pass


if __name__ == "__main__":
  instr = Instruction("addu $t2, $t0, $t1")
  print(instr.raw)
  print(instr.operation, instr.output, instr.input1, instr.input2)

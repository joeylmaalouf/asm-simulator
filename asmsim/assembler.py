from preprocessor import preprocess, normalize
from instruction import Instruction
from registers import Registers


class Assembler(object):
  """ The actual assembler, which takes an assembly program and simulates it. """
  def __init__(self, program, mode = "MIPS"):
    super(Assembler, self).__init__()
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    try:                   program_text = program.read()
    except AttributeError: program_text = program
    program_text = preprocess(program_text, self.mode)
    program_text = normalize(program_text, self.mode)
    self.instructions = [Instruction(line) for line in program_text.split("\n") if line.strip()]

  def __str__(self):
    """ String representation of the assembler. """
    return "{0} Assembler".format(self.mode)

  def run(self):
    """ Execute the program's instructions, modifying the given registers. """
    for instr in self.instructions:
      instr.run(self.registers)
    return self

  def display(self):
    """ Print the assembler mode and its register values. """
    print("{0}\nRegister Values:\n{1}".format(self, self.registers))
    return self


if __name__ == "__main__":
  asm = Assembler("li $t0, 1\nli $t1, 0x3BF20", "MIPS")
  asm.run()
  asm.display()

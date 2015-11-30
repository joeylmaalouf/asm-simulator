from registers import Registers
from instruction import Instruction


class Assembler(object):
  """ The actual assembler, which takes an assembly program and simulates it. """
  def __init__(self, program, mode = "MIPS"):
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    try:                   instruction_text = program.read()
    except AttributeError: instruction_text = program
    self.instructions = [Instruction(line) for line in instruction_text.split("\n") if line.strip()]
    self.preprocess()
    self.normalize()

  def __str__(self):
    """ String representation of the assembler. """
    return "{0} Assembler".format(self.mode)

  def preprocess(self):
    """ Goes through our instruction list and replaces
    pseudo-instructions with actual instructions. """
    # TODO
    return self

  def normalize(self):
    """ Converts instructions from a specific assembly language to our common
    instruction set, so we don't have to process instruction logic based on mode. """
    # TODO
    return self

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
  asm = Assembler("li $t0, 1\nli $t1, 2", "ARM")
  asm.run()
  asm.display()

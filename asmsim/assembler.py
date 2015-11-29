from registers import Registers
from instruction import Instruction


class Assembler(object):
  def __init__(self, program, mode = "MIPS"):
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    try:
      instruction_text = program.read()
    except AttributeError:
      instruction_text = program
    self.instructions = [Instruction(line) for line in instruction_text.split("\n") if line.strip()]

  def __str__(self):
    return "{0} Assembler".format(self.mode)

  def run(self):
    for instr in self.instructions:
      instr.run(self.registers)
    return self

  def display(self):
    print("{0}\nRegister Values:\n{1}".format(self, self.registers))
    return self


if __name__ == "__main__":
  asm = Assembler("li $t0, 1\nli $t1, 2", "ARM")
  asm.run()
  asm.display()

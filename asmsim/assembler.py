from registers import Registers
from instruction import Instruction


class Assembler(object):
  """ The actual assembler, which takes an assembly program and simulates it. """
  def __init__(self, program, mode = "MIPS"):
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    try:                   program_text = program.read()
    except AttributeError: program_text = program
    program_text = self.preprocess(program_text)
    program_text = self.normalize(program_text)
    self.instructions = [Instruction(line) for line in program_text.split("\n") if line.strip()]

  def __str__(self):
    """ String representation of the assembler. """
    return "{0} Assembler".format(self.mode)

  def preprocess(self, program_text):
    """ Goes through our instruction list and replaces
    pseudo-instructions with actual instructions. """
    processed = []
    for line in program_text.split("\n"):
      if line.strip():
        instr = Instruction(line)
        if self.mode == "MIPS":
          if instr.operation == "mov":
            instr.operation = "add"
            instr.input1 = "$zero"
          elif instr.operation == "li":
            val = int(instr.input0, 16)
            if val < 65536:
              instr.operation, instr.input0, instr.input1 = "addi", "$zero", instr.input0
            else:
              instr.operation, instr.input0, = "lui", hex(int(bin(val)[:-16], 2))
              processed.append(str(instr))
              instr.operation, instr.input0, instr.input1 = "ori", instr.output, hex(int(bin(val)[-16:], 2))
          # elif instr.operation == ...
          processed.append(str(instr))
        elif self.mode == "ARM":
          pass
    # TODO
    return "\n".join(processed)

  def normalize(self, program_text):
    """ Converts instructions from a specific assembly language to our common
    instruction set, so we don't have to process instruction logic based on mode. """
    # TODO
    return program_text

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

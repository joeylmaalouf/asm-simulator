from instruction import Instruction
from preprocessor import label_positions, normalize, preprocess
from registers import Registers
from utils import twoscomp


class Assembler(object):
  """ The actual assembler, which takes an assembly program and simulates it. """
  def __init__(self, program, mode = "MIPS"):
    super(Assembler, self).__init__()
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    try:                   program_text = program.read()
    except AttributeError: program_text = program
    program_text = preprocess(program_text, self.mode)
    self.labels = label_positions(program_text)
    program_text = normalize(program_text, self.mode)
    self.instructions = [Instruction(line) for line in program_text.split("\n") if line.strip()]

  def __str__(self):
    """ String representation of the assembler. """
    return "{0} Assembler".format(self.mode)

  def run(self):
    """ Execute the program's instructions, modifying the given registers. """
    cur_line = 0
    while cur_line < len(self.instructions):
      instr = self.instructions[cur_line]
      if cur_line in self.labels.values(): pass
      elif instr.operation in ["add", "addu"]:   self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
      elif instr.operation in ["addi", "addiu"]: self.registers[instr.operand0] = self.registers[instr.operand1] + twoscomp(instr.operand2)
      elif instr.operation == "and":             self.registers[instr.operand0] = self.registers[instr.operand1] & self.registers[instr.operand2]
      elif instr.operation == "andi":            self.registers[instr.operand0] = self.registers[instr.operand1] & twoscomp(instr.operand2)
      elif instr.operation == "beq":
        if self.registers[instr.operand0] == self.registers[instr.operand1]:
          cur_line = self.labels[instr.operand2]
      elif instr.operation == "bne":
        if self.registers[instr.operand0] != self.registers[instr.operand1]:
          cur_line = self.labels[instr.operand2]
      # TODO
      else: raise ValueError("Unrecognized instruction: {0}".format(instr.operation))
      cur_line += 1
    return self

  def display(self):
    """ Print the assembler mode and its register values. """
    print("{0}\nRegister Values:\n{1}".format(self, self.registers))
    return self


if __name__ == "__main__":
  asm = Assembler("li $t1, 0x5\nadder:\naddi $t0, $t0, 0x1\nbne $t0, $t1, adder\nend:", "MIPS")
  asm.run()
  asm.display()

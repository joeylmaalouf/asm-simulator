from instruction import Instruction
from preprocessor import label_positions, normalize, preprocess
from registers import Registers
from utils import getval


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
    HI, LO = 0, 0
    cur_line = 0
    while cur_line < len(self.instructions):
      instr = self.instructions[cur_line]
      if cur_line in self.labels.values(): pass
      elif instr.operation in ["add", "addu"]:
        self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
      elif instr.operation == "addi":
        self.registers[instr.operand0] = self.registers[instr.operand1] + getval(instr.operand2, True)
      elif instr.operation == "addiu":
        self.registers[instr.operand0] = self.registers[instr.operand1] + getval(instr.operand2, False)
      elif instr.operation == "and":
        self.registers[instr.operand0] = self.registers[instr.operand1] & self.registers[instr.operand2]
      elif instr.operation == "andi":
        self.registers[instr.operand0] = self.registers[instr.operand1] & getval(instr.operand2, False)
      elif instr.operation == "beq":
        if self.registers[instr.operand0] == self.registers[instr.operand1]:
          cur_line = self.labels[instr.operand2] # jump straight to the label rather than the following instruction because we increment the line counter at the end anyway
      elif instr.operation == "bgez":
        if self.registers[instr.operand0] >= 0:
          cur_line = self.labels[instr.operand1]
      elif instr.operation == "bgezal":
        if self.registers[instr.operand0] >= 0:
          self.registers[31] = cur_line + 1
          cur_line = self.labels[instr.operand1]
      # already in preprocessor
      # elif instr.operation == "bgtz":
      #   if self.registers[instr.operand0] > 0:
      #     cur_line = self.labels[instr.operand1]
      # already in preprocessor
      # elif instr.operation == "blez":
      #   if self.registers[instr.operand0] <= 0:
      #     cur_line = self.labels[instr.operand1]
      elif instr.operation == "bltz":
        if self.registers[instr.operand0] < 0:
          cur_line = self.labels[instr.operand1]
      elif instr.operation == "bltzal":
        if self.registers[instr.operand0] < 0:
          self.registers[31] = cur_line + 1
          cur_line = self.labels[instr.operand1]
      elif instr.operation == "bne":
        if self.registers[instr.operand0] != self.registers[instr.operand1]:
          cur_line = self.labels[instr.operand2]
      elif instr.operation in ["div", "divu"]:
        LO = self.registers[instr.operand0] // self.registers[instr.operand1]
        HI = self.registers[instr.operand0] % self.registers[instr.operand1]
      elif instr.operation == "j":
        cur_line = self.labels[instr.operand0]
      elif instr.operation == "jal":
        self.registers[31] = cur_line + 1
        cur_line = self.labels[instr.operand0]
      elif instr.operation == "jr":
        cur_line = self.registers[instr.operand0]
      elif instr.operation == "lb":
        pass # TODO
      elif instr.operation == "lui":
        pass # TODO
      elif instr.operation == "lw":
        pass # TODO
      elif instr.operation == "mfhi":
        self.registers[instr.operand0] = HI
      elif instr.operation == "mflo":
        self.registers[instr.operand0] = LO
      elif instr.operation in ["mult", "multu"]:
        LO = self.registers[instr.operand0] * self.registers[instr.operand1]
      elif instr.operation == "nor":
        self.registers[instr.operand0] = ~(self.registers[instr.operand1] | self.registers[instr.operand2]) & 0b11111111111111111111111111111111
      elif instr.operation == "or":
        self.registers[instr.operand0] = self.registers[instr.operand1] | self.registers[instr.operand2]
      elif instr.operation == "ori":
        self.registers[instr.operand0] = self.registers[instr.operand1] | getval(instr.operand2, False)
      elif instr.operation == "sb":
        pass # TODO
      elif instr.operation in ["slt", "sltu"]:
        pass # TODO
      elif instr.operation in ["slti", "sltiu"]:
        pass # TODO
     elif instr.operation == "sll":
        self.registers[instr.operand0] = self.registers[instr.operand1] << getval(instr.operand2, False)
     elif instr.operation == "sllv":
	      self.registers[instr.operand0] = self.registers[instr.operand1] << self.registers[instr.operand2]
     elif instr.operation == "sra":
        self.registers[instr.operand0] = self.registers[instr.operand1] >> getval(instr.operand2, True)
     elif instr.operation == "srl":
        self.registers[instr.operand0] = self.registers[instr.operand1] >> getval(instr.operand2, False)
     elif instr.operation == "srlv":
	      self.registers[instr.operand0] = self.registers[instr.operand1] >> self.registers[instr.operand2]
      elif instr.operation in ["sub", "subu"]:
        self.registers[instr.operand0] = self.registers[instr.operand1] - self.registers[instr.operand2]
      elif instr.operation == "sw":
        pass # TODO
      elif instr.operation == "syscall":
        if v0 == 1:
          print a0
        elif v0 in [2, 3]:
    	  print fl2
  	elif v0 == 4:
    	  print a0
  	elif v0 == 5:
          pass
  	elif v0 == 6:
    	  pass
  	elif v0 == 7:
    	  pass
  	elif v0 == 8:
    	  pass
  	elif v0 == 9:
    	  pass
  	elif v0 == 10:
    	  pass
  	elif v0 == 11:
    	  pass
  	elif v0 == 12:
    	  pass
  	elif v0 == 13:
    	  pass
  	elif v0 == 14:
    	  pass
  	elif v0 == 15:
    	  pass
  	elif v0 == 16:
    	  pass
  	elif v0 == 17:
    	  pass
  	elif v0 == 30:
    	  pass
  	elif v0 == 31:
    	  pass
  	elif v0 == 32:
    	  pass
  	elif v0 == 33:
    	  pass
  	elif v0 == 34:
    	  pass
  	elif v0 == 35:
    	  pass
  	elif v0 == 36:
    	  pass
  	elif v0 in [37, 38, 39, 45, 46, 47, 48, 49]:
    	  pass
  	elif v0 == 40:
    	  pass
  	elif v0 == 41:
    	  pass
  	elif v0 == 42:
	  pass
  	elif v0 == 43:
    	  pass
  	elif v0 == 44:
    	  pass
  	elif v0 == 50:
    	  pass
  	elif v0 == 51:
    	  pass
  	elif v0 == 52:
    	  pass
  	elif v0 == 53:
    	  pass
  	elif v0 == 54:
    	  pass
	elif v0 == 55:
    	  pass
  	elif v0 == 56:
    	  pass
  	elif v0 == 57:
    	  pass
  	elif v0 == 58:
    	  pass
  	elif v0 == 59:
    	  pass
      elif instr.operation == "xor":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ self.registers[instr.operand2]
      elif instr.operation == "xori":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ getval(instr.operand2, False)
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

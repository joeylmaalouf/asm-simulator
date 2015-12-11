from instruction import Instruction
from preprocessor import label_positions, normalize, preprocess
from registers import Registers
from utils import getval, parseaddress, syscall


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
    if self.mode == "MIPS":
      return self.runMIPS()
    elif self.mode == "ARM":
      return self.runARM()
    else:
      raise ValueError("Invalid mode: {0}".format(self.mode))

  def runMIPS(self):
    """ Execute the program using the MIPS instruction set. """
    HI, LO = 0, 0
    cur_line = 0
    memory = {}
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
        register, offset = parseaddress(instr.operand1)
        address = self.registers[register] if register in self.registers else getval(register, False)
        self.registers[instr.operand0] = memory[address + getval(offset, True)]
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
        self.registers[instr.operand0] = ~(self.registers[instr.operand1] | self.registers[instr.operand2]) & 0xFFFFFFFF
      elif instr.operation == "or":
        self.registers[instr.operand0] = self.registers[instr.operand1] | self.registers[instr.operand2]
      elif instr.operation == "ori":
        self.registers[instr.operand0] = self.registers[instr.operand1] | getval(instr.operand2, False)
      elif instr.operation == "sb":
        register, offset = parseaddress(instr.operand1)
        address = self.registers[register] if register in self.registers else getval(register, False)
        memory[address + getval(offset, True)] = self.registers[instr.operand0] & 0xFF
      elif instr.operation in ["slt", "sltu"]:
        if self.registers[instr.operand1] < self.registers[instr.operand2]:
          self.registers[instr.operand0] = 1
      elif instr.operation in ["slti", "sltiu"]:
        if self.registers[instr.operand1] < getval(instr.operand2, False):
          self.registers[instr.operand0] = 1
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
        register, offset = parseaddress(instr.operand1)
        address = self.registers[register] if register in self.registers else getval(register, False)
        memory[address + getval(offset, True)] = self.registers[instr.operand0]
      elif instr.operation == "syscall":
         retval = syscall(self.registers[2])
         if retval: break
      elif instr.operation == "xor":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ self.registers[instr.operand2]
      elif instr.operation == "xori":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ getval(instr.operand2, False)
      else: raise ValueError("Unrecognized instruction: {0}".format(instr.operation))
      cur_line += 1
    return self
  
  def runARM(self):
    """ Execute the program using the ARM instruction set. """
    if instr.operation == "add":
      self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
    elif instr.operation == "addeq":
      if zero:
        self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
    elif instr.operation == "adds":
      self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
      #also sets conditional flags?
  
  
  def display(self):
    """ Print the assembler mode and its register values. """
    print("{0}\nRegister Values:\n{1}".format(self, self.registers))
    return self


if __name__ == "__main__":
  program = """
  li $t1, 0x5
  adder:
  addi $t0, $t0, 0x1
  bne $t0, $t1, adder
  end:
  sb $t1, A
  lb $t2, A
  """
  asm = Assembler(program, "MIPS")
  asm.run()
  asm.display()

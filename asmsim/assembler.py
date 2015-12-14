from instruction import Instruction
from memory import Memory
from preprocessor import clean, label_positions, preprocess, split_sections
from registers import Registers
from utils import calcval, getval, parseaddress, syscall


class Assembler(object):
  """ The actual assembler, which takes an assembly program and simulates it. """
  def __init__(self, program, mode = "MIPS"):
    super(Assembler, self).__init__()
    try:                   text = program.read()
    except AttributeError: text = program
    self.mode = mode.upper()
    self.registers = Registers(self.mode)
    lines = text.split("\n")
    lines = clean(lines)
    instrs, data = split_sections(lines)
    self.memory = Memory()
    for d in data: self.memory.insert(d)
    instrs = preprocess(instrs, self.mode)
    self.labels = label_positions(instrs)
    self.instructions = [Instruction(instr) for instr in instrs]

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
      elif instr.operation == "la":
        self.registers[instr.operand0] = self.memory.labels[instr.operand1]
      elif instr.operation in ["lb", "lw"]:
        outside, inside = parseaddress(instr.operand1)
        address = calcval(outside, self) + calcval(inside, self)
        self.registers[instr.operand0] = self.memory[address]
      elif instr.operation == "lui":
        self.registers[instr.operand0] = getval(instr.operand1, False) << 16
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
        outside, inside = parseaddress(instr.operand1)
        address = calcval(outside, self) + calcval(inside, self)
        self.memory[address] = self.registers[instr.operand0] & 0xFF
      elif instr.operation in ["slt", "sltu"]:
        self.registers[instr.operand0] = int(self.registers[instr.operand1] < self.registers[instr.operand2])
      elif instr.operation == "slti":
        self.registers[instr.operand0] = int(self.registers[instr.operand1] < getval(instr.operand2, True))
      elif instr.operation == "sltiu":
        self.registers[instr.operand0] = int(self.registers[instr.operand1] < getval(instr.operand2, False))
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
        outside, inside = parseaddress(instr.operand1)
        address = calcval(outside, self) + calcval(inside, self)
        self.memory[address] = self.registers[instr.operand0]
      elif instr.operation == "syscall":
         retval = syscall(self.registers[2])
         if retval: break
      elif instr.operation == "xor":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ self.registers[instr.operand2]
      elif instr.operation == "xori":
        self.registers[instr.operand0] = self.registers[instr.operand1] ^ getval(instr.operand2, False)
      elif instr.operation == "break":
        break
      else: raise ValueError("Unrecognized instruction: {0}".format(instr.operation))
      cur_line += 1
    return self
  
  def runARM(self):
    """ Execute the program using the ARM instruction set. """
    #Arithmetic
    if "eq" in instr.operation: #execute only if zero flag is set
      if "add" in instr.operation:
        self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
      pass
    #elif "s" in instr.operation:
      pass
    elif "ne" in instr.operation:
      pass
    elif "cs" in instr.operation or "hs" in instr.operation:
      pass 
    elif "cc" in instr.operation or "lo" in instr.operation:
      pass
    elif "mi" in instr.operation:
      pass
    elif "pl" in instr.operation:
      pass
    elif "vs" in instr.operation:
      pass
    elif "vc" in instr.operation:
      pass
    elif "hi" in instr.operation:
      pass
    elif "ls" in instr.operation:
      pass
    elif "ge" in instr.operation:
      pass
    elif "lt" in instr.operation:
      pass
    elif "gt" in instr.operation:
      pass
    elif "le" in instr.operation:
      pass
      #self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2]
    elif instr.operation == "adc":
      self.registers[instr.operand0] = self.registers[instr.operand1] + self.registers[instr.operand2] + carry #look into what carry actually is
    elif instr.operation == "sub":
      self.registers[instr.operand0] = self.registers[instr.operand1] - self.registers[instr.operand2]
    elif instr.operation == "sbc":
      self.registers[instr.operand0] = self.registers[instr.operand1] - self.registers[instr.operand2] + (carry-1)
    elif instr.operation == "rsb":
      self.registers[instr.operand0] = self.registers[instr.operand2] - self.registers[instr.operand1]
    elif instr.operation == "rsc":
      self.registers[instr.operand0] = self.registers[instr.operand2] - self.registers[instr.operand1] + (carry-1)
    #Branch
    elif instr.operation == "b":
      cur_line = self.labels[instr.operand0]
    elif instr.operation == "bl":
      self.registers[15] = cur_line + 1    
    #Comparisons
    #Logical Operations
    #Data Movement



if __name__ == "__main__":
  program = """
  li $t1, 5
  addloop:
  addi $t0, $t0, 1
  bne $t0, $t1, addloop
  endloop:
  sb $t1, A
  lb $t2, A
  """
  asm = Assembler(program, "MIPS")
  asm.run()
  print(asm.registers["$t0"], asm.registers["$t1"], asm.registers["$t2"])

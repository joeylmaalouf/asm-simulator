if __name__ == "__main__":
  from asmsim.assembler import Assembler
  a = Assembler(open("example.asm", "r"), "MIPS").run()
  # print(a.registers["$t0"], a.registers["$t1"], a.registers["$t2"])
  offset = a.memory.labels["arr"]
  print(a.memory[offset], a.memory[offset+1], a.memory[offset+2], a.memory[offset+3])

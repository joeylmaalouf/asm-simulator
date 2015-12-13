if __name__ == "__main__":
  from asmsim.assembler import Assembler
  a = Assembler(open("example.asm", "r"), "MIPS")
  offset = a.memory.labels["arr"]
  print(a.memory[offset], a.memory[offset+1], a.memory[offset+2], a.memory[offset+3])
  a.run()
  print(a.memory[offset], a.memory[offset+1], a.memory[offset+2], a.memory[offset+3])

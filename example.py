if __name__ == "__main__":
  from asmsim.assembler import Assembler
  Assembler(open("example.asm", "r"), "MIPS").run().display()

from instruction import Instruction


""" Get a hex string of the upper 16 bits in a 32 bit number. """
upper = lambda val: hex(int(bin(val)[:-16], 2))
""" Get a hex string of the lower 16 bits in a 32 bit number. """
lower = lambda val: hex(int(bin(val)[-16:], 2))


def preprocess(program_text, mode):
  """ Goes through our instruction list and replaces
  pseudo-instructions with actual instructions. """
  processed = []
  for line in program_text.split("\n"):
    if line.strip():
      instr = Instruction(line)
      if mode == "MIPS":
        if instr.operation == "noop":
          instr.operation = "sll"
          instr.output = "$zero"
          instr.input0 = "$zero"
          instr.input1 = "0x0"
        elif instr.operation == "mov":
          instr.operation = "add"
          instr.input1 = "$zero"
        elif instr.operation == "clear":
          instr.operation = "add"
          instr.input0 = "$zero"
          instr.input1 = "$zero"
        elif instr.operation == "not":
          instr.operation = "nor"
          instr.input1 = "$zero"
        elif instr.operation == "li":
          val = int(instr.input0, 16)
          if val < 65536:
            instr.operation, instr.input0, instr.input1 = "addi", "$zero", instr.input0
          else:
            instr.operation, instr.input0, = "lui", upper(val)
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "ori", instr.output, lower(val)
        # elif instr.operation == ...
          # ...
        processed.append(str(instr))
      elif mode == "ARM":
        pass
  # TODO
  return "\n".join(processed)


def normalize(program_text, mode):
  """ Converts instructions from a specific assembly language to our common
  instruction set, so we don't have to process instruction logic based on mode. """
  # TODO
  return program_text


if __name__ == "__main__":
  print preprocess("noop\nli $t0, 1\nli $t1, 0x3BF20\nmov $t2, $t1", "MIPS")

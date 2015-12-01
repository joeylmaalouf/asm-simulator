from instruction import Instruction


""" Get a hex string of the upper 16 bits in a 32 bit number. """
upper = lambda val: hex(int(bin(val)[:-16], 2))
""" Get a hex string of the lower 16 bits in a 32 bit number. """
lower = lambda val: hex(int(bin(val)[-16:], 2))


def preprocess(program_text, mode):
  """ Goes through our instruction list and replaces any
  pseudo-instructions with actual instructions. Differs
  from the standard MIPS assembler in that we keep register
  keywords ($zero instead of converting to $0) and that we
  don't change all numbers to decimal. """
  processed = []
  for line in program_text.split("\n"):
    if line.strip():
      instr = Instruction(line)

      if mode == "MIPS":
        if instr.operation == "noop":
          instr.update("sll", "$zero", "$zero", "0x0")
        elif instr.operation == "mov":
          instr.update("add", instr.operand0, instr.operand1, "$zero")
        elif instr.operation == "clear":
          instr.update("add", instr.operand0, "$zero", "$zero")
        elif instr.operation == "not":
          instr.update("nor", instr.operand0, instr.operand1, "$zero")
        elif instr.operation == "la" or instr.operation == "li":
          val = int(instr.operand1, 16)
          if val < 65536:
            instr.update("addiu", instr.operand0, "$zero", instr.operand1)
          else:
            instr.update("lui", instr.operand0, upper(val), instr.operand2)
            processed.append(str(instr))
            instr.update("ori", instr.operand0, instr.operand0, lower(val))
        elif instr.operation == "mul":
          tmp = instr.operand0
          instr.update("mult", instr.operand1, instr.operand2, None)
          processed.append(str(instr))
          instr.update("mflo", tmp, None, None)
        elif instr.operation == "div" or instr.operation == "rem": # add bne and break, like MARS, to check for no div by 0?
          tmp0 = instr.operand0
          tmp1 = instr.operation == "rem"
          instr.update("div", instr.operand1, instr.operand2, None)
          processed.append(str(instr))
          instr.update(["mflo", "mfhi"][int(tmp1)], tmp0, None, None)
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
  example = "li $t1, 5\nli $t2, 0x3BF20\n"
  print(example)
  print(preprocess(example, "MIPS"))

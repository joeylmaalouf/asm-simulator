from instruction import Instruction
from utils import num_lower, num_upper


def clean(lines, mode):
  """ Strips extra whitespace and remove comments. """
  comment_char = {"MIPS": "#", "ARM": "@"}[mode]
  cleaned = []
  for line in lines:
    l = line.strip().split(comment_char)[0].strip()
    if l: cleaned.append(l)
  return cleaned


def split_sections(lines):
  """ Split the text and data sections of the code. """
  if ".text" not in [l.lower() for l in lines] and ".data" not in [l.lower() for l in lines]:
    return lines, [] # they didn't specify sections, so we assume it's all text
  text, data = [], []
  in_text, in_data = False, False
  for line in lines:
    if line[0] == ".":
      if   line.lower() == ".text": in_text, in_data = True, False
      elif line.lower() == ".data": in_text, in_data = False, True
      else: raise ValueError("Invalid section header (must be .text or .data): {0}".format(line))
    elif in_text: text.append(line)
    elif in_data: data.append(line)
  return text, data


def preprocess(lines, mode):
  """ Go through our instruction list and replaces any
  pseudo-instructions with actual instructions. Differs
  from the standard MIPS assembler in that we keep register
  keywords ($zero instead of converting to $0) and that we
  don't change all numbers to decimal (we assume hex). """
  processed = []
  for line in lines:
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
      elif instr.operation == "li":
        val = int(instr.operand1, 16)
        if val < 65536:
          instr.update("addiu", instr.operand0, "$zero", instr.operand1)
        else:
          instr.update("lui", instr.operand0, num_upper(val), instr.operand2)
          processed.append(str(instr))
          instr.update("ori", instr.operand0, instr.operand0, num_lower(val))
      elif instr.operation == "bge":
        label = instr.operand2
        instr.update("slt", "$at", instr.operand0, instr.operand1)
        processed.append(str(instr))
        instr.update("beq", instr.operand0, "$zero", label)
      elif instr.operation == "bgt":
        label = instr.operand2
        instr.update("slt", "$at", instr.operand1, instr.operand0)
        processed.append(str(instr))
        instr.update("bne", instr.operand0, "$zero", label)
      elif instr.operation == "ble":
        label = instr.operand2
        instr.update("slt", "$at", instr.operand1, instr.operand0)
        processed.append(str(instr))
        instr.update("beq", instr.operand0, "$zero", label)
      elif instr.operation == "blt":
        label = instr.operand2
        instr.update("slt", "$at", instr.operand0, instr.operand1)
        processed.append(str(instr))
        instr.update("bne", instr.operand0, "$zero", label)
      elif instr.operation == "b":
        instr.update("beq", "$zero", "$zero", instr.operand0)
      elif instr.operation == "bal":
        instr.update("bgezal", "$zero", instr.operand0, instr.operand2)
      elif instr.operation == "blez":
        label = instr.operand1
        instr.update("slt", "$at", "$zero", instr.operand0)
        processed.append(str(instr))
        instr.update("beq", instr.operand0, instr.operand1, label)
      elif instr.operation == "bgtu":
        label = instr.operand2
        instr.update("sltu", "$at", instr.operand1, instr.operand0)
        processed.append(str(instr))
        instr.update("bne", instr.operand0, "$zero", label)
      elif instr.operation == "bgtz":
        label = instr.operand1
        instr.update("slt", "$at", "$zero", instr.operand0)
        processed.append(str(instr))
        instr.update("bne", instr.operand0, instr.operand1, label)
      elif instr.operation == "beqz":
        instr.update("beq", instr.operand0, "$zero", instr.operand1)
      elif instr.operation == "mul":
        output = instr.operand0
        instr.update("mult", instr.operand1, instr.operand2, None)
        processed.append(str(instr))
        instr.update("mflo", output, None, None)
      elif instr.operation == "div" or instr.operation == "rem": # add bne and break, like MARS, to check for no div by 0?
        output = instr.operand0
        isrem = instr.operation == "rem"
        instr.update("div", instr.operand1, instr.operand2, None)
        processed.append(str(instr))
        instr.update(["mflo", "mfhi"][int(isrem)], output, None, None)
      processed.append(str(instr))

    elif mode == "ARM":
      # TODO
      if instr.operation == "nop":
        instr.update("mov", "r0", "r0", None)
      processed.append(str(instr))

  return processed


def label_positions(lines):
  """ Create a dict of label positions for use in jumping and branching. """
  labels = {}
  cur_line = 0
  for line in lines:
    word = line.split(" ")[0]
    if word[-1] == ":":
      labels[word[:-1]] = cur_line
    cur_line += 1
  return labels


if __name__ == "__main__":
  example = ".data\nval: .byte 3\n\n.text\nmain:\n  li $t1, 5\n  li $t2, 0x3BF20\nend:\n".split("\n")
  print(example)
  print(clean(example, "MIPS"))
  print(split_sections(clean(example, "MIPS")))
  print(preprocess(clean(example, "MIPS"), "MIPS"))

  example = "nop\nadd r0, r1, #5".split("\n")
  print(example)
  print(preprocess(clean(example, "ARM"), "ARM"))

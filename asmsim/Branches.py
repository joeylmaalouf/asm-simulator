if self.mode == "MIPS":
          if instr.operation == "mov":
            instr.operation = "add"
            instr.input1 = "$zero"
          elif instr.operation == "li":
            val = int(instr.input0, 16)
            if val < 65536:
              instr.operation, instr.input0, instr.input1 = "addi", "$zero", instr.input0
            else:
              instr.operation, instr.input0, = "lui", hex(int(bin(val)[:-16], 2))
              processed.append(str(instr))
              instr.operation, instr.input0, instr.input1 = "ori", instr.output, hex(int(bin(val)[-16:], 2))
          # elif instr.operation == ...
          elif instr.operation == "bge":
            label = instr.input1
            instr.operation, instr.output, instr.input0, instr.input1 = "slt", "$at", instr.output, instr.input0
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "beq", "$zero", label
          elif instr.operation == "bgt":
            label = instr.input1
            instr.operation, instr.output, instr.input1 = "slt", "$at", instr.output
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "bne", "$zero", label
          elif instr.operation == "ble":
            label = instr.input1
            instr.operation, instr.output, instr.input1 = "slt", "$at", instr.output
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "beq", "$zero", label
          elif instr.operation == "blt":
            label = instr.input1
            instr.operation, instr.output, instr.input0, instr.input1 = "slt", "$at", instr.output, instr.input0
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "bne", "$zero", label
          elif instr.operation == "b":
            instr.operation, instr.output, instr.input0, instr.input1 = "beq", "$zero", "$zero", instr.output
          elif instr.operation == "bal":
            instr.operation, instr.output, instr.input0 = "bgezal", "$zero", instr.output
          elif instr.operation == "blez":
            label = instr.input0
            instr.operation, instr.output, instr.input0, instr.input1 = "slt", "$at", "$zero", instr.output
            processed.append(str(instr))
            instr.operation, instr.input1 = "beq", label
          elif instr.operation == "bgtu":
            label = instr.input1
            instr.operation, instr.output, inst.input1 = "sltu", "$at", instr.output
            processed.append(str(instr))
            instr.operation, instr.input0, instr.input1 = "bne", "$zero", label
          elif instr.operation == "bgtz":
            label = instr.input0
            instr.operation, instr.output, instr.input0, instr.input1 = "slt", "$at", "$zero", instr.output
            processed.append(str(instr))
            instr.operation, instr.input1 = "bne", label
          elif instr.operation == "beqz":
            instr.operation, instr.input0, instr.input1 = "beq", "$zero", instr.input0
          processed.append(str(instr))

        elif self.mode == "ARM":
          pass


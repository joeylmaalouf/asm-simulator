#Comparisons
elif instr.operation == "CMP":
	res = self.registers[instr.operand0] - self.registers[instr.operand1]
	pass #Update conditionals, O1-O2
elif instr.operation == "CMN":
	res = self.registers[instr.operand0] + self.registers[instr.operand1]
	pass #Update conditionals, O1+O2
elif instr.operation == "TST":
	res = self.registers[instr.operand0] & self.registers[instr.operand1]
	pass #Update conditionals, O1 AND O2
elif instr.operation == "TEQ":
	res = self.registers[instr.operand0] ^ self.registers[instr.operand1]
	pass #Update conditionals, O1 XOR

#Logical Operationsn
elif instr.operation == "AND":
	self.registers[instr.operand0] = self.registers[instr.operand1] & self.registers[instr.operand2]
elif instr.operation == "EOR":
	self.registers[instr.operand0] = self.registers[instr.operand1] ^ self.registers[instr.operand2]
elif instr.operation == "ORR":
	self.registers[instr.operand0] = self.registers[instr.operand1] | self.registers[instr.operand2]
elif instr.operation == "BIC":
	self.registers[instr.operand0] = self.registers[instr.operand1] & ~self.registers[instr.operand2]

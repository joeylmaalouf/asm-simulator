#Comparisons
elif instr.operation == "CMP":
	res = self.registers[instr.operand0] - self.registers[instr.operand1]
	n, z, c, v = 0,0,0,0
	if res < 0:
		n = 1
	if res == 0;
		z = 1 
	flags.Update(n,z,c,v)
elif instr.operation == "CMN":
	res = self.registers[instr.operand0] + self.registers[instr.operand1]
	n, z, c, v = 0,0,0,0
	if res < 0:
		n = 1
	if res == 0:
		z = 1 
	if 4294967295> res > 2147483647:
		c = 1
	if res > 4294967295:
		v = 1
	flags.Update(n,z,c,v)
elif instr.operation == "TST":
	res = self.registers[instr.operand0] & self.registers[instr.operand1]
	n, z, c, v = 0,0,0,0
	if res == 0:
		z = 1 
	flags.Update(n,z,c,v)
elif instr.operation == "TEQ":
	res = self.registers[instr.operand0] ^ self.registers[instr.operand1]
	n, z, c, v = 0,0,0,0
	if res == 0:
		z = 1 
	flags.Update(n,z,c,v)

#Logical Operations
elif instr.operation == "AND":
	self.registers[instr.operand0] = self.registers[instr.operand1] & self.registers[instr.operand2]
elif instr.operation == "EOR":
	self.registers[instr.operand0] = self.registers[instr.operand1] ^ self.registers[instr.operand2]
elif instr.operation == "ORR":
	self.registers[instr.operand0] = self.registers[instr.operand1] | self.registers[instr.operand2]
elif instr.operation == "BIC":
	self.registers[instr.operand0] = self.registers[instr.operand1] & ~self.registers[instr.operand2]

#
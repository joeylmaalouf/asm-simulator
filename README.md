# asm-simulator
Assembly code simulation in Python. Done for Olin Computer Architecture, Fall 2015.


### Usage:
Assembly code in a separate file:
```python
if __name__ == "__main__":
  from asmsim.assembler import Assembler
  f = open("program.asm", "r")
  a = Assembler(f, "MIPS")
  a.run()
  print(a.registers["$t2"])
```

Assembly code in the program itself:
```python
if __name__ == "__main__":
  from asmsim.assembler import Assembler
  program = """
  li $t0, 2
  li $t1, 2
  add $t2, $t0, $t1
  """
  a = Assembler(program, "MIPS")
  a.run()
  print(a.registers["$t2"])
```

See `example.py` for more examples of Assembler usage.


### References:
* http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html
* https://en.wikipedia.org/wiki/MIPS_instruction_set#Pseudo_instructions
* http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/dataseg.html

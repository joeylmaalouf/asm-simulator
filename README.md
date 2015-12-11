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
  a.display()
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
  a.display()
```


### Why?
We wanted to learn more about assembly, especially how different asm languages/architectures parse and execute instructions.

### TODO:
* data memory for MIPS
* .data and .text section parsing for MIPS
* ARM

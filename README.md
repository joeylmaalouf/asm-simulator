# asm-simulator
MIPS assembly code simulation in Python.


### Usage:
Assembly code in a separate file:
```python
if __name__ == "__main__":
  from asmsim.assembler import Assembler
  f = open("program.asm", "r")
  a = Assembler(f, "MIPS")
  a.run()
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
```


### Why?
We were interested in better understanding assembly (pseudo-)instructions. Done for Olin Computer Architecture, Fall 2015.

### TODO:
* .data and .text section parsing for MIPS
* ARM

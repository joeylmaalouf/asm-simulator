# Python Assembly Simulator

### What did we do?
We created a python assembly simulator which can take in either MIPS or ARM instructions and return an output consistent with what would be expected from a lower level assembler. We process all of the instructions in a manner as close as feasible to the actual encoded actions, in terms of execution. The MIPS assembler includes parsing for pseudoinstructions, usable data memory, and all other operations with the expected registers. The ARM assembler contains parsing for the no operation pseudoinstruction only as well as all expected operations compatible with the appropriate registers. 

### Why did we do it?
We wanted to learn more about assembly, especially how different asm languages/architectures parse and execute instructions. We discovered a huge number of similarities, with some things being exactly the same. That being said, there were quite a few discrepancies as well. The modular and expandable nature of our code allowed us to reuse some parsing and register implementations across platforms, and paves the way for future additions if desired. Becuase Computer Architecture only has time to cover the MIPS implementation of assembly, this experience helped to highlight advantages and disadvantages that would have been missed had we assumed MIPS was all that was out there.

### How did we do it?

### How can someone else build on it?

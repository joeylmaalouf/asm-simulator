# Python Assembly Simulator

### What did we do?

We created a python program to run assembly instructions in ARM or MIPS architecture, simulating a system with either architectures. It can be given inputs of an iterable object, and will turn text into instructions to run. It also has a functioning data memory, which we have demonstrated with a program that can repeatedly double an array in data memory.

### Why did we do it?

We wanted to learn more about assembly, especially how different asm languages/architectures parse and execute instructions.

### How did we do it?

1. We started by creating a Register class, to simulate the registers that would hold values in a physical system. The Register class also allows us to easily specify which register we want to access in our program, either by name or number
2. Once we had registers, we also created an Instruction object, designed to parse each line of assembly code, and break it down into operands and operators, which refer to register locations and things to do to them.
3. Finally, we started inplimenting the assembler. The MIPS one was first, and simpler - it takes in the instruction, and has an operation ready for each different instruction, and common pseudo-instructions.
4. ARM was a bigger challenge, because each instruction has multiple versions based on conditional execution. We first analyze the instruction for all of the possible conditions, and evaluate those conditions. If the condition fails, we simply don't execute the instruction. If we do meet the conditional, the execution goes through. That allowes us to only wory about one implimentation of the execution of the instructions, instead of having to inpliment execution for every possible version of a more basic command.

### How can someone else build on it?



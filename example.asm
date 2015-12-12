# Looping program
# for (i = initial; i < final; i += increment){}

.data
initial: .byte 0x01 # the loop counter's starting value
increment: .byte 0x03 # the number by which we increment the counter
final: .byte 0x05 # the value at/after which to stop

.text
main:
  lw $t0, initial
  lw $t1, increment # could also do 1(initial) or initial(1); it's offset by 1 since it comes right after in data memory
  lw $t2, final
addloop:
  add $t0, $t0, $t1
  blt $t0, $t2, addloop
endloop:
# The end!

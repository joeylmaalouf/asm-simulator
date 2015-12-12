# Looping program
# for (i = initial; i < final; i += increment){}

.data
initial: .byte 0x00 # the loop counter's starting value
increment: .byte 0x01 # the number by which we increment the counter
final: .byte 0x05 # the value at which to stop

.text
main:
  li $t0, 0
  li $t1, 1
  li $t2, 5
addloop:
  add $t0, $t0, $t1
  blt $t0, $t2, addloop
endloop:
# The end!

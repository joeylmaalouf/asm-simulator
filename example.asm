# Array doubling program
# for (i = initial; i < final; i += increment){ arr[i] *= 2; }

.data
arr: .byte 0x01, 0x02, 0x04, 0x08 # the data to double
initial: .byte 0x00 # the loop counter's starting value
increment: .byte 0x01 # the number by which we increment the counter
final: .byte 0x04 # the value at/after which to stop

.text
main:
  lw $t0, initial
  lw $t1, increment
  lw $t2, final
loop:
  lw $t3, arr($t0)
  sll $t3, $t3, 1
  sw $t3, arr($t0)
  add $t0, $t0, $t1
  blt $t0, $t2, loop
end:
# The end!

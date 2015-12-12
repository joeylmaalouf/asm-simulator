# Looping program

.data
numiter: .byte 0x05 # the total number of iterations to go through

.text
main:
  li $t1, 5
addloop:
  addi $t0, $t0, 1
  bne $t0, $t1, addloop
endloop:
# The end!

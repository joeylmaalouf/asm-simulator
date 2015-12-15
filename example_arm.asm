@ this program sums the first n numbers, starting from 0
@ r0 is the counter
@ r1 is the number of values to sum
@ r2 is the result

main:
  add r1, r0, #5
loop:
  add r0, r0, #1 @ increment counter
  add r2, r2, r0 @ add counter to result
  cmp r1, r0     @ check if we need to exit
  bne loop
endloop:

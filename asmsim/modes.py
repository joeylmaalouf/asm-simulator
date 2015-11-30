# conversion dictionaries for strings that refer to registers

MIPS_registers = {
  "$zero": 0,
  "$at":   1,
  "$v0":   2,
  "$v1":   3,
  "$a0":   4,
  "$a1":   5,
  "$a2":   6,
  "$a3":   7,
  "$t0":   8,
  "$t1":   9,
  "$t2":  10,
  "$t3":  11,
  "$t4":  12,
  "$t5":  13,
  "$t6":  14,
  "$t7":  15,
  "$s0":  16,
  "$s1":  17,
  "$s2":  18,
  "$s3":  19,
  "$s4":  20,
  "$s5":  21,
  "$s6":  22,
  "$s7":  23,
  "$t8":  24,
  "$t9":  25,
  "$k0":  26,
  "$k1":  27,
  "$gp":  28,
  "$sp":  29,
  "$fp":  30,
  "$ra":  31
}

ARM_registers = {
  #ARM has only 17 registers, but a number of different ways to refer to those same 17 registers. Here we allow people to use the format they like best
  "R0":    0, "A1": 0,
  "R1":    1, "A2": 1,
  "R2":    2, "A3": 2,
  "R3":    3, "A4": 3,
  "R4":    4, "V1": 4,
  "R5":    5, "V2": 5,
  "R6":    6, "V3": 6,
  "R7":    7, "V4": 7,  "WR":  7,
  "R8":    8, "V5": 8,
  "R9":    9, "V6": 9,  "SB":  9,
  "R10":  10, "V7": 10, "SL": 10,
  "R11":  11, "V8": 11, "FP": 11,
  "R12":  12, "IP": 12,
  "R13":  13, "SP": 13,
  "R14":  14, "LR": 14,
  "R15":  15, "PC": 15,
  "CPSR": 16
}

mode_dict = {
  "MIPS": MIPS_registers,
  "ARM": ARM_registers
}

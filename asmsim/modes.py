""" Conversion dictionaries for strings that refer to registers. """

MIPS_registers = {
  "$zero": 0, "$0":   0,
  "$at":   1, "$1":   1,
  "$v0":   2, "$2":   2,
  "$v1":   3, "$3":   3,
  "$a0":   4, "$4":   4,
  "$a1":   5, "$5":   5,
  "$a2":   6, "$6":   6,
  "$a3":   7, "$7":   7,
  "$t0":   8, "$8":   8,
  "$t1":   9, "$9":   9,
  "$t2":  10, "$10": 10,
  "$t3":  11, "$11": 11,
  "$t4":  12, "$12": 12,
  "$t5":  13, "$13": 13,
  "$t6":  14, "$14": 14,
  "$t7":  15, "$15": 15,
  "$s0":  16, "$16": 16,
  "$s1":  17, "$17": 17,
  "$s2":  18, "$18": 18,
  "$s3":  19, "$19": 19,
  "$s4":  20, "$20": 20,
  "$s5":  21, "$21": 21,
  "$s6":  22, "$22": 22,
  "$s7":  23, "$23": 23,
  "$t8":  24, "$24": 24,
  "$t9":  25, "$25": 25,
  "$k0":  26, "$26": 26,
  "$k1":  27, "$27": 27,
  "$gp":  28, "$28": 28,
  "$sp":  29, "$29": 29,
  "$fp":  30, "$30": 30,
  "$ra":  31, "$31": 31
}

# ARM_registers = {
#   "R0":    0, "A1": 0,
#   "R1":    1, "A2": 1,
#   "R2":    2, "A3": 2,
#   "R3":    3, "A4": 3,
#   "R4":    4, "V1": 4,
#   "R5":    5, "V2": 5,
#   "R6":    6, "V3": 6,
#   "R7":    7, "V4": 7,  "WR":  7,
#   "R8":    8, "V5": 8,
#   "R9":    9, "V6": 9,  "SB":  9,
#   "R10":  10, "V7": 10, "SL": 10,
#   "R11":  11, "V8": 11, "FP": 11,
#   "R12":  12, "IP": 12,
#   "R13":  13, "SP": 13,
#   "R14":  14, "LR": 14,
#   "R15":  15, "PC": 15,
#   "CPSR": 16
# }

ARM_registers = {
  "r0": 0,
  "r1": 1,
  "r2": 2,
  "r3": 3,
  "r4": 4,
  "r5": 5,
  "r6": 6,
  "r7": 7,
  "r8": 8, "r8_fiq": 8, 
  "r9": 9, "r9_fiq": 9,
  "r10": 10, "r10_fiq": 10,
  "r11": 11, "r11_fiq": 11,
  "r12": 12, "r12_fiq": 12,
  "r13": 13, "r13_fiq": 13, "r13_svc": 13, "r13_abt": 13, "r13_irq": 13, "r13_undef": 13, "sp":13,
  "r14": 14, "r14_fiq": 14, "r14_svc": 14, "r14_abt": 14, "r14_irq": 14, "r14_undef": 14, "lr":14,
  "r15": 15, "pc": 15
  "cpsr": 16,
             "spsr_fiq":17, "spsr_svc": 17, "spsr_abt": 17, "spsr_irq": 17, "spsr_undef": 17,
}




# nest the dicts for accessing based on mode
mode_dict = {
  "MIPS": MIPS_registers,
  "ARM": ARM_registers
}

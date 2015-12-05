def twoscomp(hexstring, bits = 32):
  val = int(hexstring, 16)
  binstring = "{0:0{1}b}".format(int(hexstring, 16), bits)
  if binstring[0] == "1":
    val -= (1 << bits)
  return val


if __name__ == "__main__":
  print(twoscomp("00000000"))
  print(twoscomp("7FFFFFFF"))
  print(twoscomp("80000000"))
  print(twoscomp("FFFFFFFF"))

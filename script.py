from bitstring import BitArray

B = BitArray()

x = 70
k = x*1024

for i in range(k*8):
  B.append("0b1")

f = str(x) + "kb.bin"
with open(f, "wb") as f:
  B.tofile(f)

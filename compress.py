import sys
from math import ceil, log2

from bitstring import BitArray

BLOCK_SIZE = 4096 # standard block size

def position_size(d: dict):
    '''Number of bits required to represent position of D.'''
    return ceil(log2(len(d)))

def pad(block: BitArray):
    '''Adds padding to output.'''
    l = block.len
    pad_size = 8 - (l % 8)
    padding = BitArray(uint=1, length=pad_size)
    padding.append(block)
    return padding

# Check arguments
if(len(sys.argv) < 3):
  print("Usage: compress.py infile.txt outfile.lz")
  exit(1)
fin = sys.argv[1]
fout = sys.argv[2]

output = BitArray()
with open(fin, "rb") as fin, open(fout, "wb") as fout:
  # Initialize variables
  D = { BitArray().bin:0 } # word dictionary
  w = BitArray() # word

  # Read 1 block
  buffer = BitArray(fin.read(BLOCK_SIZE))

  # Code input
  while(buffer != BitArray()):
    for bit in buffer:
      bit = bin(bit)
      w.append(bit)
      if w.bin not in D:
        y = w[:-1] # word in D
        b = w[-1] # last bit of w
        s = position_size(D) # size
        if s != 0:
          # Get index of y in D
          i = D[y.bin] # index
          output.append(BitArray(uint=i, length=s))
        b = bin(b)
        output.append(b)
        # Add w to dictionary
        l = len(D)
        D[w.bin] = l
        # Reset word
        w.clear()

    # Read another block
    buffer = BitArray(fin.read(BLOCK_SIZE))

  # Code remaining bits
  if w != BitArray():
    i = D[w.bin] # index
    s = position_size(D) # size
    output.append(BitArray(uint=i, length=s))

  # Handle byte alignment
  output = pad(output)
  output.tofile(fout)

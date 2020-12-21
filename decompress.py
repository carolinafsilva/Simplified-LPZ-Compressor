import sys
from math import ceil, log2

from bitstring import BitArray

BLOCK_SIZE = 4096 # standard block size

def position_size(d: dict):
  '''Number of bits required to represent position of D.'''
  return ceil(log2(len(d)))

def unpad(block: bytes):
  '''Removes padding from input.'''
  block = BitArray(block)
  while(block[0] != 1):
      block = block[1:]
  return block[1:]

# Check arguments
if(len(sys.argv) < 3):
  print("Usage: decompress.py infile.lz outfile.txt")
  exit(1)
fin = sys.argv[1]
fout = sys.argv[2]

# Read File
with open(fin, 'rb') as fin, open(fout, 'wb') as fout:
  # Initialize variables
  D = { 0:BitArray() } # word dictionary
  output = BitArray()

  # Read code
  block = fin.read()

  # Decode input
  buffer = unpad(BitArray(block))
  s = position_size(D)
  while(buffer.len >= s + 1):
    l = len(D)
    w = BitArray() # word
    if s!=0:
      i = buffer[:s].uint # index
      y = D[i] # word in d
      output.append(y)
      w.append(y)
    b = bin(buffer[s]) # bit
    output.append(b)
    w.append(b)
    D[l] = w

    # Update variables
    buffer = buffer[s+1:]
    s = position_size(D)

    # Write output to file
    if(output.len >= BLOCK_SIZE * 8):
      output[:BLOCK_SIZE * 8].tofile(fout)
      output = output[BLOCK_SIZE * 8:]

  # Decode remaining bits
  if buffer != BitArray():
    output.append(D[buffer.uint])

  # Write output
  output.tofile(fout)

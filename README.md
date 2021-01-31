# Simplified LPZ Compressor

## Dependencies
In order to run the python scripts you need to instal the *bitstring* library.

## How to compress a file?
In order to compress a file you must execute the following command, specifying the file you want to compress and the destiny file.
```sh
python3 compress.py file.txt file.lz
```
or
```sh
pypy3 compress.py ficheiro.txt ficheiro.lz
```

## How to decompress a file?
In order to decompress a file you must execute the following command, specifying the name of the compressed file a the name of the destiny file.
```sh
python3 decompress.py ficheiro.lz ficheiro.txt
```
or
```sh
pypy3 decompress.py ficheiro.lz ficheiro.txt
```

## Implementation Details
- The padding is done by adding a binary string *(0)\*1* in order to byte align the file.
- The file is read in blocks of 4096 bytes, since this is the standard block size, used in most OS.
- The remaing bits are coded using their position on the dicitionary.
    This is, being *w* the sequence of remaing bits and D the dicitionary used to encode, we encode w by concatenating to the output the position of the ocurrence of w in the dictionary, D[w].

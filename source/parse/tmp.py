from bitarray import bitarray

from bitstring import BitArray, BitStream
a = BitArray(uintle=0xaa551e57, length=32)
print(a.hex, a.bin, a[0:4])

print(a[0:4], a[4:8], a[8:16].int, a[16:32])

print('done')
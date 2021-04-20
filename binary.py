with open('binary', 'bw') as binary_file:
    for i in range(17):
        binary_file.write(bytes([i]))
        # note - bytes method takes an iterable, hence [i]

with open('binary2', 'bw') as binary_file_2:
    binary_file_2.write(bytes(range(17)))

with open('binary', 'br') as binary_filled_in_file:
    for b in binary_filled_in_file:
        print(b)

with open('binary2', 'br') as binary_filled_in_file_2:
    for b in binary_filled_in_file_2:
        print(b)


a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open('binary3', 'bw') as binary_file_3:
    # write to binary file with number of bytes specified
    # and either big/little endian format

    # NOTE: big endian byte order signifies that the most
    # significant byte should be placed at the byte with the
    # lowest address
    # Little endian: least signficant byte is placed at the byte
    # with the lowest address

    binary_file_3.write(a.to_bytes(2, 'big'))
    binary_file_3.write(b.to_bytes(2, 'big'))
    binary_file_3.write(c.to_bytes(4, 'big'))
    binary_file_3.write(x.to_bytes(4, 'big'))
    binary_file_3.write(x.to_bytes(4, 'little'))

with open('binary3', 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    # NOTE: reading this back in big endian format
    # changes the end result; we stored it in little
    # endian format, but we read back in big endian.
    # Not good for keeping the same value we want!!
    i = int.from_bytes(binFile.read(4), 'big')
    print(i)

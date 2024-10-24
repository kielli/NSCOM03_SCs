def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))


def shiftRegister(message, generator):
    m, g = int(message, 2) << (len(generator) - 1), int(generator, 2)
    for i in range(len(message)):
        if m & (1 << (len(message) + len(generator) - 2 - i)):
            m ^= (g << (len(message) - 1 - i))
    return format(m & ((1 << (len(generator) - 1)) - 1), f'0{len(generator) - 1}b')

def longDivisionCRC(message, generator):
    pick = len(generator)
    message = message + '0' * (len(generator) - 1) 
    tmp = message[:pick]

    while pick < len(message):
        tmp = xor(generator if tmp[0] == '1' else '0'*pick, tmp) + message[pick]
        pick += 1

    tmp = xor(generator if tmp[0] == '1' else '0'*pick, tmp)
    return tmp

if __name__ == "__main__":
    message = '1010011010'
    generator = '110101'
    crc32Generator = '100000100110000010001110110110111'
    keylen = len(generator)

    long_division_remainder = longDivisionCRC(message, generator)
    crc_32_checksum = longDivisionCRC(message, crc32Generator)
    #shift_register_remainder = shiftRegister(message, generator)

    print(f"Message in Binary: {message}")
    print(f"Generator Polynomial in Binary: {generator}")
    print(f"Generator Polynomial in Binary (CRC-32): {crc32Generator}")


    print(f"\nRemainder using long-hand division: {''.join(map(str, long_division_remainder))}")
    print(f"Remainder using CRC-32: {''.join(map(str, crc_32_checksum))}")
    print(f"Encoded Message using CRC-32: 1010011010{''.join(map(str, crc_32_checksum))}")
    #print(f"Remainder using shift register: {''.join(map(str, shift_register_remainder))}")
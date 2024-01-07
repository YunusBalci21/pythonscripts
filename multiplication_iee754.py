import struct

def float_to_ieee_754(number):
    """ Convert a floating point number to its IEEE 754 binary representation """
    return ''.join(f'{c:08b}' for c in struct.pack('>f', number))

def ieee_754_to_float(binary_string):
    """ Convert an IEEE 754 binary representation to a floating point number """
    return struct.unpack('>f', int(binary_string, 2).to_bytes(4, byteorder="big"))[0]

def multiply_ieee_754(binary_string1, binary_string2):
    """ Multiply two IEEE 754 numbers given in binary format """
    # Convert binary IEEE 754 to float
    num1 = ieee_754_to_float(binary_string1)
    num2 = ieee_754_to_float(binary_string2)

    # Perform multiplication
    result = num1 * num2

    # Convert the result back to IEEE 754 format
    return float_to_ieee_754(result)

# Change the numbers
A = "01000000001010101010101010101010" # IEEE 754 representation of a number
B = "11000000110000000000000000000000" # IEEE 754 representation of another number

result = multiply_ieee_754(A, B)
print("Result:", result)

result_decimal = ieee_754_to_float("11000001011111111111111111111111")
print("Decimal value of the result:", result_decimal)


import struct

def binary_to_float(binary_string):
    # Remove spaces and convert to a 32-bit integer
    int_value = int(binary_string.replace(" ", ""), 2)

    # Convert 32-bit integer to bytes
    byte_value = int_value.to_bytes(4, 'big')

    # Unpack bytes to a float
    float_value = struct.unpack('>f', byte_value)[0]

    return float_value

# Binary to float
binary_input = "0 10000101 10010000000000000000000"  # Example binary input
float_output = binary_to_float(binary_input)

print(float_output)
def decimal_to_binary(value, bits):
    """Converts a decimal number to binary representation with a fixed number of bits."""
    if value >= 0:
        return format(value, '0' + str(bits) + 'b')
    else:
        return format(2**bits + value, '0' + str(bits) + 'b')

# Given values
x = 9  # Decimal
y = -13  # Decimal
z = 13  # Decimal

# Represent x and z as 4-bit binary numbers
x_binary = decimal_to_binary(x, 4)
z_binary = decimal_to_binary(z, 4)

# Represent y in 5-bit two's complement and sign magnitude
y_twos_complement = decimal_to_binary(y, 5)
y_sign_magnitude = decimal_to_binary(abs(y), 5)
y_sign_magnitude = '1' + y_sign_magnitude[1:]  # Add the sign bit

# Range of numbers in 5-bit two's complement
min_value_5bit = -2**(5-1)
max_value_5bit = 2**(5-1) - 1
min_value_5bit_binary = decimal_to_binary(min_value_5bit, 5)
max_value_5bit_binary = decimal_to_binary(max_value_5bit, 5)

print(x_binary, z_binary, y_twos_complement, y_sign_magnitude, (min_value_5bit, min_value_5bit_binary), (max_value_5bit, max_value_5bit_binary)
)

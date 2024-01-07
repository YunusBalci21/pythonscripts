def decimal_to_binary(number):
    """
    Convert a decimal number to its binary representation
    """
    # The bin() function converts a decimal number to binary
    # It returns a string in the format '0bxxxx', so we slice off the '0b'
    return bin(number)[2:]

# conversion 45 to binary
binary_representation = decimal_to_binary(45)
print(binary_representation)

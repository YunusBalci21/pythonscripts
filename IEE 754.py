import struct

def float_to_ieee_754(number):
    """
    Convert a floating-point number to its IEEE 754 binary representation (32-bit single precision).
    """
    # Pack the float into 4 bytes using IEEE 754 standard, big-endian byte order
    packed = struct.pack('>f', number)

    # Convert the bytes to their binary representation
    return ''.join(f'{byte:08b}' for byte in packed)

def is_valid_ieee_754(binary_string):
    """
    Check if a given binary string is a valid IEEE 754 32-bit single precision representation.
    A valid IEEE 754 32-bit binary string should be exactly 32 bits long.
    """
    return len(binary_string) == 32

# Input section
try:
    number = float(input("Enter a floating-point number: "))
    ieee_754_representation = float_to_ieee_754(number)
    is_valid = is_valid_ieee_754(ieee_754_representation)

    print(f"IEEE 754 representation for {number}: {ieee_754_representation}")
    print("Is this a valid IEEE 754 representation?", "Yes" if is_valid else "No")

except ValueError:
    print("Invalid input. Please enter a valid floating-point number.")

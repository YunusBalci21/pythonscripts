def binary_to_decimal_hex_and_check_ieee754(binary_string):
    # Remove spaces from the binary string
    cleaned_binary_string = binary_string.replace(" ", "")

    # Count the number of digits
    num_digits = len(cleaned_binary_string)

    # Check if it fits the IEEE 754 32-bit single-precision format
    is_ieee754 = num_digits == 32

    # Convert binary to decimal
    decimal = int(cleaned_binary_string, 2)

    # Convert decimal to hexadecimal
    hexadecimal = hex(decimal)

    return decimal, hexadecimal, is_ieee754, num_digits

# input for binary to decimal
binary_input = "0100 1100"  # binary input
decimal_output, hexadecimal_output, is_ieee754, num_digits = binary_to_decimal_hex_and_check_ieee754(binary_input)

print(binary_input, decimal_output, hexadecimal_output, is_ieee754, num_digits)


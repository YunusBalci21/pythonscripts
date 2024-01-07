def hex_to_binary(hex_string):
    # Remove the '0x' prefix if present
    hex_string = hex_string.lower().replace("0x", "")

    # Convert hex to binary
    binary_string = bin(int(hex_string, 16))[2:]

    # Pad the binary string with leading zeros if necessary
    if len(binary_string) % 4 != 0:
        binary_string = '0' * (4 - len(binary_string) % 4) + binary_string

    return binary_string

# hex to binary
A = "0x6d"
B = "0xb3"

binary_A = hex_to_binary(A)
binary_B = hex_to_binary(B)

print(binary_A, binary_B)


from decimal_to_binary import decimal_to_binary


def booth_multiplication(x, y, bits):
    # Assuming decimal_to_binary is defined elsewhere or imported
    # Convert to two's complement binary
    x_bin = decimal_to_binary(x, bits)
    y_bin = decimal_to_binary(y, bits)

    # Extend the bits for calculation
    extended_bits = bits + 1
    x_bin = decimal_to_binary(x, extended_bits)
    y_bin = decimal_to_binary(y, extended_bits)

    # Initialize accumulator and extended multiplier
    accumulator = '0' * extended_bits
    extended_multiplier = y_bin + '0'

    # Booth's algorithm steps
    steps = []
    for i in range(bits):
        # Check last two bits of the extended multiplier
        if extended_multiplier[-2:] == '01':
            # Subtract x from accumulator
            accumulator = bin(int(accumulator, 2) - int(x_bin, 2))[2:].zfill(extended_bits)
        elif extended_multiplier[-2:] == '10':
            # Add x to accumulator
            accumulator = bin(int(accumulator, 2) + int(x_bin, 2))[2:].zfill(extended_bits)

        # Arithmetic right shift (accumulator and extended multiplier)
        combined = accumulator + extended_multiplier
        combined = bin(int(combined, 2) >> 1)[2:].zfill(2 * extended_bits)
        accumulator = combined[:extended_bits]
        extended_multiplier = combined[extended_bits - 1:]

        steps.append((accumulator, extended_multiplier))

    # Final product
    product = accumulator + extended_multiplier[:-1]
    return product, steps

# Given values
x = 9  # Decimal
y = -13  # Decimal

# Perform Booth's multiplication
product, booth_steps = booth_multiplication(x, y, 5)

# Convert product to decimal
product_decimal = int(product, 2) if product[0] == '0' else -int(product[1:], 2)

print(f"Product: {product}, Decimal: {product_decimal}, Steps: {booth_steps}")

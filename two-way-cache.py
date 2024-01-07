def convert_hex_to_binary_components(address_hex, total_bits=32, tag_bits=24, index_bits=4):
    """

    Converts a hexadecimal address to its binary components: tag, index, and offset,

    and also converts the binary index to decimal.



    :param address_hex: Hexadecimal address as a string.

    :param total_bits: Total number of bits in the address (default 32).

    :param tag_bits: Number of bits used for the tag (default 24).

    :param index_bits: Number of bits used for the index (default 4).

    :return: A tuple containing the binary representations of the tag, index, and offset,

             and the decimal value of the index.

    """

    # Convert the address to binary and pad to ensure it's the correct length

    address_bin = bin(int(address_hex, 16))[2:].zfill(total_bits)

    # Extract the tag, index, and offset

    tag = address_bin[:tag_bits]

    index_binary = address_bin[tag_bits:tag_bits + index_bits]

    offset = address_bin[tag_bits + index_bits:]

    # Convert binary index to decimal

    index_decimal = int(index_binary, 2)

    return tag, index_binary, offset, index_decimal

# Usage

address_hex = "121076"

tag, index_binary, offset, index_decimal = convert_hex_to_binary_components(address_hex)

print(f"Address: {address_hex}")

print(f"Binary Tag: {tag}")

print(f"Binary Index: {index_binary} (Decimal Index: {index_decimal})")

print(f"Binary Offset: {offset}")
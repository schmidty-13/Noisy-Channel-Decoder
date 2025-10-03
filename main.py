import numpy as np

# Parity-check matrix for
PARITY_CHECK = np.array([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
])

# Lookup table: index = binary value of columns in H, entry = error position (0-based index), None = no error
PARITY_COLUMN = [None, 4, 5, 0, 6, 1, 2, 3]


def load_bits_from_file(filename: str) -> str:
    """
    Load the bit sequence from a file as a comma-separated string.
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                bits = line.strip()
    except FileNotFoundError:
        raise
    return bits


def decode_bitstream(bits_str: str) -> str:
    """
    Decode the bit sequence into an ASCII message.
    Performs error correction using the parity-check matrix,
    extracts 4 message bits from each block, groups into bytes,
    and converts to characters.
    """
    message_list = []
    binary_sequences = []
    ascii_values = []

    # Split input string into list of integer bits
    bit_list = bits_str.split(',')
    for i in range(len(bit_list)):
        bit_list[i] = int(bit_list[i])

    # Divide bit sequence into 7-bit code blocks
    code_list = []
    for i in range(0, len(bit_list), 7):
        code_list.append(bit_list[i:i + 7])

    # Correct each 7-bit block and extract the first 4 bits
    for code in code_list:
        code_matrix = np.array(code).reshape(7, 1)
        result_check = np.matmul(PARITY_CHECK, code_matrix) % 2
        column_num = (result_check[0, 0] << 0) | (result_check[1, 0] << 1) | (result_check[2, 0] << 2)
        if column_num != 0:
            error_index = PARITY_COLUMN[column_num]
            code[error_index] = 1 - code[error_index]
        message_list.append(code[0:4])

    # Combine pairs of 4-bit blocks into 8-bit binary sequences
    for i in range(0, len(message_list), 2):
        binary_sequences.append(message_list[i] + message_list[i + 1])

    # Convert each 8-bit sequence into ASCII values 
    for binary in binary_sequences:
        ascii_value = 0
        for j in range(8):
            ascii_value += binary[j] << j
        ascii_values.append(ascii_value)

    # Convert ASCII values into characters to form the final message
    message = ''.join([chr(value) for value in ascii_values])
    return message


def main():
    try:
        bits = load_bits_from_file("input.txt")
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    decoded = decode_bitstream(bits)
    print(decoded)


if __name__ == "__main__":
    main()

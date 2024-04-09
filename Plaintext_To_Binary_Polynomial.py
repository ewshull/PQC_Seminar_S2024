# Code Generated from ChatGPT with the following prompt: "Write a method that converts text into binary,
# and then binary into a binary polynomial between 0 and q-1"

def text_to_binary_polynomial(text, q):
    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Convert binary to binary polynomial between 0 and q-1
    binary_polynomial = []
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i + 8]
        binary_polynomial.append(int(byte, 2) % q)

    return binary_polynomial


# Code Generated from ChatGPT with the following prompt: "Write [the text_to_binary_polynomial] function in reverse so
# that it converts from a binary polynomial to text"

def binary_polynomial_to_text(binary_polynomial):
    # Convert each integer in the binary polynomial to an 8-bit binary string
    binary_text = ''.join(format(num, '08b') for num in binary_polynomial)

    # TODO: something about this conversion back to text is NOT working

    # Split the binary representation into chunks of 8 bits
    # Convert each chunk to its corresponding ASCII character
    text = ''.join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8))

    return text

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
    # Initialize an empty string to store the binary representation
    binary_text = ''

    # Convert each integer in the binary polynomial to an 8-bit binary string and concatenate it to binary_text
    for num in binary_polynomial:
        # Convert the integer to an 8-bit binary string and format it with leading zeros
        binary_representation = format(num, '08b')

        print(binary_representation)

        # Concatenate the binary representation to binary_text
        binary_text += binary_representation

    print(binary_text)

    # TODO: something about this conversion back to text is NOT working

    # Split the binary representation into chunks of 8 bits
    # Convert each chunk to its corresponding ASCII character
    # Initialize an empty string to store the characters
    text = ''

    # Iterate over binary_text in steps of 8 (8 bits = 1 byte)
    for i in range(0, len(binary_text), 8):
        # Extract an 8-bit substring from binary_text and convert it to an integer
        byte = binary_text[i:i + 8]

        print(byte)

        num = int(byte, 2)

        print(num)

        # Convert the integer to its corresponding ASCII character and append it to text
        character = chr(num)

        print (character)

        text += character

    return text

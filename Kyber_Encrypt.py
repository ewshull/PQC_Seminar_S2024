# Code Generated by ChatGPT from the prompt: "Write a Python implementation of the Crystals-Kyber
# encryption algorithm with comments."

import random


def encrypt(n, q, public_key, plaintext):
    # Generate a random noise polynomial
    noise = [random.randint(0, q - 1) for _ in range(n)]

    # Initialize the ciphertext polynomial
    ciphertext = [0] * n

    for i in range(n):
        # Calculate the contribution from the public key
        ciphertext[i] = public_key[i] * noise[i]

        # Add the plaintext to the ciphertext
        ciphertext[i] += plaintext[i]

        # Modulo q
        ciphertext[i] %= q

    return ciphertext
import random
from Kyber_KeyGeneration import generate_keypair
from Plaintext_To_Binary_Polynomial import text_to_binary_polynomial, binary_polynomial_to_text
from Kyber_Encrypt import encrypt
from Kyber_Decrypt import decrypt

# Parameters for Kyber
n = 256  # Polynomial degree
q = 7681  # Modulus

plaintext = 'Once upon a time there were three Bears, who lived together in a house of their own, in a wood. One of them was a Little Wee Bear, and one was a Middle-sized Bear, and the other was a Great Big Bear. They had each a bowl for their porridge; a little bowl f'

# Input plaintext
print()
print("Plaintext Before:", plaintext)
print()

binary_polynomial_plaintext = text_to_binary_polynomial(plaintext, q)
print("Plaintext as Binary Polynomial:", binary_polynomial_plaintext)
print()

# Generate Public & Secret Key
secret_key, public_key = generate_keypair(n, q)

# Output keys
print("Secret Key:", secret_key)
print()

print("Public Key:", public_key)
print()

# Encrypt Plaintext into Ciphertext
ciphertext = encrypt(n, q, public_key, binary_polynomial_plaintext)

# Output ciphertext
print("Ciphertext:", ciphertext)
print()

# Decrypt Ciphertext into Plaintext
# decrypted_plaintext_binary_polynomial = decrypt(n, q, secret_key, ciphertext)

# Output the decrypted plaintext
# print("Decrypted Plaintext as Binary Polynomial:", decrypted_plaintext_binary_polynomial)
# print()

# decrypted_plaintext = binary_polynomial_to_text(decrypted_plaintext_binary_polynomial)
# print("Decrypted Plaintext:")
# print(decrypted_plaintext)

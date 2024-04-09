import random
from Kyber_KeyGeneration import generate_keypair
from Plaintext_To_Binary_Polynomial import text_to_binary_polynomial, binary_polynomial_to_text
from Kyber_Encrypt import encrypt
from Kyber_Decrypt import decrypt

# Parameters for Kyber
n = 256  # Polynomial degree
q = 7681  # Modulus

plaintext = 'lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget felis eget nunc lobortis mattis aliquam faucibus purus in massa tempor nec feugiat nisl pretium fusc'

# Input plaintext
print("Plaintext Before:", plaintext)

binary_polynomial_plaintext = text_to_binary_polynomial(plaintext, q)
print("Plaintext as Binary Polynomial:", binary_polynomial_plaintext)

# Generate Public & Secret Key
secret_key, public_key = generate_keypair(n, q)

# Output keys
print("Secret Key:", secret_key)
print("Public Key:", public_key)


# Encrypt Plaintext into Ciphertext
ciphertext = encrypt(n, q, public_key, binary_polynomial_plaintext)

# Output ciphertext
print("Ciphertext:", ciphertext)

# Decrypt Ciphertext into Plaintext
decrypted_plaintext_binary_polynomial = decrypt(n, q, secret_key, ciphertext)

# Output the decrypted plaintext
print("Decrypted Plaintext as Binary Polynomial:", decrypted_plaintext_binary_polynomial)

decrypted_plaintext = binary_polynomial_to_text(decrypted_plaintext_binary_polynomial)
print("Decrypted Plaintext:", decrypted_plaintext)

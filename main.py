def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(message, key):
    encrypted_text = []
    key = generate_key(message, key)
    for i in range(len(message)):
        if message[i].isalpha():  # Only encrypt alphabetic characters
            shift = (ord(message[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(message[i])  # Non-alphabetic characters are not encrypted
    return "".join(encrypted_text)

def decrypt(encrypted_message, key):
    decrypted_text = []
    key = generate_key(encrypted_message, key)
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():  # Only decrypt alphabetic characters
            shift = (ord(encrypted_message[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(encrypted_message[i])  # Non-alphabetic characters are not decrypted
    return "".join(decrypted_text)

# Contoh penggunaan
message = "ATTACKATDAWN"
key = "LEMON"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Pesan Asli: ", message)
print("Kunci: ", key)
print("Pesan Terenkripsi: ", encrypted_message)
print("Pesan Terdekripsi: ", decrypted_message)

from collections import Counter

# Fungsi untuk mencari pola berulang dalam teks
def find_repeated_patterns(text, min_length=3):
    patterns = {}
    for i in range(len(text) - min_length + 1):
        for j in range(i + min_length, len(text) - min_length + 1):
            pattern = text[i:j]
            if pattern in patterns:
                patterns[pattern].append(i)
            else:
                patterns[pattern] = [i]
    return {pattern: indices for pattern, indices in patterns.items() if len(indices) > 1}

# Fungsi untuk menghitung faktor umum dari jarak
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_key_length(distances):
    if len(distances) < 2:
        return distances[0] if distances else 1  # Return 1 if distances list is empty
    key_length = gcd(distances[0], distances[1])
    for distance in distances[2:]:
        key_length = gcd(key_length, distance)
    return key_length

# Fungsi untuk analisis frekuensi
def frequency_analysis(segment):
    frequencies = Counter(segment)
    most_common = frequencies.most_common(1)[0][0]
    shift = (ord(most_common) - ord('E')) % 26
    return shift

# Contoh serangan
encrypted_message = "LXFOPVEFRNHR"

# Kasiski Examination
patterns = find_repeated_patterns(encrypted_message)
distances = []
for indices in patterns.values():
    for i in range(1, len(indices)):
        distances.append(indices[i] - indices[i - 1])

if not distances:
    print("Tidak ditemukan pola yang berulang. Tidak dapat menentukan panjang kunci.")
else:
    key_length = find_key_length(distances)

    # Analisis Frekuensi
    key = ''
    for i in range(key_length):
        segment = encrypted_message[i::key_length]
        shift = frequency_analysis(segment)
        key += chr((26 - shift) % 26 + ord('A'))

    print("Panjang Kunci yang Ditemukan: ", key_length)
    print("Kunci yang Ditemukan: ", key)

#!/usr/bin/env python3
"""Caesar and substitution ciphers. Zero dependencies."""

def caesar_encrypt(text, shift=3):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c)-base+shift)%26+base))
        else: result.append(c)
    return "".join(result)

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

def caesar_crack(ciphertext):
    freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    best_shift = 0; best_score = -1
    for shift in range(26):
        plain = caesar_decrypt(ciphertext, shift)
        score = sum(1 for c in plain.upper() if c in freq[:6])
        if score > best_score: best_score = score; best_shift = shift
    return best_shift, caesar_decrypt(ciphertext, best_shift)

def vigenere_encrypt(text, key):
    result = []; ki = 0
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(key[ki % len(key)].upper()) - ord('A')
            result.append(chr((ord(c)-base+shift)%26+base))
            ki += 1
        else: result.append(c)
    return "".join(result)

def vigenere_decrypt(text, key):
    inv_key = "".join(chr((26-(ord(c.upper())-ord('A')))%26+ord('A')) for c in key)
    return vigenere_encrypt(text, inv_key)

def rot13(text): return caesar_encrypt(text, 13)

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "Hello World"
    print(f"Caesar: {caesar_encrypt(text)}")
    print(f"ROT13: {rot13(text)}")

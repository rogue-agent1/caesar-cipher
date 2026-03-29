from caesar_cipher import caesar_encrypt, caesar_decrypt, caesar_crack, vigenere_encrypt, vigenere_decrypt, rot13
assert caesar_encrypt("ABC", 1) == "BCD"
assert caesar_decrypt("BCD", 1) == "ABC"
assert caesar_encrypt("Hello!", 3) == "Khoor!"
assert caesar_decrypt(caesar_encrypt("Test", 7), 7) == "Test"
shift, plain = caesar_crack(caesar_encrypt("THE QUICK BROWN FOX", 5))
assert shift == 5
assert vigenere_encrypt("HELLO", "KEY") == "RIJVS"
assert vigenere_decrypt("RIJVS", "KEY") == "HELLO"
assert rot13(rot13("test")) == "test"
print("caesar_cipher tests passed")

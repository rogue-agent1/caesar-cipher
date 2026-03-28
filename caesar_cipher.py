#!/usr/bin/env python3
"""Caesar cipher encoder/decoder with brute force."""
import sys

def shift(text, n):
    out = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            out.append(chr((ord(c) - base + n) % 26 + base))
        else:
            out.append(c)
    return ''.join(out)

def brute(text):
    for i in range(26):
        print(f"ROT-{i:2d}: {shift(text, i)}")

if __name__ == '__main__':
    if len(sys.argv) < 3: print("Usage: caesar_cipher.py <encode|decode|brute> <text> [shift]"); sys.exit(1)
    cmd, text = sys.argv[1], ' '.join(sys.argv[2:] if cmd == 'brute' else sys.argv[2:-1] if len(sys.argv) > 3 else sys.argv[2:])
    if cmd == 'brute': brute(text)
    else:
        n = int(sys.argv[-1]) if len(sys.argv) > 3 else 13
        if cmd == 'decode': n = -n
        print(shift(text, n))

#!/usr/bin/env python3
"""caesar_cipher - Caesar cipher with brute force."""
import sys, argparse, json, string

def encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force(text):
    return [{"shift": i, "text": decrypt(text, i)} for i in range(26)]

def frequency_attack(text):
    freq = {}
    for ch in text.lower():
        if ch.isalpha(): freq[ch] = freq.get(ch, 0) + 1
    if not freq: return 0
    most_common = max(freq, key=freq.get)
    return (ord(most_common) - ord("e")) % 26

def main():
    p = argparse.ArgumentParser(description="Caesar cipher")
    sub = p.add_subparsers(dest="cmd")
    e = sub.add_parser("encrypt"); e.add_argument("text"); e.add_argument("shift", type=int)
    d = sub.add_parser("decrypt"); d.add_argument("text"); d.add_argument("shift", type=int)
    b = sub.add_parser("crack"); b.add_argument("text")
    args = p.parse_args()
    if args.cmd == "encrypt":
        print(json.dumps({"plaintext": args.text, "shift": args.shift, "ciphertext": encrypt(args.text, args.shift)}))
    elif args.cmd == "decrypt":
        print(json.dumps({"ciphertext": args.text, "shift": args.shift, "plaintext": decrypt(args.text, args.shift)}))
    elif args.cmd == "crack":
        likely = frequency_attack(args.text)
        print(json.dumps({"ciphertext": args.text, "likely_shift": likely, "likely_plaintext": decrypt(args.text, likely), "all_shifts": brute_force(args.text)}, indent=2))
    else: p.print_help()

if __name__ == "__main__": main()

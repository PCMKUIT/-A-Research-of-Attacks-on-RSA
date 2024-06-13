import argparse
from sympy.ntheory.modular import crt
from sympy import integer_nthroot

def decode_message(integer):
    message_bytes = int.to_bytes(integer, (integer.bit_length() + 7) // 8, byteorder='big')
    return message_bytes.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="Perform Hastad's Broadcast Attack.")
    parser.add_argument('cipher_file', type=str, help="File with ciphertexts")
    parser.add_argument('output_file', type=str, help="Output file for plaintext")
    args = parser.parse_args()

    with open(args.cipher_file, 'r') as f:
        data = [line.strip().split() for line in f]

    n = []
    C = []
    e = None
    for line in data:
        ni, ei, ci = map(int, line)
        n.append(ni)
        C.append(ci)
        if e is None:
            e = ei

    x, _ = crt(n, C)
    M, exact = integer_nthroot(x, e)
    if exact:
        plaintext = decode_message(M)
        with open(args.output_file, 'w') as f:
            f.write(plaintext)
        print(f"Attack success with Hastad's Broadcast Method! Check '{args.output_file}' for the result.")
    else:
        print("Failed to find the exact root")

if __name__ == "__main__":
    main()

import argparse

def encode_message(message):
    return int.from_bytes(message.encode('utf-8'), byteorder='big')

def main():
    parser = argparse.ArgumentParser(description="Encrypt a message using RSA public keys.")
    parser.add_argument('key_file', type=str, help="File with public keys")
    parser.add_argument('output_file', type=str, help="Output file for ciphertexts")
    parser.add_argument('-e', '--exponent', type=int, required=True, help="Public exponent")
    parser.add_argument('-p', '--plaintext', type=str, required=True, help="Plaintext message to encrypt")
    args = parser.parse_args()

    with open(args.key_file, 'r') as f:
        keys = [line.strip().split() for line in f]

    message = encode_message(args.plaintext)
    ciphertexts = []

    for n, e in keys:
        n = int(n)
        e = int(e)
        c = pow(message, e, n)
        ciphertexts.append((n, e, c))

    with open(args.output_file, 'w') as f:
        for n, e, c in ciphertexts:
            f.write(f"{n} {e} {c}\n")

    print(f"Encryption completed. Check '{args.output_file}' for the result.")

if __name__ == "__main__":
    main()

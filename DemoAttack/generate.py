import argparse
from Crypto.Util import number

def generate_keys(e, bits=2048):
    keys = []
    for _ in range(e):
        while True:
            p = number.getPrime(bits // 2)
            q = number.getPrime(bits // 2)
            n = p * q
            if number.GCD(e, (p-1)*(q-1)) == 1:
                keys.append(n)
                break
    return keys

def main():
    parser = argparse.ArgumentParser(description="Generate RSA public keys.")
    parser.add_argument('output_file', type=str, help="Output file for keys")
    parser.add_argument('-e', '--exponent', type=int, required=True, help="Public exponent")
    args = parser.parse_args()

    keys = generate_keys(args.exponent)
    with open(args.output_file, 'w') as f:
        for n in keys:
            f.write(f"{n} {args.exponent}\n")

    print(f"Key generation completed. Keys saved as '{args.output_file}'.")

if __name__ == "__main__":
    main()

import random
from Crypto.Util import number
from sympy import isprime, Integer, sqrt

def generate_prime(bits):
    """Generate a prime number of 'bits' length."""
    while True:
        candidate = number.getPrime(bits)
        if isprime(candidate):
            return candidate

def generate_keys():
    """Generate RSA public and private keys with conditions q < p < q + sqrt(q)."""
    bits = 1024

    # Generate q first
    q = generate_prime(bits)

    # Generate p such that q < p < q + sqrt(q)
    max_p = q + Integer(sqrt(q))
    p = generate_prime_between(q + 1, max_p)

    n = p * q
    e = 65537  # Common RSA exponent

    # Calculate the modular inverse of e modulo (p-1)*(q-1)
    d = pow(e, -1, (p - 1) * (q - 1))


    # Save keys to files
    with open('publickey.pub', 'w') as pub_file:
        pub_file.write(f'{n}\n{e}\n')
    with open('privatekey.pri', 'w') as pri_file:
        pri_file.write(f'{n}\n{d}\n')
    with open('factor.txt', 'w') as pri_file:
        pri_file.write(f'{p}\n{q}\n')

    print("Key generation completed. Keys saved as 'privatekey.pri' and 'publickey.pub' and 'factor.txt'.")

def generate_prime_between(low, high):
    """Generate a prime number between 'low' and 'high'."""
    while True:
        candidate = random.randint(low, high)
        if isprime(candidate):
            return candidate

def main():
    generate_keys()

if __name__ == '__main__':
    main()

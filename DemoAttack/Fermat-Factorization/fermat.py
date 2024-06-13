from Crypto.PublicKey import RSA
from sympy import isprime, sqrt, Integer

def fermat_factorization(n):
    """Perform Fermat factorization to factorize n."""
    a = Integer(sqrt(n)) + 1
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n
    b = Integer(sqrt(b2))
    p = a + b
    q = a - b
    return p, q

def is_square(x):
    """Check if x is a perfect square."""
    s = Integer(sqrt(x))
    return s * s == x

def save_factors(p, q):
    """Save factors p and q to fermat.txt."""
    with open('fermat.txt', 'w') as file:
        file.write(f'{p}\n{q}\n')

def main():
    # Load public key
    with open('publickey.pub', 'r') as file:
        key_data = file.readlines()
        n = int(key_data[0].strip())

    # Perform Fermat factorization
    p, q = fermat_factorization(n)

    # Save factors to fermat.txt
    save_factors(p, q)
    print(f"Factors p and q saved to fermat.txt.")

if __name__ == '__main__':
    main()

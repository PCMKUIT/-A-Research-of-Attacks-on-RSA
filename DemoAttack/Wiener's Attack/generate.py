import random
import math
import os.path
from Crypto.Util import number

def check_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = pow(a_to_power, 2, n)
    return a_to_power == n - 1

def check(n, k=20):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not check_pass(a, s, d, n):
            return False
    return True

def gen_prime(bits):
    while True:
        p = number.getPrime(bits)
        if check(p):
            return p

def gen_prime_range(start, stop):
    while True:
        p = random.randrange(start, stop)
        if p % 2 == 0:
            p += 1
        if check(p):
            return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, n):
    x, y, gcd_value = extended_gcd(e, n)
    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist")
    return x % n

def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, gcd_value = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, gcd_value

def totient(p, q):
    return (p - 1) * (q - 1)

def generate_keys(bits=2048):
    p = gen_prime(bits // 2)
    q = gen_prime_range(p + 1, 2 * p)
    n = p * q
    phi_n = totient(p, q)
    
    n_root_4 = integer_root(n, 4)
    max_d = min(phi_n, int((1 / 3) * n_root_4))
    d = random.randrange(2, max_d)
    while gcd(d, phi_n) != 1:
        d = random.randrange(2, max_d)
    
    e = mod_inverse(d, phi_n)
    
    return (n, e, d), (n, e)

def integer_root(x, n):
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1

def save_keys(private_key, public_key):
    """Save RSA keys to files 'privatekey.pri' and 'publickey.pub'."""
    n, e, d = private_key
    with open('privatekey.pri', 'w') as pri_file:
        pri_file.write(f'{n}\n{d}\n')
    n, e = public_key
    with open('publickey.pub', 'w') as pub_file:
        pub_file.write(f'{n}\n{e}\n')

def main():
    """Main function to generate RSA keys and save them to files."""
    private_key, public_key = generate_keys()
    save_keys(private_key, public_key)
    print("Key generation completed. Keys saved as 'privatekey.pri' and 'publickey.pub'.")
    

if __name__ == '__main__':
    main()

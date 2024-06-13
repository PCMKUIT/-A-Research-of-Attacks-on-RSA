from fractions import Fraction
from Crypto.PublicKey import RSA
import os
import traceback
from math import isqrt

def continued_fraction(e, n):
    a = e
    b = n
    frac = []
    while b != 0:
        frac.append(a // b)
        a, b = b, a % b
    return frac

def convergents_from_contfrac(frac):
    n0, n1 = frac[0], frac[1] * frac[0] + 1
    d0, d1 = 1, frac[1]
    yield n0, d0
    yield n1, d1

    for i in frac[2:]:
        n = i * n1 + n0
        d = i * d1 + d0
        yield n, d
        n0, n1 = n1, n
        d0, d1 = d1, d

def wiener_attack(e, n):
    frac = continued_fraction(e, n)
    for k, d in convergents_from_contfrac(frac):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        s = n - phi + 1
        discriminant = s * s - 4 * n
        if discriminant >= 0:
            t = isqrt(discriminant)
            if t * t == discriminant:
                x1 = (s + t) // 2
                x2 = (s - t) // 2
                if x1 * x2 == n:
                    return d
    return None

def main():
    try:
        if not os.path.exists('publickey.pub'):
            print("Publickey.pub not found. Please generate keys first.")
            return

        with open('publickey.pub', 'r') as pub_file:
            lines = pub_file.readlines()
            n = int(lines[0].strip())
            e = int(lines[1].strip())
        
        d = wiener_attack(e, n)
        
        if d is None:
            print("Wiener's Attack failed.")
        else:
            with open('privatekey.txt', 'w') as pri_file:
                pri_file.write(f'{n}\n{d}\n')
            print(f"Attack success with Wiener's Attack! Check privatekey.txt for the result.")
    
    except FileNotFoundError:
        print("Publickey.pub not found. Please generate keys first.")
    except Exception as e:
        print(f"Error reading publickey.pub: {e}")
        traceback.print_exc()  

if __name__ == '__main__':
    main()

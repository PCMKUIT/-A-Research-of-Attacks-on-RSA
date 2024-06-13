from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def generate_key(key_size=1024):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    return private_key, private_key.public_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def save_public_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def load_private_key(filename):
    with open(filename, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )

def load_public_key(filename):
    with open(filename, 'rb') as f:
        return serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

def encrypt(plaintext, public_key):
    plaintext_bytes = plaintext.encode('utf-8')
    ciphertext = public_key.encrypt(
        plaintext_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt(ciphertext, private_key):
    ciphertext_bytes = base64.b64decode(ciphertext)
    plaintext_bytes = private_key.decrypt(
        ciphertext_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext_bytes.decode('utf-8')

def main():
    print("Please select an option:")
    print("1. Generate Key")
    print("2. Encrypt Data")
    print("3. Decrypt Data")

    choice = input("Enter your choice: ")

    if choice == '1':
        private_key, public_key = generate_key()
        save_key(private_key, 'privatekey.pri')
        save_public_key(public_key, 'publickey.pub')
        print("Key generation completed. Keys saved as 'privatekey.pri' and 'publickey.pub'.")
    elif choice == '2':
        plaintext = input("Enter plaintext: ")
        public_key_file = input("Enter public key file path: ")
        public_key = load_public_key(public_key_file)
        ciphertext = encrypt(plaintext, public_key)
        with open('ciphertext.txt', 'w', encoding='utf-8') as f:
            f.write(ciphertext)
        print("Encryption completed. Check ciphertext.txt for the result.")
    elif choice == '3':
        ciphertext_file = input("Enter ciphertext file path: ")
        private_key_file = input("Enter private key file path: ")
        private_key = load_private_key(private_key_file)
        with open(ciphertext_file, 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        plaintext = decrypt(ciphertext, private_key)
        with open('plaintext.txt', 'w', encoding='utf-8') as f:
            f.write(plaintext)
        print("Decryption completed. Check plaintext.txt for the result.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

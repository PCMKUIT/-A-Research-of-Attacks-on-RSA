# A-Research-of-Attacks-on-RSA

Hastad's Broadcast Attack

Generate public key (run first):

python generate.py gen.txt -e ... ( e is exponent )

Message encryption:

python cipher.py gen.txt cipher.txt -e .... -p ... ( p is your plaintext, leave here and we will attack to find it )

Attack and decode the message:

python hastad.py cipher.txt plaintext.txt

In ubuntu

Example:

python3 generate.py gen.txt -e 3

python3 cipher.py gen.txt cipher.txt -e 3 -p "Test Hastad's Broadcast Attack"

python3 hastad.py cipher.txt plaintext.txt 

cat plaintext.txt (check it if it's your plaintext)

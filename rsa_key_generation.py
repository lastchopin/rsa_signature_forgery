import random
import hashlib
from Crypto.Util import number
from sympy import mod_inverse, isprime

def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)

def generate_large_prime(bits):
    while True:
        prime_candidate = number.getPrime(bits)
        if isprime(prime_candidate):
            return prime_candidate

def generate_rsa_key(bits):
    # Schritt 1: Generiere zwei große Primzahlen p und q
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)

    # Schritt 2: Berechne n und φ
    n = p * q
    phi = (p - 1) * (q - 1)

    # Schritt 3: Wähle eine Zufallszahl e
    e = 2**16 + 1
    while number.GCD(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Schritt 4: Berechne d
    d = mod_inverse(e, phi)

    return p, q, n, phi, e, d

# Generiere einen 3000-Bit RSA-Schlüssel
bits = 3000
p, q, n, phi, e, d = generate_rsa_key(bits)

print(f"RSA-Schlüsselparameter:\np: {p}\nq: {q}\nn: {n}\nφ(n): {phi}\ne: {e}\nd: {d}")

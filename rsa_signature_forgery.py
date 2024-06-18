import random
import hashlib
from Crypto.Util import number
from sympy import mod_inverse, isprime

def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)

def rsa_verify(message, signature, e, n):
    message_hash = sha256_hash(message)
    return pow(signature, e, n) == message_hash

def universal_forgery_attack(message, e, d, n):
    # Wähle eine Zufallszahl r
    while True:
        r = random.randint(2, n - 1)
        if pow(r, e, n) != 1:
            break

    # Berechne m' = r^e * m mod n
    message_hash = sha256_hash(message)
    m_prime = (pow(r, e, n) * message_hash) % n

    # Erfrage die Signatur von m' vom Signierer
    s_prime = pow(m_prime, d, n)

    # Berechne s = r^(-1) * s' mod n
    r_inv = mod_inverse(r, n)
    s = (r_inv * s_prime) % n

    return s

# Wähle eine beliebige Nachricht (nur ASCII-Zeichen)
message = b'Example message for forgery'

# Annahme: Die RSA-Schlüsselparameter p, q, n, e, d sind bereits bekannt (kann aus rsa_key_generation.py übernommen werden)

# Führe den universellen Fälschungsangriff durch
# Annahme: Die RSA-Schlüsselparameter p, q, n, e, d sind bereits bekannt (kann aus rsa_key_generation.py übernommen werden)
p, q, n, phi, e, d =  # Füge hier die entsprechenden RSA-Schlüsselparameter ein

forged_signature = universal_forgery_attack(message, e, d, n)

# Verifiziere die gefälschte Signatur
is_valid = rsa_verify(message, forged_signature, e, n)
print(f"Gefälschte Signatur: {forged_signature}")
print(f"Signatur gültig: {is_valid}")

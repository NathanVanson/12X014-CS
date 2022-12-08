### Nathan Vanson UNIGE ###

import hashlib
import ninhash
import random
import os

# Pour utiliser la fonction Nintendhash, il suffit d'appeler la fonction
# ninhash.Nintendhash(bytestring), avec bytestring qui est un... byte string.
# Exemple :

#print("Exemple avec Nintendhash : ")

message = b"Are you sure this hash function is secure ?"
#print("message : ",message)

digest = ninhash.Nintendhash(message)
#print("digest avec Nintendhash : ", digest)

# Pour utiliser SHA-256, voici un exemple : on instancie la classe sha256.
# .update() permet de construire ou rallonger le message (avec des byte strings)
# .digest() retourne le digest (en byte string)
# .hexdigest() retourne le digest en forme hexadecimale (hex string)

m = hashlib.sha256()
m.update(b"Voici un message")
m.update(b" rajout a la suite du message initial")
digest = m.digest()
hexdigest = m.hexdigest()

# La même chose en version condensée :

message = b"Voici un message rajout a la suite du message initial"
hexdigest = hashlib.sha256(message).hexdigest()

#print()

#print("Exemple avec SHA-256 : ")

#print("le message : ", message)

#print("le digest : ", hexdigest)


# Série 11, partie 1 : il faut montrer que le Nintendhash ne respecte pas la
# preimage resistance et la second pre-image resistance.


# 1) La seconde pre-image resistance : voici un message et le digest
# correspondant.
# Trouvez un autre message avec le même digest.

sec_image_message = b"To catch them is my real test. To train them is my cause."
sec_image_digest = ninhash.Nintendhash(sec_image_message)

# TODO : Une fonction qui cherche une autre pre-image ayant le même digest.

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def searchSecondPreimage(message, digest):
    """Renvoie un message ayant le même digest que digest."""
    i = 0
    while True:
        i += 1
        res = byte_xor(message, str(i).encode())
        if ninhash.Nintendhash(res) == digest:
            return res
        
print("Un message ayant le meme digest est :", searchSecondPreimage(sec_image_message, sec_image_digest))

# 2) Trouvez une pre-image pour le digest suivant :

pre_image_digest = "Paper Pokemon Let's Go 2 : Version Argent"

# TODO : Une fonction qui cherche un message ayant le digest voulu.

def searchPreImage(digest):
    """Renvoie un message ayant le digest voulu"""
    while True:
        res = random.getrandbits(256).to_bytes(32, 'little')
        if ninhash.Nintendhash(res) == digest:
            return res
        
print("Un message ayant le digest voulu est :", searchPreImage(pre_image_digest))

# Série 11, partie 2 : trouver une collision partielle sur SHA-256.

# TODO : Une fonction qui trouve un digest finissant par minimum 20 bits à 0

def searchCollision(message):
    """Renvoie un digest finissant par 20 bits à 0"""
    while True:
        digest = hashlib.sha256(message + os.urandom(8)).hexdigest()
        if digest[-5:] == "00000":
            return digest
        
print("Un digest finissant par minimum 20 bits a 0 est :", searchCollision(b"vanson"))
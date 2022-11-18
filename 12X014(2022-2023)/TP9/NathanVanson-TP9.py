### Nathan VANSON UNIGE ###

### RSA Implementation - Asymmetric RSA encryption ###
### License : GNU Public License (GPL)
### Course : Cryptography and Security (TP9)

# ========== LIBRAIRES ========== #

import random

# ========== FONCTIONS ========== #

# ----- Step 1 : Fast Modular Exponentiation Function ----- #

def fastModularExponentiation(a, b, n):
    """Fast modular exponentiation

    Args:
        a (_Any_): Base
        b (_Any_): Exponent
        n (_Any_): Modulus

    Returns:
        _Any | Literal[1]_: Return the result of the modular exponentiation
    """
    number = 1
    while b > 0:
        if b % 2 == 1:
            number = (number * a) % n
        b = b // 2
        a = (a * a) % n
    return number
#print(fastModularExponentiation(123, 687, 15))

# ----- Step 2.1 : Primal Fermat Function ----- #

def primalFermat(n):
    """Fermat primality test

    Args:
        n (_Any_): Number to test

    Returns:
        _Literal[False] | None_: Return value regarding its primality
    """
    for i in range(20): # 20 - Number of repetitions needed for this TP
        a = random.randint(2, n-1)
        number = fastModularExponentiation(a, n-1, n)
        if number != 1:
            return False
        return number
#print(primalFermat(3))

# ----- Step 2.2 : Prime Random Generator Function ----- #

def primeRandomGenerator():
    """Random prime number generator

    Returns:
        _Any_: Return a random prime number
    """
    while True:
        prime = random.getrandbits(512)
        if primalFermat(prime):
            return prime
#p = primeRandomGenerator()
#q = primeRandomGenerator()
#print(p)
#print(q)

# ----- Step 3 : Extended Euclide Function ----- #

def extendedEuclide(a, b):
    """Extended Euclide Algorithm - RSA

    Args:
        a (_Any_): First random integer
        b (_Any_): Second random integer such that a >= b 

    Returns:
        _tuple_: Tuple
    """
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    q = [0, r[0] // r[1]]
    i = 1
    while True:
        r.append(r[i-1] - q[i]*r[i])
        s.append(s[i-1] - q[i]*s[i])
        t.append(t[i-1] - q[i]*t[i])
        if r[i+1] == 0: # Prevent division by 0
            return r[i], s[i] % b, t[i] % a
        q.append(r[i] // r[i+1])
        i += 1
#print(extendedEuclide(46, 25))

# ----- Step 4 : Key Pair Generation Function ----- #

def keyPairGeneration(p, q):
    """_summary_

    Args:
        p (_Any_): First large prime number
        q (_Any_): Second large prime number

    Returns:
        _tuple[list, list]_: Public and private key pairs
    """
    n = p * q
    print("Your modulus corresponds to 'n' is : \n", n)
    print("\n")
    phi = (p-1) * (q-1)
    
    r = 0
    while r != 1:
        e = random.randint(1, phi)
        r, s, d = extendedEuclide(phi, e)
        if r == 1:
            return [e, n], [d, n]
#print(keyPairGeneration(19, 77))
        

# ----- Step 5 : Encryption Function ----- #

def encryption(m, e, n):
    """Encryption Function - RSA

    Args:
        m (_Any_): Message
        e (_Any_): Encryption exponent
        n (_Any_): Modulus

    Returns:
        _Any | Literal[1]_: Encrypted message
    """
    return fastModularExponentiation(m, e, n)
#print(encryption(3,37,77))

# ----- Step 6 : Decryption Function ----- #

def decryption(c, d, n):
    """Decryption Function - RSA

    Args:
        c (_Any_): Message
        d (_Any_): Decryption exponent
        n (_Any_): Modulus

    Returns:
        _Any | Literal[1]_: Decrypted message
    """
    return fastModularExponentiation(c, d, n)
#print(decryption(69,13,77))

# ========== MAIN ========== #

if __name__ == "__main__":
    print("===========================================================================================================")
    print("================================== RSA ENCRYPTION / DECRYPTION. ===========================================")
    print("===========================================================================================================")
    print("\n")
    p = primeRandomGenerator()
    q = primeRandomGenerator()

    print("Your first random prime number corresponding to 'p' is :\n", p)
    print("\n")
    print("Your second random prime number corresponding to 'q' is \n", q)
    print("\n")
    
    public, private = keyPairGeneration(p, q)
    
    print("Your public key is :\n", public)
    print("\n")
    print("Your private key is :\n", private)
    print("\n")
    
    m = random.getrandbits(512)
    encryptedMessage = encryption(m,public[0], public[1])
    
    print("Your random message corresponds to :\n", m)
    print("\n")
    print("Encryption of the message with the given random public key :\n", encryptedMessage)
    print("\n")
    
    decryptedMessage = decryption(encryptedMessage,private[0], private[1])
    
    print("Decryption of the message with the given random private key :\n", decryptedMessage)
    print("\n")
    
    print("===========================================================================================================")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")
### Nathan Vanson UNIGE ###

### Vigenère encryption from a given ciphertext ###
### Course : Cryptography and Security (TP2)

# ========== LIBRAIRIES ========== #

from ciphertextTP2 import *
from math import sqrt

# ========== Step 1 : KEY LENGHT ========== #

def decalage(a, L):
    """Shift of the cyphertext of 'L' caracateres

    Args:
        a (_Any_): Character in the original text
        L (_Any_): Shifted position of the character(s)

    Returns:
        _Any_: Position of the character in the offset text
    """
    return a[L:] + a[:L]

def superposition(a, b, j):
    """Superposition : Test if the 'ith' character of each string is equal

    Args:
        a (_Any_): Character of the original text
        b (_Any_): Shifted text character
        j (_Any_): Position of the character

    Returns:
        _int_: Return 1 if equal, 0 otherwise
    """
    return int(a[j] == b[j])
    
def indice_coincidence(A, B, L):
    """The coincidence index

    Args:
        A (_Any_): Original text
        B (Any): Shifted text of L characters
        L (Any): Shifted position of the character(s)

    Returns:
        _Any_: Coincidence index
    """
    N = len(A)
    N2 = N - L
    somme = sum(superposition(A, B, j) for j in range(1, N2+1))
    taille = somme / N2
    return taille

# ========== Step 2 : VIGENERE ========== #

def groupe(string, n, k):
    """Separations into k groups to create k subtexts

    Args:
        string (_Any_): _NONE_
        n (_Any_): _NONE_
        k (_Any_): Number of groups / subtexts

    Returns:
        _list_: List of groups
    """
    groupe_liste = []
    for i in range(int(len(string)/k)):
        groupe_liste.append(string[n + i*k])
        #print(groupe_liste)
    return groupe_liste

def frequence(string):
    """Frequency of a character

    Args:
        string (_Any_): Character

    Returns:
        _list[float]_: Returns the frequency of a character in float
    """
    freq = [0] * 26
    for char in string:
        freq[ord(char) - ord('a')] += 1
    somme_freq = sum(freq)
    #print(somme_freq)
    freq = [k / somme_freq for k in freq]
    return freq

def distance_euclidienne(F, M, dec):
    """Euclidean distance

    Args:
        F (_Any_): Known language frequencies
        M (_Any_): Frequencies measured by the subtext
        dec (_Any_): Gap

    Returns:
        _int_: Euclidean distance
    """
    distance = sum(pow(F[i]-M[(i+dec)%26], 2 ) for i in range(26)) # Modulo 26 pour la position de l'alphabet
    return distance

# ========== Step 3 : DECRYPTION ========== #

def decryption(ciphertext, cle):
    """Decryption of the ciphertext with the key

    Args:
        ciphertext (_Any_): Ciphertext from "ciphertextTP2.py"
        cle (_Any_): Decoded key

    Returns:
        _LiteralString_: The corresponding text
    """
    plaintext = []
    for i, c in enumerate(ciphertext):
        c = ord(c) - ord(cle[i % len(cle)])
        c = chr(c % 26 + ord('a'))
        plaintext.append(c)
    return "".join(plaintext)

# ========== MAIN ========== #

if __name__ == "__main__":
    cle = []
    groupes = []
    indice = [indice_coincidence(ciphertext, decalage(ciphertext, L), L) for L in range(1, maximum_key_size)]
    
    n = max(indice)
    k = indice.index(n) + 1
        
    print("L'index maximale est : {}".format(n))
    print("La taille de la clé correspond à : {}".format(k))
    
    for n in range(k+1):
        groupes.append(groupe(ciphertext, n, k))
        
    for freq in range(k):
        M = frequence(groupes[freq])
        distance = [distance_euclidienne(english_freq, M, dec) for dec in range(1, 27)]
        distance_minimum = min(distance)
        indice_cle = distance.index(distance_minimum) + 1
        cle.append(chr((indice_cle % 26) + ord('a')))
        distance = []
            
    print("La clé est : ", "".join(cle))
    print("Le texte déchiffré est donc : ", decryption(ciphertext, cle))

### Nathan Vanson UNIGE ###

### DES implementation - Data Encryption Standard (Encryption and Decryption) ###
### Course : Cryptography and Security (TP6)

# ========== LIBRAIRES ========== #

from DES_tables import *

# ========== FONCTIONS ========== #

# ----- Step 1 : Basic Functions ----- #

def hex2Bin(hex):
    """Hexadecimal to Binary

    Args:
        hex (_Any_): Hexadecimal

    Returns:
        _list[int]_: Binary
    """
    return list(map(int, list(format(hex, '0>64b'))))

def bin2Hex(ciphertext):
    """Binary to Hexadecimal

    Args:
        ciphertext (_Any_): Ciphertext in binary

    Returns:
        _str_: Hexadecimal
    """
    return hex(int("".join(str(x) for x in ciphertext), 2))

def permutation(list, table):
    """Permutation of the list with n elements in a table

    Args:
        list (_Any_): List
        table (_Any_): Table

    Returns:
        _list[int]_: _description_
    """
    return [int(list[n-1]) for n in table]

def xor(list1, list2):
    """Xor between 2 lists

    Args:
        list1 (_Any_): First List
        list2 (_Any_): Second List

    Returns:
        _list_: List resulting from the xor
    """
    return [list1[i]^list2[i] for i in range(len(list1))]

def cutList(list):
    """Separations of the site in 2 parts of 32 bits

    Args:
        list (_Any_): List

    Returns:
        _tuple_: Tuple of 2 lists of 32 bits
    """
    size = len(list) 
    n = int(size/2)
    L = list[:n]
    R = list[n:]
    return L, R

def rotation(n, i):
    """Rotates two parts of the number n (binary)

    Args:
        n (_Any_): _NONE_
        i (_Any_): _NONE_

    Returns:
        _Any_: _NONE_
    """
    return n[i:] + n[:i]
        
def key_PC2(LK, RK):
    """PC_2 Permutation

    Args:
        LK (_Any_): LK
        RK (_Any_): RK

    Returns:
        _list[int]_: List PC_2 Permutation
    """
    key_p = LK + RK
    return permutation(key_p, PC_2)

def subKey(key):
    """Generates an array with 16 SubKeys

    Args:
        key (_Any_): Key

    Returns:
        _list_: SK
    """
    LK, RK = cutList(permutation(key, PC_1))
    SK = []
    for i in Rotations:
        LK = rotation(LK, i)
        RK = rotation(RK, i)
        SK.append(key_PC2(LK, RK))
    return SK

def substitutions(res):
    """Substitutions function - DES

    Args:
        res (_Any_): _NONE_

    Returns:
        _LiteralString_: Substitutions result
    """
    s_result = []
    for i in range(8):
        tmp = res[i*6:i*6+6]
        row = tmp[0]*2 + tmp[-1]
        col = tmp[1]*8 + tmp[2]*4 + tmp[3]*2 + tmp[4]
        val = S_Boxes[i][row][col]
        s_result.append('{:04b}'.format(val))
    s_result = ''.join(s_result)
    return s_result
        
# ----- Step 2 : Cipher Function ----- #
# Following the example that is : Cipher(R_i, SubKey_i) = P(S(E(R_i) ⊕ SubKey_i))

def cipherFunction(R, SubKey):
    """Cipher function - DES

    Args:
        R (_Any_): _NONE_
        SubKey (_Any_): SubKey

    Returns:
        _list[int]_: Integer table
    """
    # Ri extension with the table "E" of the file DES_tables.py
    Ri_etendu = permutation(R, E) 
    # XOR between Ri and the step subkey
    xor_Ri = xor(Ri_etendu, SubKey)
    # Cutting the result using 1 of the 8 S-boxes
    s_res = substitutions(xor_Ri)
    # We apply to the 32 bits obtained a permutation P
    p_res = permutation(s_res, P)
    return p_res    

# ----- Step 3 : Encryption Function ----- #

def encryption(plaintext, key):
    """Encryption function - DES

    Args:
        plaintext (_Any_): Plaintext to encrypt
        key (_Any_): Key

    Returns:
        _str_: Ciphertext
    """
    bin_plaintext = hex2Bin(plaintext)
    #print("message: ", bin_plaintext)
    bin_key = hex2Bin(key)
    #print("key: ", bin_key)
    
    L, R = cutList(permutation(bin_plaintext, IP))
    #print("L: {}\nR: {}".format(L, R))

    SubKey = subKey(bin_key)
    #print("SubKey Set: ", SubKey)
    for i in range(0, 15):
        res = cipherFunction(R, SubKey[i])
        #print("Cipher result number {}: {}".format(i, res))
        L = xor(L, res)
        #print("R xored: ", R)
        L, R = R, L

    res = cipherFunction(R, SubKey[15])
    #print("Last Cipher: ", res)
    L = xor(L, res)
    #print("L xored: ", L)
    full = L + R
    inversed = permutation(full, IP_Inverse)
    #print("Inversed L and R: ", inversed)
    ciphertext = bin2Hex(inversed)
    return ciphertext

# ----- Step 4 : Decryption Function ----- #
    
def decryption(ciphertext, key):
    """Decryption function - DES

    Args:
        ciphertext (_Any_): Ciphertext to decrypt
        key (_Any_): Key used for the encryption

    Returns:
        _str_: Plaintext
    """
    bin_ciphertext = hex2Bin(ciphertext)
    bin_key = hex2Bin(key)

    L, R = cutList(permutation(bin_ciphertext, IP))
    SK = subKey(bin_key)
    #print("SubKey Set: ", SubKey)
    for i in range(15,0,-1):
        #F function
        res = cipherFunction(R, SK[i])
        #print("Cipher result number {}: {}".format(i, res))
        L = xor(L, res)
        #print("R xored: ", R)
        L, R = R, L

    res = cipherFunction(R,SK[0])
    #print("Last Cipher: ", res)
    L = xor(L, res)
    #print("L xored: ", L)
    full = L + R
    inversed = permutation(full, IP_Inverse)
    #print("Inversed L and R: ", inversed)
    plaintext = bin2Hex(inversed)
    return plaintext

# ========== MAIN ========== #

if __name__ == "__main__" :
    # We perform a test with the example given in the statement :
    plaintext = 0x0011223344556677
    key = 0x0123456789ABCDEF
    
    ciphertext_DES = encryption(plaintext, key)
    
    print("Ciphertext correspondant:" ,ciphertext_DES)
    print("Decryption correspondante à {} : {}".format(hex(0xcadb6782ee2b4823), decryption(0xcadb6782ee2b4823, key)))

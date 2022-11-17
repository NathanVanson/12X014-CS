### Nathan Vanson UNIGE ###

### TP4 : Version Hidden Blue - Steganography ###
### License : GNU Public License (GPL)
### Course : Cryptography and Security (TP4)

# ========== LIBRAIRIES ========== #

from PIL import Image
import PIL.ImageOps
import numpy as np

# ========== Step 1 : VARIABLES ========== #

# Opening images
image_A = Image.open("Aerith.png")
image_B = Image.open("Smash.png")
image_C = Image.open("Pokemon.png")
imageCipher = Image.open("Cipherimage.png")

# Size of the images
longueur_A, hauteur_A = image_A.size
longueur_B, hauteur_B = image_B.size
longueur_C, hauteur_C = image_C.size

# RGB colors
couleurs = {
    "rouge": 0,
    "vert": 1,
    "bleu": 2
}

# ========== Step 2 : FONCTIONS ========== #

def imageToTableau(image):
    """Convert an existing image into a table

    Args:
        image (_type_): Selected image

    Returns:
        _NDArray_: Table
    """
    return np.asarray(image).copy()

#print(imageToTableau(image_A))
#print(imageToTableau(image_B))
#print(imageToTableau(image_C))

def pixelLigne(imageTableau, hauteurDebut, hauteur, longueurDebut, longueur, couleur):
    """Search for matching pixels in line 

    Args:
        imageTableau (_Any_): _NONE_
        hauteurDebut (_Any_): _NONE_
        hauteur (_Any_): _NONE_
        longueurDebut (_Any_): _NONE_
        longueur (_Any_): _NONE_
        couleur (_Any_): _NONE_

    Returns:
        _list_: Pixels
    """
    pixels = []
    for i in range(hauteurDebut -1, hauteur):
        for j in range(longueurDebut -1, longueur):
            pixels.append(imageTableau[i][j][couleur])
    return pixels
    
def pixelColonnes(imageTableau, hauteurDebut, hauteur, longueurDebut, longueur, couleur):
    """Search for matching pixels in rows (no for the first image)

    Args:
        imageTableau (_Any_): _NONE_
        hauteurDebut (_Any_): _NONE_
        hauteur (_Any_): _NONE_
        longueurDebut (_Any_): _NONE_
        longueur (_Any_): _NONE_
        couleur (_Any_): _NONE_

    Returns:
        _list_: Pixels
    """
    pixels = []
    for i in range(longueurDebut -1, longueur):
        for j in range(hauteurDebut -1, hauteur):
            pixels.append(imageTableau[j][i][couleur])
    return pixels

def DernierBitSignificatif(bits, dbs): 
    """Get the last significant bit

    Args:
        bits (_Any_): Bits
        dbs (_Any_): Last significant bit

    Returns:
        _Literal[1, 0]_: Least significant bit
    """
    x = (bits & (1 << (dbs - 1)))
    if x:
        return 1
    else:
        return 0

def list_DernierBitSignificatif(tableau): 
    """Put the last significant bit in an array

    Args:
        tableau (_Any_): Table

    Returns:
        _list_: List containing the last significant bit
    """
    LastBits = []
    for bits in tableau:
        LastBits.append(str(DernierBitSignificatif(bits, 1)))
    return LastBits

def list_DeuxDernierBitSignificatif(tableau):
    """Put the two last significant bit in an array

    Args:
        tableau (_Any_): Table

    Returns:
        _list_: List containing the two last significant bit
    """
    Last2Bits = []
    for bits in tableau:
        Last2Bits.append(str(DernierBitSignificatif(bits,  2)))
        Last2Bits.append(str(DernierBitSignificatif(bits,  1)))
    return Last2Bits

def binToAscii(texteBinaire):
    """Transforms binary to Ascii

    Args:
        texteBinaire (_Any_): Binary text

    Returns:
        _str_: Ascii
    """
    n = 8
    bits = [texteBinaire[i:i+n] for i in range(0, len(texteBinaire), n)]
    return ''.join([chr(int(bit, 2)) for bit in bits])

def decode(string):
    """Decoding the text hidden in the image

    Args:
        string (_Any_): Text

    Returns:
        _LiteralString_: Decoded text
    """
    return "".join(x for x in string if x.isupper())

# ========== MAIN ========== #

if __name__ == "__main__" :
    
    # ======================== #
    ### Image A : Aerith.png ###
    # ======================== #

    #print("Image A:", longueur_A, "*", hauteur_A, "\n")
    image_A_Tableau = imageToTableau(image_A)
    #print(image_A_Tableau)
    pixelsImage_A = pixelLigne(image_A_Tableau, 43, 47, 1, longueur_A, couleurs["vert"])
    #print(pixelsImage_A)
    dernierBitSignificatifImage_A = ''.join(list_DernierBitSignificatif(pixelsImage_A))
    #print(lsbImage_A)q
    aerith_binToAscii = binToAscii(dernierBitSignificatifImage_A)
    #print(aerith_binToAscii)
    decodeImage_A_String = decode(aerith_binToAscii)
    print(decodeImage_A_String)

    # ======================= #
    ### Image B : Smash.png ###
    # ======================= #
    
    # After decoding the image A : SMASH-COLONNE-CENT-VINGT-ET-APRES-LEAST-TWO-RED-BITSÏÏÄHÅ #

    #print("Image B:", longueur_B, "*", hauteur_B, "\n")
    image_B_Tableau = imageToTableau(image_B)
    #print(image_B_Tableau)
    pixelsImage_B = pixelColonnes(image_B_Tableau, 1, hauteur_B, 120, 122, couleurs["rouge"])
    #print(pixelsImage_B)
    dernierBitSignificatifImage_B = ''.join(list_DeuxDernierBitSignificatif(pixelsImage_B))
    #print(lsbImage_B)
    smash_binToAscii = binToAscii(dernierBitSignificatifImage_B)
    #print(smash_binToAscii)
    print(" Message décodé dans l'image Smash : {}".format(smash_binToAscii.encode("utf-8")))
    print("\n")

    # ========================= #
    ### Image C : Pokemon.png ###
    # ========================= #
    
    # After decoding image B: The key image is hidden in the Pokémon image.
    # Each pixel of the key is hidden in a 2x2 square ( 4 pixels ) in the image,
    # in this way: the value is hidden in the last two green bits of each pixel ( in this order :
    # top left, top right, bottom left, bottom right ). These eight bits make the green value of the key pixel.
    # Ditto for the red and blue colors. We have a pixel of the key hidden in 4 pixels of the image
    # ( example: the pixel [0][0] of the key is in the pixels [0][0], [0][1], [1][0] and [1][1] of the image ).
    # Only the first 450 rows and columns are useful ( because the key is 225x225 in size ).
    
    #print("Image C:", longueur_C, "*", hauteur_C, "\n")
    image_C_Tableau = imageToTableau(image_C)
    #print(image_C_Tableau)

    hauteurNeed_C, longueurNeed_C = 450, 450
    KeyImage_C = image_C_Tableau[:hauteurNeed_C, :longueurNeed_C, :]

    pixels_C_rouge = []
    pixels_C_vert = []
    pixels_C_bleu = []

    for i,j in zip(range(0, hauteurNeed_C+1, 2), range(2, hauteurNeed_C+1, 2)):
        for k, l in zip(range(0, hauteurNeed_C+1, 2), range(2, hauteurNeed_C+1, 2)):
            pixels = KeyImage_C[i:j, k:l]
            pixels_C_rouge.append(pixelLigne(pixels, 1, 2, 1, 2, couleurs["rouge"]))
            pixels_C_vert.append(pixelLigne(pixels, 1, 2, 1, 2, couleurs["vert"]))
            pixels_C_bleu.append(pixelLigne(pixels, 1, 2, 1, 2, couleurs["bleu"]))

    #print(pixels_C_rouge)
    #print(pixels_C_vert)
    #print(pixels_C_bleu)

    LastBit_rouge_string = []
    LastBit_vert_string = []
    LastBit_bleu_string = []

    # Array containing all pixels bits ( red, green, blue )
    for i, j, k in zip(pixels_C_rouge, pixels_C_vert, pixels_C_bleu):
        LastBit_rouge_string.append(''.join(list_DeuxDernierBitSignificatif(i))) # -> Red
        LastBit_vert_string.append(''.join(list_DeuxDernierBitSignificatif(j))) # -> Green
        LastBit_bleu_string.append(''.join(list_DeuxDernierBitSignificatif(k))) # -> Bleue

    pixels_C_All = []
    for i, j, k in zip(LastBit_rouge_string, LastBit_vert_string, LastBit_bleu_string):
        pixels_C_All.append([int(i, 2), int(j, 2), int(k, 2)])

    pixels_C = np.array(pixels_C_All).reshape(225, 225, 3) # Paramètres permettant d'obtenir une image à partir d'un tableau en 3D

    #print(pixels_C)

    Key_Image = Image.fromarray((pixels_C * 255).astype(np.uint8))
    Key_Image.save("FinalKeyImage.png")

    # ================ #
    ### Image Finale ###
    # ================ #

    #print(imageCipher.size)
    Key_Image = Image.open("FinalKeyImage.png")

    finalResult = np.bitwise_xor(imageCipher, Key_Image).astype(np.uint8)
    Image.fromarray(finalResult).save("Final_Image.png")

    finalImage = Image.open("Final_Image.png")

    inverseImage = PIL.ImageOps.invert(finalImage) # -> Invert the colors of the first final image obtained.
    inverseImage.save("Final_Image.png")

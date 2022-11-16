ciphertext = """iymyiiiwuhvruqwpimmwtiqqwdwduhtfomqtjxdsslkqhqpvurivvpsdemajiymosbgizchdwexgjcogtjaryawzmrryqeihkpqwtiqqwefxgppiqfchgizwhvdqvpcvurivvpsrfvesavaimiybtiuzzexgxiyibvbdsxuzqptraqhxevurtkmqrtzotxnjqjjdibticzvficuwqrivzfexeuqrijgextdzfltdmfvdzlsebvaolgfvugavbtibzaemdeaajqfczxnyczxtiamqjjideczvmwrzmzgtwqoxxfvdwtkburvnpugwtwzxpzveqpegembztmvxkqqwifbtipcqqruztyjgrvolxjmoickzmpecwfiavuqrijzmvtkpqqtkzamsfzseczaywpelfltjxmgtgqdeivailxtpfvnkwqbecwuxiymyiiiwuhhgwiigjbtigxiyiecikgddjurtjipztebgvtsieisfvqbecwdeizwzecuqfibxifltiqzklzbttarbrsgdmdecuzeldfbqvspvmqxtafltdmfvdzlsebvamvtwiysjjnaviymuvcfvxmcvidkpdmbpppetigvwzirrvdgddxxiivisebveuxwrnderkqardwbtixkmywpmiuppstqmckpqkpdmdxwvzqegvwhigrladteomqtjqzxwvaqvxvaflxjqzgallqwuzdqqpzvsebvayiiiwuhbvbdsxubisgimfygewrwpdcewjgmdqtkzamsdmfvdzlryhzwzecuuqxgfqphgvipxlfabmcfnrkpdmejdibtigeqzxtelahhwiymapuqxgfqptgzuqtxejmparvpqtkzamsgzuqtwmpigrbuscwwdgtrnuvhkxqvhfvdesmmzxjimsebveuxwnqdiavaeecuwzpxemyyakqbpppmdqtkzamsgzuqtyczxtiafltdmfvdzlbvxdmdxgztakndmfvdzlbvxdmyiiiwuheiqyiinwqgwfmeecuuqxgfqptgzuqxwimqgdizgtizwzecuzyiiiwuhdkpqvbraiiaciezpiqayhfbtiggwdxhrvpvtdiwih"""

# Taille maximale de la clé. Vous savez d'avance que la clé est d'une taille
# inférieure ou égale à 10 caractères.
maximum_key_size = 10

# Frequences de chaque caractere dans la langue anglaise
# (sur un total de 1. Ex : pour le "a", 0.0808 signifie donc 8.08 %)
english_freq = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, \
                  0.0527, 0.0724, 0.0014, 0.0063, 0.0404, 0.0260, 0.0738, \
                  0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0279, \
                  0.0100, 0.0189, 0.0021, 0.0165, 0.0007]


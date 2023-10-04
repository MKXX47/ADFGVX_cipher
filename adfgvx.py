"""
Chiffre ADFGVX - Phase de substitution
"""
import random
import string


def generer_cle_substitution():
    """
    Génère une liste contenant 36 caractères, les 26 lettres majuscules et les 10 chiffres, mélangés au hasard.
    Exemple : ['R', 'I', 'C', '8', 'O', 'E', 'S', 'A', '6', 'U', 'L', '9', 'K', 'Y', 'B', 'N', 'F', '3',
               'H', '5', 'T', '1', 'Q', 'D', 'G', 'V', 'W', 'Z', '2', '0', 'X', 'J', 'M', 'P', '7', '4']
    :return: clé secrète
    :rtype: list of str
    """
    alphabet_maj = string.ascii_uppercase
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cle_secrete = []
    for lettre in alphabet_maj:
        cle_secrete.append(lettre)
    for number in num:
        cle_secrete.append(number)
    random.shuffle(cle_secrete)
    return cle_secrete


def afficher_cle_substitution(cle):
    """
    Affiche les 36 caractères de la clé de substitution selon un tableau de codage ADFGVX.
    Exemple :
          A D F G V X
        A R I C 8 O E
        D S A 6 U L 9
        F K Y B N F 3
        G H 5 T 1 Q D
        V G V W Z 2 0
        X X J M P 7 4
    :param cle: liste contenant les 36 caractères de la clé de substitution
    :type cle: list of str
    """
    return f'''Clé de substitution :
      A D F G V X 
    A {' '.join([str(item) for item in cle[0:6]])}
    D {' '.join([str(item) for item in cle[6:12]])}
    F {' '.join([str(item) for item in cle[12:18]])}
    G {' '.join([str(item) for item in cle[18:24]])}
    V {' '.join([str(item) for item in cle[24:30]])}
    X {' '.join([str(item) for item in cle[30:]])} 
    '''


def creer_dict_de_substitution(cle):
    """
    Crée un dictionnaire qui associe à chacun des 36 caractères son diagramme ADFGVX de substitution.
    Exemple : {'R': 'AA', 'I': 'AD', 'C': 'AF', '8': 'AG', 'O': 'AV', 'E': 'AX', 'S': 'DA', ... }
    :param cle: liste contenant les 36 caractères de la clé de substitution
    :type cle: list of str
    :return: dictionnaire de substitution ADFGVX
    :rtype: dict {str: str}
    """
    line = ['A', 'D', 'F', 'G', 'V', 'X']
    dic_sub = {}
    indice = 0
    for item in cle[0:6]:
        dic_sub[item] = 'A' + line[indice]
        indice += 1
    indice = 0
    for item1 in cle[6:12]:
        dic_sub[item1] = 'D' + line[indice]
        indice += 1
    indice = 0
    for item2 in cle[12:18]:
        dic_sub[item2] = 'F' + line[indice]
        indice += 1
    indice = 0
    for item3 in cle[18:24]:
        dic_sub[item3] = 'G' + line[indice]
        indice += 1
    indice = 0
    for item4 in cle[24:30]:
        dic_sub[item4] = 'V' + line[indice]
        indice += 1
    indice = 0
    for item5 in cle[30:]:
        dic_sub[item5] = 'X' + line[indice]
        indice += 1
    return dic_sub


def substituer_message(dict_subst, message):
    """
    Chiffre le message en substituant chaque lettre ou chiffre par son digramme ADFGVX.
    Les autres caractères sont éliminés.
    :param dict_subst: le dictionnaire de substitution
    :type dict_subst: dict {str: str}
    :param message: le message à chiffrer
    :type message: str
    :return: le message chiffré
    """
    message_chiffre = ""
    for cle in dict_subst.keys():
        for i in message:
            if cle == i:
                message_chiffre += dict_subst[cle] + " "
            else:
                pass
    return message_chiffre


def main():
    cle_secret = generer_cle_substitution()
    print("Chiffrement ADFGXV\n------------------\n          ")
    print(afficher_cle_substitution(cle_secret))
    dic_sub = creer_dict_de_substitution(cle_secret)
    print(f"Dictionnaire de substitution :\n{dic_sub}\n       ")
    while True:
        message_input = input("Message à chiffrer ?").upper()
        message_chiffre = substituer_message(dic_sub, message_input)
        if len(message_input) > 1:
            print(f"Message chiffré : {message_chiffre}\n    ")
        else:
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()

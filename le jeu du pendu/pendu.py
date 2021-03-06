# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:13:03 2019

Jeu du Pendu
"""

from random import choice

mystery_word = "" # Mot à trouver
partial_word = "" # Mot recherché
letter = "" # Caractère saisie par le joueur
try_nb = 0 # Nombre d'essaie
words_list = list() # Tous les mots disponibles
go = True # Condition de fin de jeu
found_letter = False


file = open("words_list.txt", "r")
words_list = file.readlines() # Met les mots du fichier dans un liste
file.close()

# Choix du mot mystère
def word_choice(words_list):
    return choice(words_list).rstrip() # Prend au hasard un mot

# Nombre de lettres du mot mystère
def partial_init(mystery_word):
    start_word = "_" * len(mystery_word) # Nombre de lettre = nombre de "_"
    return start_word

# Affichage de ce que le joueur sais (mot partiel)
def word_display(displayed_word):
    displayed_word = str() # Nouvelle variable locale pour l'affichage
    # Répétition qui parcourt chaque lettre numérotée par i (0, 1, 2, 3...)
    for i in range(len(partial_word)):
        displayed_word = displayed_word + " " + partial_word[i]

    print(displayed_word)

# Initialisation du jeu
def hanged_init():
    global words_list, mystery_word, partial_word, try_nb
    try_nb = check_validity_is_a_number(True, 9) # Par défaut le joueur à 9 coups
    mystery_word = word_choice(words_list)
    partial_word = partial_init(mystery_word)
    #print(partial_word)

def check_validity_is_a_number(invalide, int_try):
    while invalide:
        string_entry = input("En combien de coups penses-tu gagner ? => ")
        try: # On essaye de convertir le nombre mais si ça ne marche pas, pas d'erreur ! Direction le 
            int_try = int(string_entry)
            if int_try <= 0:
                print("Mais t'es con ? -> ∀ x ∈ N*")
                
            elif int_try > 35:
                print("Calmes-toi, y a que 26 lettres dans l'alphabet.")
                
            else: # ] 0 ; 35 [
                invalide = False # Pour sortir de la boucle
        except:
            print("Un nombre naturel putain !")

    return int_try

# Saisie du caratère avec vérification
def character_entry():
    letter = "no_entry"
    # La saisie doit comprendre un caractère de l'alphabet (utilisation de la table ASCII)
    while len(letter) != 1 or (not(65 <= ord(letter) <= 89 or 97 <= ord(letter) <= 122)):
        letter = input("Tape une lettre (ou abandonne avec \"?\") : ")
        if letter == "?": # Demande la réponse
            return letter

    letter = letter.lower() # ATTENTION : "lower" met tout en minuscule et "upper" met tout en majuscule
    return letter

# Placement des lettres proposées dans le mot partiel
def letter_place(letter, partial_word, mystery_word):
    global found_letter
    found_letter = False # Remet la variable pour chaque nouvelle lettre testée
    # i prend le numéro de chaque caractère du mot mystère de 0, 1, 2, 3...
    for i in range(len(mystery_word)): # len() compte le nombre de lettre
        # La lettre est dans le mot au numéro i
        if letter == mystery_word[i]:
            # Le mot est coupé en 2, du début jusqu'au rang i
            # Puis, on ajoute le lettre et on ajoute le fin du mot
            partial_word = partial_word[:i] + letter + partial_word[i+1:]
            found_letter = True
            
    return partial_word

# Si une lettre est trouvée, pas de coups en moins
def score(found_letter, try_nb):
    if found_letter == False:
        try_nb -= 1
        
    print("Coups restants :", try_nb)
    return try_nb
    

# On en est-on ?
def end_game(mystery_word, partial_word, try_nb, letter):
    if partial_word == mystery_word:
        print("BRAVO, t'as trouvé le mot :", mystery_word)
        return False

    if letter == "?":
        print("FIN, le mot est :", mystery_word)
        return False

    if try_nb == 0:
        print("PERDU, le mot mystère est :", mystery_word)
        return False

    return True

    # Pas de "else" après "return" !


# Code exécutif

hanged_init()

while go:
    word_display(mystery_word) # Affichage du mot recherché
    letter = character_entry() # Saisir le caractère joué
    partial_word = letter_place(letter, partial_word, mystery_word) # Mot partiel avec les lettres trouvées
    try_nb = score(found_letter, try_nb) # Calcul et affichage des coups
    go = end_game(mystery_word, partial_word, try_nb, letter) # On continue ?

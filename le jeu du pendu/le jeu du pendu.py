# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:49:03 2019

@author: natas
"""

motmystere= ""
morpartiel= ""
lettre= ""
nbcoup = 7
listemots = list()
go = True

fichier = open("listemots.txt", "r")
listemots = fichier.readlines()
fichier.close()

from random import choice

def choixmot(listemots):
    return choice(listemots).rstrip()

def initpartiel(motmystere):
   motdebut = "_"* len(motmystere)
   return motdebut

def affichemot(motpartiel):
    motaffiche = str()
    for i in range(len(motpartiel)):
        motaffiche = motaffiche + " " + motpartiel[i]
    print(motaffiche)
        
def initpendu():
    global listemots, motmystere, motpartiel, nbcoup
    nbcoup = 7
    motmystere = choixmot(listemots)
    motpartiel = initpartiel(motmystere)
    
def saisiecaract():
    lettre = input("taper une lettre de votre choix : ")
    if lettre == "?":
        return lettre
    while len(lettre) != 1 or (not(65 <= ord(lettre) <= 89 or 97 <= ord(lettre) <= 122)):
        lettre = input("taper une lettre de votre choix:")
    lettre = lettre.upper()
    return lettre

def placelettre(lettre,motpartiel):
    for i in range(len(motmystere)):
        if lettre == motmystere[i]:
            motpartiel = motpartiel[:i] + lettre + motpartiel[i+1:]
    return motpartiel
 
def finjeu(motmystere,motpartiel,nbcoup,lettre):
    if motpartiel == motmystere :
        print ("brv, t'as trouver un mot dans ta vie et c'est:", motmystere)
        return False
    if lettre == "?":
        print("fin lol tu veux plus zouer, le mot était:", motmystere)
        return False
    if nbcoup == 0:
        print("perdu rip, le mot était", motmystere)
        return False
    return True
    
initpendu()
while go :
    affichemot(motpartiel)
    lettre = saisiecaract()
    nbcoup -= 1
    print("essais restants :", nbcoup)
    motpartiel = placelettre(lettre,motpartiel)
    go = finjeu(motmystere, motpartiel, nbcoup, lettre)


        
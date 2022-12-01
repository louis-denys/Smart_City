from turtle import *
from Immeubles import *
from random import randint



#On génère une ville, de 6 batiments, d'une hauteur entre 3 et 5, en partant des coordonées (-300, -200)
Ville(
    6,
    Immeuble((3,5), (-300, -200))   
    ).dessine()
 

#On laisse la fenêtre affichée avec done()
done()
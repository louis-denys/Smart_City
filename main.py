from turtle import *
from Immeubles import *
from random import randint
import ctypes

#On récupère les données d'utilisateur depuis le module ctypes.
usr32 = ctypes.windll.user32
hauteur = usr32.GetSystemMetrics(1)

largeur = usr32.GetSystemMetrics(0)



#On génère une ville, de 6 batiments, d'une hauteur entre 3 et 5, en partant des coordonées (-300, -200)
Ville(
    largeur//120,   #La longueur de la ville s'adapte à la taille de l'écran.
    Immeuble((3,(hauteur//50)//2), (-(largeur//2)+25, -(hauteur//2)+125))   
    ).dessine()
 

#On laisse la fenêtre affichée avec done()
done()
from turtle import *

#Inutilisé pour le moment
def est_impair(self, a: int): 
        """
        La fonction prend en paramètre un entier.
        Si l'entier est pair elle renvoie False.
        Si l'entier est impair elle renvoie False.
        """
        if int(str(a)[-1]) in [0,2,4,6,8]:
            return False
        else:
            return True

#Inutilisé pour le moment.
def carre(self, x: int, color: str):
        """
        Dessine un carré de coté x
        """
        begin_fill()
        fillcolor(color)
        for i in range(4):
            forward(x)
            left(90)
        end_fill()

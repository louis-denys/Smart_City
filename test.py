from turtle import *

speed(100)
setpos(0,0)
fd(1000)

def solar_panel(longueur,x,y):
        """
        Dessine un panneau solaire.
        """
        penup()
        setpos(x,y)
        pendown()
        color("#818589")
        begin_fill()
        fillcolor("#818589")
        pos1 = pos()
        fd(longueur*3)
        left(90)
        fd(longueur/2)
        left(90)
        fd(5/4*longueur) #-------
        right(90)
        fd(longueur*5/2)  # coté  barre
        left(90) #TOIT DU PANNEAU
        fd(longueur/2)  # TOIT DU PANNEAU
        left(90) # TOIT DU PANNEAU
        fd(longueur/2)  #coté barre
        z =pos()
        fd(8/4*longueur) # côté barre
        right(90)
        fd(5/4*longueur)#------
        left(90)
        fd(longueur/2)
        penup()
        setpos(z)
        pendown()
        left(135)
        end_fill()
        begin_fill()
        color("#0047AB")
        fillcolor("#0047AB")
        fd(longueur*2)
        left(90)
        fd(longueur/2)
        left(90)
        fd(longueur*4)
        left(90)
        fd(longueur/2)
        left(90)
        fd(longueur*2)
        left(50)
        penup()
        setpos(pos1)
        pendown()
        end_fill()

solar_panel(20, 0,0)
done()
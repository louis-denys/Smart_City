from turtle import *
def porte_en_arc(x, color):
        fillcolor(color)
        begin_fill()
        right(180)
        penup()
        fd(x/2)
        pendown()
        left(90)
        fd(x)
        left(90)
        fd(x/2)
        left(90)
        fd(x)
        left(90)
        penup()
        fd(x/2)
        pendown()
        right(180)
        
        #Arc de cercle:
        penup()
        right(90)
        fd(x/4)
        left(90)
        fd(x/4)
        circle(x/4,extent = 90)
        pendown()
        circle(x/4,extent = 180)


        end_fill()

        left(90)

porte_en_arc(50, 'red')
done()
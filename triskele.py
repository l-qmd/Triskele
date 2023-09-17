from turtle import *

setposition(0,0)


def motif(dim,couleur):
    fillcolor(couleur)
    begin_fill()
    right(60)
    circle(dim,180)
    circle(dim/2,180)
    circle(dim/4,180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/4,-180)
    circle(dim*0.75,-270)
    
    setheading(60)
    
    circle(dim,180)
    circle(dim/2,180)
    circle(dim/4,180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/4,-180)
    circle(dim*0.75,-270)
    
    setheading(180)
    
    circle(dim,180)
    circle(dim/2,180)
    circle(dim/4,180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/8,-180)
    penup()
    circle(dim/8,-180)
    pendown()
    circle(dim/4,-180)
    circle(dim*0.75,-270)
    
    
     
    
    end_fill()
    














# def motif(radius, color1):
#     width(3)
#     color("black", color1)
#     begin_fill()
#     circle(radius/2., 180)
#     circle(radius, 180)
# #     left(180)
# #     circle(-radius/1.2, 180)
# #     circle(-radius/3, 180)
# #     end_fill()
    
    



motif(100,"Black",)

exitonclick()
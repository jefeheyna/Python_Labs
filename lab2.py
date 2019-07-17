#----------------------------------------------------
# This program creates squares that become larger and lighter in shade.
#
# Jeff Hejna
# 9/9/2014
#----------------------------------------------------


import turtle

def main():
    wn = turtle.Screen()  #creates white screen
    bob = turtle.Turtle()  
    bob.speed(0)
    bob.pensize(4)      #allows for smooth overlapping for shading
    for i in range(500):
        shade = (i/500,i/500,i/500) #creates shading that goes from 0 (black) to 1 (white)
        bob.color(shade) 
        bob.forward(i)  #creates the squares
        bob.right(90)

        
main()

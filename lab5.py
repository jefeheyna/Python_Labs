#----------------------------------------------------------
#Lab 5
#Jeff Hejna
#10/7/2014
#-------------------------------------------------------



import turtle
import random
import math

def drawlines(x1,y1,x2,y2, color1,color2,color3):
    '''This function draws the line and assigns the lines the appropriate color.'''
    bob = turtle.Turtle()
    bob.shape("blank")
    bob.speed(0)                 
    bob.color(color1,color2,color3)   #creates the color

    bob.up()
    bob.goto(x1,y1)
    bob.down()      #creates the line
    bob.goto(x2,y2)

def randomnumber():
    '''This function creates a random number to use in the randomlines function.'''
    num=random.randrange(2,5)
    num2=random.randrange(0,2)  #creates random number
    if num2==0:
        num = -1 * num
    return num


def randomlines():
    """draws random lines on the screen that bounce around"""
    width=340
    height=320
    x1=0
    y1=0         
    x2=0
    y2=0
    x1_inc=randomnumber()
    y1_inc=randomnumber()   #various increments of said variables
    x2_inc=randomnumber()
    y2_inc=randomnumber()

    R1=random.random()
    G1=random.random()
    B1=random.random()
    R2=random.random()  #random numbers between 0-1 to use for color changing
    G2=random.random()
    B2=random.random()

    
    color_inc1=(R2-R1)/100
    color_inc2=(G2-G1)/100   #color changing increments
    color_inc3=(B2-B1)/100

    a=0
    while(True):
        
        R1 = R1 + color_inc1
        G1 = G1 + color_inc2  #colors that will be used for the lines
        B1 = B1 + color_inc3

        a = a + 1  # number of lines
        if R1<.01 or R1>.99:
            color_inc1=-color_inc1
        if G1<.01 or G1>.99:
            color_inc2=-color_inc2  #conditions so that color_inc isnt negative
        if B1<.01 or B1>.99:
            color_inc3=-color_inc3
        
        if a >= 1000:
            a = 0
            R1=R2
            G1=G2
            B1=B2
            R2=random.random()
            G2=random.random()
            B2=random.random()
            color_inc1=(R2-R1)/100
            color_inc2=(G2-G1)/100
            color_inc3=(B2-B1)/100
 
        
        x1 = x1 + x1_inc
        if x1>width or x1<-1*width:
            x1_inc = x1_inc * -1
        y1 = y1 + y1_inc
        if y1>height or y1<-1*height:
            y1_inc = y1_inc * -1
        x2 = x2 + x2_inc
        if x2>width or x2<-1*width:   #increments and boundaries for the lines themselves
            x2_inc = x2_inc * -1
        y2 = y2 + y2_inc
        if y2>height or y2<-1*height:
           y2_inc = y2_inc * -1
            
        drawlines(x1,y1,x2,y2, R1, G1, B1)
    
def main():
    '''This main function calls the randomlines function.'''
    randomlines()

main()

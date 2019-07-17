'''
#--------------------------------------------------------------------------------------
# This program calculates the surface area of two houses and then adds these two values 
# together so that the user knows how much paint to buy.
#
# Jeff Hejna
# 9/16/14
#
#                                   Algorithm
#               1)Get user inputs for height,length,width, and gable hieght for house one.
#               2)Calculate areas for section of house (front/back, sides, triangles)
#               3)Add areas together/print result
#               4)Repeat steps 1-3 for second house
#               5)Add surface areas of both houses together/print result
#
#
#-------------------------------------------------------------------------------------
'''
def calcRectArea(length,height):
    '''This function calculates both the front and back area of the house and then returns the
value into the main() function.'''    
    F_BArea = 2*length*height            #calculates front and back areas
    return F_BArea
    
def calcSideArea(width,height):
    '''This function calculates both side areas of the house and then returns the
value into the main() function. '''
    Side_Area = 2*width*height         #calculates both side areas
    return Side_Area
    
def calcTriangleArea(gableheight,width):
    '''This function calculates both areas of the triangles on the house and then returns the
value into the main() function.'''    

    GableArea = gableheight*width       #calculates both gable areas
    return GableArea

def main():
    '''This function asks the user to imput the dimensions of the house (length, width, height,
and gable height). Then, the function calculates the total surface area of the house,
shows the user what the surface area of the house is,and returns the value into the
CompleteArea() function.'''

    length = float(input("What is the length of the house?"))
    print(length)

    width = float(input("What is the width of the house?"))
    print(width)

    height = float(input("What is the height of the house?"))
    print(height)

    gableheight = float(input("What is the gable height?"))
    print(gableheight)

    F_B_Area = calcRectArea(length,height)       
    
    SideArea = calcSideArea(width,height)         
    
    GableArea = calcTriangleArea(gableheight,width)      
    
    TotalArea = F_B_Area + SideArea + GableArea         # calculates total surface area of house
    print("Total for house: ",TotalArea)
    return TotalArea
    


def CompleteArea():
    '''This function calls the main function twice and stores the two house areas into x and y. Then,
the function adds these two values together and shows the user what the total surface area of
the two houses is.'''
    x = main()
    print("Next House...")
    y = main()
    CompleteArea = x+y     #calculates total surface area of both houses
    print("The total area for the two houses is",CompleteArea)

CompleteArea()    



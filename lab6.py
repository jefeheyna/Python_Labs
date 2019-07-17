#---------------------------------------------------------------
# This program takes an image and changes it to the 'hope' style
# Jeff Hejna
# 10/7/2014
#
#                       Algorithm
#           1)Obtain image
#           2)Convert pixels to appropriate color
#           3)Display the image
#
#---------------------------------------------------------------


import cImage as image

def main():
    change_pixels()

def change_pixels():
    img=image.Image("Husky.gif")
    img2=image.EmptyImage(img.getWidth(),img.getHeight())

    win=image.ImageWin()
    win2=image.ImageWin()

    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            pix=img.getPixel(x,y)

            red=pix.getRed()
            green=pix.getGreen()
            blue=pix.getBlue()

            brightness=int(red+green+blue)

            if brightness>=470:
                new_pix=image.Pixel(254,228,169) #converts pixels to new color scheme
            elif brightness>=370:                # depending on brightness.
                new_pix=image.Pixel(112,152,162) 
            elif brightness>=270:
                new_pix=image.Pixel(215,26,33)
            else:
                new_pix=image.Pixel(0,50,77)

            img2.setPixel(x,y,new_pix) #puts appropriate color into pixel 
            

    img.draw(win)
    img2.draw(win2)
    win.exitonclick()
    win2.exitonclick()


main()
    

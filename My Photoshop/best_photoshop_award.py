"""
File: best_photoshop_award.py
Name: 劉亭方
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.225
# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(logo,yvonne):
    for y in range(logo.height):
        for x in range(logo.width):
            yvonne_p=yvonne.get_pixel(x,y)
            avg=(yvonne_p.red+yvonne_p.green+yvonne_p.blue)//3
            total=yvonne_p.red+yvonne_p.green+yvonne_p.blue
            if yvonne_p.green>avg*THRESHOLD and total > BLACK_PIXEL:
                logo_p=logo.get_pixel(x,y)
                yvonne_p.red=logo_p.red
                yvonne_p.blue=logo_p.blue
                yvonne_p.green=logo_p.green
    return yvonne

                        
def main():
    """
    創作理念：STANCODE IS THE BEST!!!
    """
    logo=SimpleImage("C:/Users/方方/OneDrive/桌面/課程/SC001/Assignment4/images/logo.jpg")
    yvonne=SimpleImage("C:/Users/方方/OneDrive/桌面/課程/SC001/Assignment4/images/yvonne.jpg")
    logo.make_as_big_as(yvonne)
    combine_img=combine(logo,yvonne)
    combine_img.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

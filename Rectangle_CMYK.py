import PIL  #Python Imaging Library
from PIL import Image,ImageDraw,ImageFilter # from library import modules needed 

output_dpi = (300.0, 150.0)      # Defined DPI for tiff format 
width = 192                   # width of rectangle in DPI cross process direction
length = 6400                     #Length of rectangle in DPI process direction
start = (0,0)                    # starting x,y coordinates of rectangle
finish = (length,width)          # Ending x,y coordinates of rectangle 
fill = (0,0,0,255)               # rectangle fill color CMYK levels (c,m,y,k) set 0-255 where 0 = no color 255= 100% color
outline = (0,0,0,0)              # rectangle outline color CMYK levels (c,m,y,k) set 0-255 where 0 = no color 255= 100% color


output = Image.new('CMYK',(length,width))
draw = ImageDraw.Draw(output)
draw.rectangle((start,finish),fill ,outline)                      #Rectangle image (xy start corrdinates, XY end corrdinates, Fill color CMYK, Outline color CMYK)
file_name = "c:\\Users\\Michael Olin\\Desktop\\Rectangle_Suave.tif"  # path to save file to

output.save(file_name, dpi=output_dpi, compression="tiff_lzw")

                                                      # file name and DPI information compression of image to use
output.show()
print("done")       # end of program
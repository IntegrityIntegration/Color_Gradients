import os   #operating system interfaces Library
import PIL  #Python Imaging Library
from PIL import Image,ImageDraw,ImageFilter # from library import modules needed 

output_dpi = (300.0, 150.0)      # Defined DPI for tiff format 
width = 19 #192                         # width of rectangle in DPI cross process direction
length = 640 #6400                     #Length of rectangle in DPI process direction
start = (0,0)                    # starting x,y coordinates of rectangle
finish = (length,width)             # Ending x,y coordinates of rectangle 
gradients = 0
fill = (0,0,0,gradients)               # rectangle fill color CMYK levels (c,m,y,k) set 0-255 where 0 = no color 255= 100% color
outline = (0,0,0,0)              # rectangle outline color CMYK levels (c,m,y,k) set 0-255 where 0 = no color 255= 100% color
file_name = "c:\\Users\\Michael Olin\\Desktop\\Rectangle_Save.tif"  # path to save file to
file_name_2 = "c:\\Users\\Michael Olin\\Desktop\\Rectangle_Save_2.tif"  
file_name_new = "c:\\Users\\Michael Olin\\Desktop\\Rectangle_Save_new.tif" 
x = 0
#a = 0

for x in range(0,5760,640):
    for y in range(641,6400,640):
        output = Image.new('CMYK',(length,width))
        draw = ImageDraw.Draw(output)
        draw.rectangle((start,finish),fill ,outline)                      #Rectangle image (xy start corrdinates, XY end corrdinates, Fill color CMYK, Outline color CMYK)
        #a += 640
       # start =(a,width)
       # length += 640
       # width += 19
       # finish = (length,width) 
        #gradients += 25
        fill = (0,0,0,125) #(0,0,0,gradients)
        if x == 0:
            output.save(file_name, dpi=output_dpi, compression="tiff_lzw")
            output.save(file_name_2, dpi=output_dpi, compression="tiff_lzw")
            x = 1
        else:
            file_name = open("c:\\Users\\Michael Olin\\Desktop\\Rectangle_Save.tif", "r")
            file_name_2 = open("c:\\Users\\Michael Olin\\Desktop\\Rectangle_Save_2.tif", "r")
            contents1 = file_name.read()
            contents2 = file_name_2.read()
            file_name_new.write(contents1 + contents2)
            file_name.close()
            file_name_2.close()
            file_name_new.close


            
       # os.rename file_name, file_name_new

        

                                                      # file name and DPI information compression of image to use
output.show()

"""
from PIL import Image

# Create a new image with RGB mode
width, height = 256, 100
image = Image.new('RGB', (width, height))

# Generate the gradient
for x in range(width):
    for y in range(height):
        r = int((x / width) * 255)
        g = int((y / height) * 255)
        b = 128  # Fixed value for blue
        image.putpixel((x, y), (r, g, b))

# Save or display the image
image.show()

"""
# -*- coding: utf-8 -*-
"""
Spyder Editor
pyBMParray
Created by Simon Henley 27-9-15
"""

import sys
import os
from PIL import Image

class location():
    def __init__(self, location_x, location_y, rotation_degs):
        self.location_x = location_x
        self.location_y = location_y
        self.rotation_degs = rotation_degs
        
class pyBMParray():
    def __init__(self, bpp):
        self.bpp = bpp  #define bits per pixel
        self.x_size_final_image =2000;
        self.y_size_final_image =2000;
        #location of script
        self.working_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.template_bmp_filename = "template.bmp"
        self.list_of_positions = []
        self.template = Image.new("1",(100,100)) # temporary definition
        self.location_filename = "Locations.txt"
                
    def make_bmp_array(self):
        #make an image large enough to hold all copies 
        im = Image.new("1",(self.x_size_final_image,self.y_size_final_image),1)               
        #create all locations (from file...) 
        f=open(self.working_dir+"\\"+self.location_filename)
        lines = f.readlines 
        #temp list of locations
        location_1 = location(100,100,30)
        location_2 = location(600,600,60)
        self.list_of_positions.append(location_1)
        self.list_of_positions.append(location_2)
        #create stamp from template file
        self.template = Image.open(self.working_dir+"\\"+self.template_bmp_filename)        
        #paste all locations to 
        for stamp in self.list_of_positions:  
            #overridden rotate method to mask conrers on rotations
            rotated_template = self.rotate(self.template,stamp.rotation_degs, 255) 
            im.paste(rotated_template,(stamp.location_x,stamp.location_y)) 
        im.save(self.working_dir+"\\BMPoutput.bmp")
        
    def rotate(self,image, angle, color, filter=Image.NEAREST):
        if image.mode == "P" or filter == Image.NEAREST:
            matte = Image.new("1", image.size, 1) # mask
        else:
            matte = Image.new("L", image.size, 255) # true matte
        bg = Image.new(image.mode, image.size, color)
        bg.paste(
            image.rotate(angle, filter,expand=0),
            matte.rotate(angle, filter,expand=0)
            )
        return bg    

renderer = pyBMParray("1")
renderer.make_bmp_array()
'''
Created on 6 Nov. 2018

@author: Michael
'''
import sys, os
from PIL import Image
import operator
import numpy as np
from statistics import median

MEDIAN_PIXELS = 1

def process_image(image_path,output_path,median_pixels):
    path,ext = os.path.splitext(image_path)
    with Image.open(image_path) as image:
        pix = image.load()
        
        width, height = image.size
        #width, height = (2,2)
        
        tenpercent = int(width/10)
        
        for i in range(width):
            #First find out which of the surrounding pixels exist
            if not i==0 and i % tenpercent ==0:
                print(int((i/width)*100)+1,"%")
            
            for j in range(height):
                
                selectedPixels = []
                #get all surrounding pixels
                for x in range(-1*median_pixels,median_pixels+1):
                    if i+x >= 0 and i+x < width:
                        for y in range(-1*median_pixels,median_pixels+1):
                            if j+y >= 0 and j+y < height:
                                selectedPixels.append(pix[i+x,j+y])
                
                mat = np.matrix(selectedPixels).transpose().tolist()
                
                pix[i,j] = (int(median(mat[0])),int(median(mat[1])),int(median(mat[2])))
                
                
                
                #print("After: ",i,",",j," : ",pix[i,j])
            
        if ext.upper()==".JPG":
            ext = ".JPEG"
        
        image.save(output_path, ext[1:])

if __name__ == '__main__':
    if len(sys.argv)==2 or len(sys.argv)==3:
        image_path = sys.argv[1]
        if len(sys.argv)==3:
            output_path = sys.argv[2]
        else:
            path,ext = os.path.splitext(image_path)
            output_path = path+'_out'+ext
        print("Processing Image: ",image_path)
        process_image(image_path,output_path,MEDIAN_PIXELS)
        print("Process Finished")
    else:
        print("Usage: python median-filter.py <path_to_image> <optional: output_path>")
        print("If no ouput path is provided, then the output will be named the same but appended with '_out'")
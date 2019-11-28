# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:36:27 2019

@author: suilven
"""
#these are imports
#I make images using tkinter
#from tkinter import *
import tkinter as tk
import math
import os
from PIL import Image
from PIL import ImageDraw

#this gets window ready
window=tk.Tk()
window.title('Animation')

iwidth = 2700
iheight = 1600

c = tk.Canvas(window, height=iheight, width=iwidth)
c.pack()





#this makes an image
str1 = "square"
#draw.text((10, 20), str1, 'black')
#draw.ellipse([100, 150, 300, 250],'black')
#draw.line([50,50,100,100],'black')
step=5
x1=100
y1=100
xe1=220
ye1=140
xe2=320
ye2=140

shift=10
shifteye=10


for i in range(1,10):
    
    image1 = Image.open("images/mars-landscape-1-1200.jpg")
    image1.resize([iwidth,iheight], Image.LANCZOS)
    
    #image1 = Image.new("RGB", (iwidth, iheight), 'white')
    draw = ImageDraw.Draw(image1)
    draw.line([0,0,(i-1)*150,0],'blue')
    draw.line([0,0,0,(i-1)*165],'red')
    
    draw.line([50,50,900,50],'green')
    draw.line([50,50,50,1000],'green')
#for i in range(1,4):
    draw.text((10, 20), str1, 'black')
    step=0
    draw.line([900,950,1100,1050],'red')
    #draw.ellipse([900+i*step, 950+i*step, 1100+i*step, 1050+i*step],'red')
    #draw.ellipse([950+i*step, 1000+i*step, 1150+i*step, 1100+i*step],'blue')
    #draw.ellipse([1000+i*step, 1050+i*step, 1200+i*step, 1150+i*step],'blue')
    #draw.ellipse([1050+i*step, 1100+i*step, 1250+i*step, 1200+i*step],'red')
    

    if i%10==0:
        shifteye=shifteye*-1
    
    
    x1=x1+shift
    xe1=xe1+shifteye+shift
    xe2=xe2+shifteye+shift
    draw.ellipse([x1, y1, x1+400, y1+200],'green')
    draw.ellipse([xe1, ye1, xe1+40, ye1+40],'blue')
    draw.ellipse([xe2, ye2, xe2+40, ye2+40],'blue')
    
    
    
    #if i%10==0:
    #    step=step*-1
    #draw.line([50+i*10,50,100,100],'black')
    filename = "movie-images/aliens"+str(i)+".jpg"
    image1.save(filename)  
    del draw

#ffmpeg documentation https://ffmpeg.org/ffmpeg.html#Examples-1
#ffmpeg command    
#ffmpeg -f image1 -framerate 7 -i foo-%03d.jpeg -s WxH foo.avi
#ffmpeg -f image1 -framerate 7 -i does_it_work%d.jpg foo.avi


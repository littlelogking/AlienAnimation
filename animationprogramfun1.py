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

#functions
#These will make the program neater.

def windowprep(iwidth,iheight):
    window=tk.Tk()
    window.title('Animation')

    c = tk.Canvas(window, height=iheight, width=iwidth)
    c.pack
    
    return window
#this gets window ready
#window=tk.Tk()
#window.title('Animation')

#iwidth = 2700
#iheight = 1600

#c = tk.Canvas(window, height=iheight, width=iwidth)
#c.pack()

iwidth = 2700 
iheight = 1600

window=windowprep(iwidth, iheight)

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

#shift moves the cirles 
shift=10
shifteye=10


x1b=100+700
y1b=100
xe1b=220+700
ye1b=140
xe2b=320+700
ye2b=140

shiftb=-10
shifteyeb=10






#start of loop to draw alien at each time step
for i in range(1,25):
    
    #this adds a backround to the animation
    image1 = Image.open("images/mars-landscape-1-1200.jpg")
    image1.resize([iwidth,iheight], Image.LANCZOS)
    
    #creates the new image
    image1 = Image.new("RGB", (iwidth, iheight), 'white')
    draw = ImageDraw.Draw(image1)
    
    # draws lines but cant see with background on
    #draw.line([0,0,(i-1)*150,0],'blue')
    #draw.line([50,0,0,(i-1)*165],'red')
  
    draw.line([50,50,900,50],'green')
    draw.line([50,50,50,1000],'green')
#for i in range(1,4):
#    draw.text((10, 20), str1, 'black')
#    step=0
#    draw.line([900,950,1100,1050],'red')
    #draw.ellipse([900+i*step, 950+i*step, 1100+i*step, 1050+i*step],'red')
    #draw.ellipse([950+i*step, 1000+i*step, 1150+i*step, 1100+i*step],'blue')
    #draw.ellipse([1000+i*step, 1050+i*step, 1200+i*step, 1150+i*step],'blue')
    #draw.ellipse([1050+i*step, 1100+i*step, 1250+i*step, 1200+i*step],'red')
    

    if i%10==0:
        shifteye=shifteye*-1
        shifteyeb=shifteyeb*-1    
    #this draws the first alien
    x1=x1+shift
    xe1=xe1+shifteye+shift
    xe2=xe2+shifteye+shift
    draw.ellipse([x1, y1, x1+400, y1+200],'green')
    draw.ellipse([xe1, ye1, xe1+40, ye1+40],'blue')
    draw.ellipse([xe2, ye2, xe2+40, ye2+40],'blue')
    
    #TODO   
    #this draws the second alien(b)
    #eyes don't get shifted 
    x1b=x1b+shiftb
    xe1b=xe1b+shifteyeb+shiftb
    xe2b=xe2b+shifteyeb+shiftb
    draw.ellipse([x1b, y1b, x1b+400, y1b+200],'green')
    draw.ellipse([xe1b, ye1b, xe1b+40, ye1b+40],'blue')
    draw.ellipse([xe2b, ye2b, xe2b+40, ye2b+40],'blue')
    
    
    
    #if i%10==0:
    #    step=step*-1
    #draw.line([50+i*10,50,100,100],'black')
    filename = "movie-images/aliens"+str(i)+".jpg"
    image1.save(filename)  
    del draw
    
    #end of loop to draw alien

#ffmpeg documentation https://ffmpeg.org/ffmpeg.html#Examples-1
#ffmpeg command    
#ffmpeg -f image1 -framerate 7 -i foo-%03d.jpeg -s WxH foo.avi
#ffmpeg -f image1 -framerate 7 -i does_it_work%d.jpg foo.avi


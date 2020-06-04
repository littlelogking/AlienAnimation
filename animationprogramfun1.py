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

def initalien(xpos, ypos, siz):
    
    aliendat={ 
    'x': xpos,
    'y': ypos,
    'xe': xpos+120,
    'ye': ypos+40,
    'siz': siz,

    
    #shift moves the cirles 
    'shift': 10,
    'shifteye': 10    
    }    
    
    return aliendat



def initdrawdata():    
    ddata={ 
    'step': 5,
    'x1': 100,
    'y1': 100,
    'xe1': 220,
    'ye1': 140,
    'xe2': 320,
    'ye2': 140,
    
    #shift moves the cirles 
    'shift': 10,
    'shifteye': 10,
    
    
    'x1b': 100+700,
    'y1b': 100,
    'xe1b': 220+700,
    'ye1b': 140,
    'xe2b': 320+700,
    'ye2b': 140,
    
    'shiftb': -10,
    'shifteyeb': 10,
    
    'sx1': 100+350,
    'sy1': 100+50,
    'sxe1': 220+350,
    'sye1': 140+50,
    'sxe2': 320+350,
    'sye2': 140+50,
    
    }
    
    #acces daata item using 
    #ddata['step']
    return ddata

def drawalien(draw,x,y,siz, ddat,i,shift):
    #status=0
    #siz=200
    ddat['siz']=siz
    ddat['x']=x+shift
    ddat['y']=y
    ddat['xe']= x+shift+120
    ddat['ye']= y+40
    ddat['xe2']= x+shift+120+(siz/5)
    ddat['ye2']= y+40        
    
    if i%10==0:
        ddat['shifteye']=ddat['shifteye']*-1
            
    #this draws the first alien
    ddat['xe']=ddat['xe']+ddat['shifteye']
    draw.ellipse([ddat['x'], ddat['y'], ddat['x']+2*ddat['siz'], ddat['y']+ddat['siz']],'green')
    draw.ellipse([ddat['xe'], ddat['ye'], ddat['xe']+(ddat['siz']/5), ddat['ye']+(ddat['siz']/5)],'blue')
    draw.ellipse([ddat['xe2'], ddat['ye2'], ddat['xe2']+(ddat['siz']/5), ddat['ye2']+(ddat['siz']/5)],'blue')
    
    return ddat    

def drawaliena(draw, ddat,i):
    status=0
    if i%40==0:
        ddat['shift']= -ddat['shift']
        
    if i%10==0:
        ddat['shifteye']=ddat['shifteye']*-1
            
    #this draws the first alien
    ddat['x1']=ddat['x1']+ddat['shift']
    ddat['xe1']=ddat['xe1']+ddat['shifteye']+ddat['shift']
    ddat['xe2']=ddat['xe2']+ddat['shifteye']+ddat['shift']
    draw.ellipse([ddat['x1'], ddat['y1'], ddat['x1']+400, ddat['y1']+200],'green')
    draw.ellipse([ddat['xe1'], ddat['ye1'], ddat['xe1']+40, ddat['ye1']+40],'blue')
    draw.ellipse([ddat['xe2'], ddat['ye2'], ddat['xe2']+40, ddat['ye2']+40],'blue')
    
    return status
    
def drawalienb(draw, ddat,i):
    status=0

    #TODO   
    #this draws the second alien(b)
    #eyes don't get shifted
    if i%40==0:
        ddat['shiftb']= -ddat['shiftb']

    
    if i%10==0:
        ddat['shifteyeb']=ddat['shifteyeb']*-1
    ddat['x1b']=ddat['x1b']+ddat['shiftb']
    ddat['xe1b']=ddat['xe1b']+ddat['shifteyeb']+ddat['shiftb']
    ddat['xe2b']=ddat['xe2b']+ddat['shifteyeb']+ddat['shiftb']
    draw.ellipse([ddat['x1b'], ddat['y1b'], ddat['x1b']+400, ddat['y1b']+200],'green')
    draw.ellipse([ddat['xe1b'], ddat['ye1b'], ddat['xe1b']+40, ddat['ye1b']+40],'blue')
    draw.ellipse([ddat['xe2b'], ddat['ye2b'], ddat['xe2b']+40, ddat['ye2b']+40],'blue')

    return status

def drawsuperalien(draw, ddat, i):
    ddat['sx1']=ddat['sx1']
    ddat['sxe1']=ddat['sxe1']
    ddat['sxe2']=ddat['sxe2']
    draw.ellipse([ddat['sx1'], ddat['sy1'], ddat['sx1']+400, ddat['sy1']+200],'red')
    draw.ellipse([ddat['sxe1'], ddat['sye1'], ddat['sxe1']+40, ddat['sye1']+40],'blue')
    draw.ellipse([ddat['sxe2'], ddat['sye2'], ddat['sxe2']+40, ddat['sye2']+40],'blue')
    
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
ddat=initdrawdata()
aliens=initalien(450,100,200)


alien1=initalien(100,100,200)
alien2=initalien(800,100,200)
#this makes an image
str1 = "square"
#draw.text((10, 20), str1, 'black')
#draw.ellipse([100, 150, 300, 250],'black')
#draw.line([50,50,100,100],'black')







#start of loop to draw alien at each time step
for i in range(1,1201):
    
    #this adds a backround to the animation
    image1 = Image.open("images/mars-landscape-1-1200.jpg")
    image1.resize([iwidth,iheight], Image.LANCZOS)
    
    #creates the new image
    #image1 = Image.new("RGB", (iwidth, iheight), 'white')
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
    drawaliena(draw, ddat,i)
    drawalienb(draw, ddat,i)
    
    r=200+(i/18)
    theta=i*math.pi/18
    x=300+r*math.cos((theta))
    y=100+r*math.sin((theta))
    siz=300
    #Draws one-eyed super alien
    aliens=drawalien(draw,x,y,siz, aliens,i,0)
    
    
    #if i%10==0:
    #    step=step*-1
    #draw.line([50+i*10,50,100,100],'black')
    filename = "movie-images/aliens"+str(i)+".jpg"
    image1.save(filename)  
    del draw
    
    #end of loop to draw alien
 
i=i+1
#draw super alien    
#filename = "movie-images/aliens"+str(i)+".jpg"
#image1.save(filename)  
#del draw
    
    #draw explosion steps
#Commands to run to turn into a video
#ffmpeg documentation https://ffmpeg.org/ffmpeg.html#Examples-1
#ffmpeg command    
#ffmpeg -f image1 -framerate 7 -i foo-%03d.jpeg -s WxH foo.avi
#ffmpeg -f image1 -framerate 7 -i does_it_work%d.jpg foo.avi
#ffmpeg -f image2 -framerate 20 -i aliens%d.jpg alienanimation.avi

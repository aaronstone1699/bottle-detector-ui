import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as imag
from PIL import ImageFilter, ImageEnhance
import pytesseract as pt
import os
from tkinter import *
import requests
def win_main():
    print(10)
    
    
    win = Tk()
    win.title("Upload UI")
    #win.geometry("250x250")
    win.configure(background='violet')
    #frame=Frame(win)
    #frame.pack()
    #frame.configure(background='violet')
    api_id=StringVar()
    folder=StringVar()
    image_path=StringVar()
    print(11)
        # this will create a label widget 
    l1 = Label(win, text = "API url") 
    l2 = Label(win, text = "Image location")
    l3 = Label(win, text = "Train/test/val") 
          
        # grid method to arrange labels in respective 
        # rows and columns as specified 
    l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
    l2.grid(row = 1, column = 0, sticky = W, pady = 2)
    l3.grid(row = 2, column = 0, sticky = W, pady = 2) 
          
        # entry widgets, used to take entry from user 
    e1 = Entry(win,textvariable=api_id) 
    e2 = Entry(win,textvariable=folder)
    e3 = Entry(win,textvariable=image_path)
          
        # this will arrange entry widgets 
    e1.grid(row = 0, column = 1, pady = 2) 
    e2.grid(row = 1, column = 1, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)
    print(api_id,image_path,folder)
          
        # checkbutton widget 
    c1 = Button(win, text = "Upload") 
    c1.grid(row = 3, column = 0, sticky = W)
    print(12)

    b1 = Button(win, text = "Labels")
    b1.grid(row = 3, column = 2, sticky = W)
    print(13)
          
        # adding image (remember image should be PNG and not JPG) 
        #img = PhotoImage(file=) 
        #img1 = img.subsample(200, 200) 
          
        # setting image with the help of label 
        #Label(frame, image = img1).grid(row = 0, column = 2, 
               #columnspan = 2, rowspan = 2, padx = 5, pady = 5) 
          
        # button widget 

        #b2 = Button(frame, text = "Zoom out") 
          
        # arranging button widgets 
        #b1.grid(row = 2, column = 2, sticky = E) 
        #b2.grid(row = 2, column = 3, sticky = E)
    print(14)
    win.mainloop()
win_main()

#imports
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as imag
from PIL import ImageFilter, ImageEnhance
import pytesseract as pt
import os
from tkinter import *
import requests

#load the cascade
bottle_cascade=cv2.CascadeClassifier("C:\\Users\\rishik\\Desktop\\New folder\\classifier\\cascade.xml")


#read the image
def load(path):
    img=cv2.imread(path)#path of the image
    #preprocess the image to fit the 256*256 size specified for the classifier
    img=cv2.resize(img,dsize=(256,256))
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return((img,img_gray))


#detect the dimensions of the bottles
def classify(img_gray):
    #crop_dims contains the dimentsions of all the bottles in the format(x,y)the inital point and (w,h)width and height
    crop_dims=bottle_cascade.detectMultiScale(img_gray,1.112,2)
    return(crop_dims)


#crop the images to a list
def crop(crop_dims,img):
    crop_imgs=[]
    for (x,y,w,h) in crop_dims:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi = img[y:y+h, x:x+w]
        crop_imgs.append(img[y:y+h, x:x+w])
    #crop_imgs contains all the cropped images
    return(crop_imgs)

def window_main():
    global api_id,folder,image_path,labelo
    labelo=list()
    win = Tk()
    win.title("Upload UI")
    #win.geometry("250x250")
    win.configure(background='violet')
    frame=Frame(win)
    frame.pack()
    frame.configure(background='violet')
    api_id=StringVar()
    folder=StringVar()
    image_path=StringVar()
    
    # this will create a label widget 
    l1 = Label(frame, text = "API url") 
    l2 = Label(frame, text = "Image location")
    l3 = Label(frame, text = "Train/test/val") 
      
    # grid method to arrange labels in respective 
    # rows and columns as specified 
    l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
    l2.grid(row = 1, column = 0, sticky = W, pady = 2)
    l3.grid(row = 2, column = 0, sticky = W, pady = 2) 
      
    # entry widgets, used to take entry from user 
    e1 = Entry(frame,textvariable=api_id) 
    e2 = Entry(frame,textvariable=folder)
    e3 = Entry(frame,textvariable=image_path)
      
    # this will arrange entry widgets 
    e1.grid(row = 0, column = 1, pady = 2) 
    e2.grid(row = 1, column = 1, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)
      
    # checkbutton widget 
    c1 = Button(frame, text = "Upload",command=upload(api_id.get(),folder.get(),image_path.get(),labelo)) 
    c1.grid(row = 3, column = 0, sticky = W) 
      
    # adding image (remember image should be PNG and not JPG) 
    #img = PhotoImage(file="C:\\Users\\rishik\\Desktop\\69.png") 
    #img1 = img.subsample(200, 200) 
      
    # setting image with the help of label 
    #Label(frame, image = img1).grid(row = 0, column = 2, 
           #columnspan = 2, rowspan = 2, padx = 5, pady = 5) 
      
    # button widget 
    b1 = Button(frame, text = "Labels",command=label(image_path.get())) 
    #b2 = Button(frame, text = "Zoom out") 
      
    # arranging button widgets 
    #b1.grid(row = 2, column = 2, sticky = E) 
    #b2.grid(row = 2, column = 3, sticky = E)

    return win

def label(img):
    if (len(img)>0):
        crop_imgs=crop(classify(load(img)[1]),load(img)[0])
        for i in crop_imgs:
            Window_select(i)
            win2.destroy()
            

def upload(add,pat,img,lab):
    if (len(img)>0):
        crop_imgs=crop(classify(load(img)[1]),load(img)[0])
        for i in range(len(crop_imgs)):
            
            url=add+'\\'+pat+'\\'+lab[i]
            file=crop_imgs[i]
            requests.post(url,files=fle)
            
    
    



def Window_select(img):
    global labs
    win2=Tk()
    win2.title("Select label")
    #win.geometry("250x250")
    win2.configure(background='violet')
    frame2=Frame(win2)
    frame2.pack()
    frame2.configure(background='violet')
    labs=StringVar()
    
    l1 = Label(frame2, text = "Label")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(frame2,textvariable=labs)
    e1.grid(row = 0, column = 1, pady = 2)
    c1 = Button(frame2, text = "Done",command=lappend()) 
    c1.grid(row = 3, column = 0, sticky = W)

    img = PhotoImage(file=img) 
    img1 = img.subsample(200, 200) 
      
    # setting image with the help of label 
    Label(frame2, image = img1).grid(row = 0, column = 2, 
           columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

    return(win2)

def lappend(lab):
    label.append(lab)

window_main()
    

    
    

        
        



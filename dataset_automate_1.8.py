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
bottle_cascade=cv2.CascadeClassifier()


#make the tkinter ui
def make_window():
    global api_id, folder, image_path
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="api id").grid(row=1, column=0, sticky=W)
    api_id = StringVar()
    aid = Entry(frame1, textvariable=api_id)
    aid.grid(row=1, column=1, sticky=W)

    Label(frame1, text="image address").grid(row=2, column=0, sticky=W)
    image_path = StringVar()
    image = Entry(frame1, textvariable=image_path)
    image.grid(row=2, column=1, sticky=W)
    
    Label(frame1, text="train/test/val").grid(row=3, column=0, sticky=W)
    folder = StringVar()
    locate = Entry(frame1, textvariable=folder)
    locate.grid(row=3, column=1, sticky=W)

    frame2 = Frame(win)      
    frame2.pack()
    b1 = Button(frame2, text=" upload  ",command=upload)

    b1.pack(side=LEFT)


    frame3 = Frame(win)      
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win



#read the image
def load(path):
    img=cv2.imread(path)#path of the image
    #preprocess the image to fit the 256*256 size specified for the classifier
    img=cv2.resize(img,dsize=(256,256))
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return((img,img_gray))

#detect the dimensions of the bottles
def detect(img_gray):
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

#detect text from label
def detect_text(crop_imgs):
    #detecting the label text
    crop_imgs_prepro=[]
    img=imag.fromarray(crop_imgs)
    img = img.convert('L')
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.convert('1')
    crop_imgs_prepro.append(img)
    imagetext = pt.image_to_string(img)
    img_label = imagetext
    return(img_label)

#upload to the specified location
def upload():
    crop_imgs=crop(detect(load(image_path.get())[1]),load(image_path.get())[0])
    #img_labels contain all the labels of the images

    for i in range(len(crop_imgs)):
        url = (api_id.get()+'/'+folder.get()+'/'+detect_text(crop_imgs[i]))
        # folderpath is one of(train,test,val) which would be taken from the user
        files = {crop_imgs[i]}
        requests.post(url, files=files)


make_window()

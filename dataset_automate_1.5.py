import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract as pt
import os
from tkinter import *
import easyapiio

def make_window():
    global api_key, api_id, folder, image_path
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="api key").grid(row=0, column=0, sticky=W)
    api_key = StringVar()
    key = Entry(frame1, textvariable=api_key)
    key.grid(row=0, column=1, sticky=W)

    Label(frame1, text="api id").grid(row=1, column=0, sticky=W)
    api_id = StringVar()
    aid = Entry(frame1, textvariable=api_id)
    aid.grid(row=1, column=1, sticky=W)

    Label(frame1, text="image address").grid(row=2, column=0, sticky=W)
    image_path = StringVar()
    image = Entry(frame1, textvariable=image_path)
    image.grid(row=2, column=1, sticky=W)
    
    Label(frame1, text="train/test/val").grid(row=2, column=0, sticky=W)
    folder = StringVar()
    locate = Entry(frame1, textvariable=folder)
    locate.grid(row=2, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2, text=" upload  ", command=upload)

    b1.pack(side=LEFT)


    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win



# load the bottle_cascade
bottle_cascade=cv2.CascadeClassifier(/path1)#path of the cascade

img=cv2.imread(/path2)#path of the image

#preprocess the image to fit the 500*500 size specified for the classifier
img=cv2.resize(img,dsize=(500,500))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#crop_dims contains the dimentsions of all the bottles in the format(x,y)the inital point and (w,h)width and height
crop_dims=bottle_cascade.detectMultiScale(img_gray,1.112,2)

def crop():
    crop_imgs=[]
    for (x,y,w,h) in crop_imgs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi = img[y:y+h, x:x+w]
        crop_imgs.append(img[y:y+h, x:x+w])
    #crop_imgs contains all the cropped images

def detect_text():
    #detecting the label text
    crop_imgs_prepro=[]
    img_labels=[]
    for i in range(len(crop_imgs)):
        img=Image.fromarray(crop_imgs[i])
        img = img.convert('L')
        img = img.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        img = img.convert('1')
        crop_imgs_prepro.append(img)
        imagetext = pt.image_to_string(img)
        img_labels.append(imagetext)

def upload():
    #img_labels contain all the labels of the images

    for i in range(len(crop_imgs)):
        path = ('path/',folderpath,'/',img_labels[i]) # folderpath is one of(train,test,val) which would be taken from the user
        #saving the cropped images in folders
        cv2.imwrite(os.path.join(path , str(i), crop_imgs[i])



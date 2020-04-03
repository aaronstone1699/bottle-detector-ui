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


#make the tkinter ui
def make_window():
    global api_id, folder, image_path ,labs
    win = Tk()
    
    win.title("UI")
    win.geometry("500x500")
    win.configure(background='violet')

    frame1 = Frame(win)
    frame1.pack()
    
    frame1.configure(background='violet')

    Label(frame1, text="api id").grid(row=1, column=0, padx=2,pady=2)
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
    
    
    b1 = Button(frame1, text=" upload  ",command=upload)
    b1.grid(row=4, column=1, sticky=W)
    b1.configure(background='darkviolet')

    
    var = IntVar()
    button = Button(frame1, text="Click Me", command=lambda: var.set(1))
    button.grid(row=5, column=1, sticky=W)
    button.configure(background='darkviolet')

    button.wait_variable(var)

 
    Label(frame1, text="label").grid(row=8, column=0, sticky=W)
    labs = StringVar()
    locate = Entry(frame1, textvariable=labs)
    locate.grid(row=8, column=1, sticky=W)

    labo = IntVar()
    button = Button(frame1, text="name", command=lambda: labo.set(1))
    button.grid(row=9, column=1, sticky=W)
    button.configure(background='darkviolet')



    canvas = Canvas(frame1,  width=256, height=256)
    canvas.grid(row=10,column=1,sticky=W)


    img = PhotoImage(Image.open("C:\\Users\\rishik\\Desktop\\2.jpg"))
    canvas.create_image(10, 10, anchor=NW, image=img)



    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=6)
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
#def detect_text(crop_imgs):
#    detecting the label text
#    crop_imgs_prepro=[]
#    img=imag.fromarray(crop_imgs)
#    img = img.convert('L')
#    img = img.filter(ImageFilter.MedianFilter())
#    enhancer = ImageEnhance.Contrast(img)
#    img = enhancer.enhance(2)
#    img = img.convert('1')
#    crop_imgs_prepro.append(img)
#    imagetext = pt.image_to_string(img)
#    img_label = imagetext
#    return(img_label)

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

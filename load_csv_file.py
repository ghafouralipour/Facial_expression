import numpy as np
import math  
import cv2
import csv
import pandas as pd

def load_fer2013():
    width,height = 194,194
    image_size=(48,48)
    faces = []
    emotions=[]
    with open("image_dataset_file.csv", "r") as f:
        csv_reader = reader(f)
        i=0
        for row in csv_reader:
            if i>0 :
                str = row[1]
                face  = str.split(' ')
                for i in range(0, len(face)): 
                    face[i] = int(face[i]) 
                face= np.asanyarray(face).reshape(width,height)
                face = cv2.resize(face.astype('uint8'),image_size)
                faces.append(face.astype('float32'))
                emotions.append(row[0])    
            i+=1

    emotions = pd.get_dummies(emotions).values
    return faces,emotions
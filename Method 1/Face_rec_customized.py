#Face rec using OpenCV
import cv2
import os
import numpy as np
from PIL import Image
from pathlib import Path
###
# For face DETECTION we will use the Haar Cascade provided by OpenCV.
cascade_path = "/Users/jatinsethi/Downloads/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascade_path)
###
# For face RECOGNITION we will the the LBPH Face Recognizer 
recognizer = cv2.face.createLBPHFaceRecognizer()
###
images_folder_path = './yale_faces'
images_folder_for_testing = './yale_faces'

Import_savedModel = False

def learning_images_paths(path):
    image_paths = [os.path.join(path, f) \
                   for f in os.listdir(path) if not f.endswith('.sad')]
    return image_paths

def image_to_numpy(image_paths):
    if not Import_savedModel:
        image_paths = learning_images_paths(images_folder_path)
    
    images_numpy = []
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        #Find a better way than converting to uint8
        image = np.array(image_pil, 'uint8')
        images_numpy.append(image)
        
    return images_numpy

def detecting_faces(images_numpy):
    if not Import_savedModel:
        images_numpy = image_to_numpy()
    
    faces = []
    labels = []
    for image in images:
        face = faceCascade.detectMultiScale(image)
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        for (x, y, w, h) in face:
            faces.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            
    return faces, labels

def training(faces, labels):
    faces, labels = detecting_faces()
    recognizer.train(faces, np.array(labels))

def recognizing_image_paths(path):
    image_paths_for_testing = [os.path.join(path, f) \
                               for f in os.listdir(path) if f.endswith('.sad')]
    return image_paths_for_testing

def recognizing(image_paths_for_testing):
    image_paths_for_testing = recognizing_image_paths(images_folder_for_testing)
    for image_path in image_paths_for_testing:        
        predict_image_pil = Image.open(image_path).convert('L')
        predict_image = np.array(predict_image_pil, 'uint8')
        faces = faceCascade.detectMultiScale(predict_image)

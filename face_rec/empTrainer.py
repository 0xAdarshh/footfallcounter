import cv2,os
import numpy as np
from PIL import Image
import dlib


def train():
    print("asdsdhbsbkfbkhdbfkbfksd")
    path_rec=os.path.join(os.getcwd(), 'face_rec\\recognizers\\face-trainner.yml')
    data_path=os.path.join(os.getcwd(), 'face_rec\\dataset')

    # print(path_rec)
    # print(data_path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #detector= cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml");
    detector = dlib.get_frontal_face_detector()

    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths[0])
        #create empth face list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:

            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[0][1])
            # extract the face from the training image sample
            #faces=detector.detectMultiScale(imageNp)
            faces = detector(imageNp, 0)
            #If a face is there then append that in the list as well as Id of it
            #for (x,y,w,h) in faces:
            for i, d in enumerate(faces):     
                faceSamples.append(imageNp[d.top(): d.bottom(),d.left():d.right()])
                Ids.append(Id)
        return faceSamples,Ids

    print("asdsdhbsbkfbkhdbfkbfksdopopopppoopoop")
    faces,Ids = getImagesAndLabels(data_path)
    recognizer.train(faces, np.array(Ids))

    recognizer.write(path_rec)
    print("Trainned Successfully..")
import cv2, os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    # Get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        # Load the image and convert it to grayscale
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        # Get the ID from the image filename
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # Detect the face in the image
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

faces, Ids = getImagesAndLabels('TrainingImage')
if len(faces) > 0:
    recognizer.train(faces, np.array(Ids))
    if not os.path.exists('TrainingImageLabel'):
        os.makedirs('TrainingImageLabel')
    recognizer.save('TrainingImageLabel/trainner.yml')
    print("Model trained and saved successfully.")
else:
    print("No images found in TrainingImage folder.")
# let's Starts By Importing required Libraries
import cv2
import argparse


#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required= True ,type = str, help = "path to the (optional) video file")
ap.add_argument("-x", "--cascades", required= True , help = "path to the cascade file")
args = vars(ap.parse_args())
# capture frames from a video
cap = cv2.VideoCapture(args["video"])

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier(args["cascades"])

# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('sKSama', frames )
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()

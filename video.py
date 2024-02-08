import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from tkinter import *
import tkinter as tk

def home_page():
    root.destroy()
    import start


root = Tk()
root.geometry("300x300")
root.title("EXPRESSIFY")
root.state('zoomed')

Home = Button(root, height=2,
                 width=20,
                 text="Home",
                 command=lambda: home_page())
Home.pack()

l1 = Label(root, text="To print Alphabets \n one-by-one click button below", font='Helvetica 20 bold').place(relx=0.50, rely=0.10,
                                                                                                anchor=N)
T = Text(root, height=30, width=70)
Display = Button(root, height=2,
                 width=20,
                 text="Start Video",
                 command=lambda: startVideo()).place(relx=0.50, rely=0.25,anchor=N)


def startVideo():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

    offset = 20
    imgSize = 300

    folder = "Data/Z"
    counter = 0
    wait = 0
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]

    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)


            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)

            wait = wait + 1
            if wait == 40:
                print(labels[index])
                wait = 0
                # p = Label(root, text=labels[index])
                # p.pack(side=LEFT, pady=10)
                T.insert(tk.END, labels[index])
                break

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                          (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                          (x + w + offset, y + h + offset), (255, 0, 255), 4)

        cv2.imshow("Image", imgOutput)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()




T.pack(side=BOTTOM)
mainloop()

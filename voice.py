import tkinter as tk
from datetime import time
import time
from tkinter import *
from tkinter import font
import speech_recognition as sr
import pyttsx3


def home_page():
    frame.destroy()
    import start


# Top level window
frame = tk.Tk()
frame.title("EXPRESSIFY")
frame.geometry('400x200')
frame.state('zoomed')

Home = Button(frame, height=2,
              width=20,
              text="Home",
              command=lambda: home_page())
Home.pack()

l1 = Label(frame, text="To Display ASL write below \n and click button below", font='Helvetica 20 bold')
l1.pack()


# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    inp = inp.lower()
    for i in inp:
        if i == 'a':
            img = PhotoImage(file="Voice/A.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'b':
            img = PhotoImage(file="Voice/B.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'c':
            img = PhotoImage(file="Voice/C.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'd':
            img = PhotoImage(file="Voice/D.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'e':
            img = PhotoImage(file="Voice/E.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'f':
            img = PhotoImage(file="Voice/F.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'g':
            img = PhotoImage(file="Voice/G.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'h':
            img = PhotoImage(file="Voice/H.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'i':
            img = PhotoImage(file="Voice/I.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'j':
            img = PhotoImage(file="Voice/J.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'k':
            img = PhotoImage(file="Voice/K.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'l':
            img = PhotoImage(file="Voice/L.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'm':
            img = PhotoImage(file="Voice/M.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'n':
            img = PhotoImage(file="Voice/N.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'o':
            img = PhotoImage(file="Voice/O.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'p':
            img = PhotoImage(file="Voice/P.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'q':
            img = PhotoImage(file="Voice/Q.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'r':
            img = PhotoImage(file="Voice/R.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 's':
            img = PhotoImage(file="Voice/S.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 't':
            img = PhotoImage(file="Voice/T.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'u':
            img = PhotoImage(file="Voice/U.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'v':
            img = PhotoImage(file="Voice/V.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'w':
            img = PhotoImage(file="Voice/W.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'x':
            img = PhotoImage(file="Voice/X.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'y':
            img = PhotoImage(file="Voice/Y.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'z':
            img = PhotoImage(file="Voice/Z.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=10,
                   width=50)

inputtxt.pack()


#########################################################################################################
def voice_text():
    r = sr.Recognizer()

    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        print(MyText)
    l2 = Label(frame, text=MyText,
               font='Helvetica 20 bold')
    l2.pack()

    for i in MyText:
        if i == 'a':
            img = PhotoImage(file="Voice/A.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'b':
            img = PhotoImage(file="Voice/B.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'c':
            img = PhotoImage(file="Voice/C.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'd':
            img = PhotoImage(file="Voice/D.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'e':
            img = PhotoImage(file="Voice/E.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'f':
            img = PhotoImage(file="Voice/F.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'g':
            img = PhotoImage(file="Voice/G.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'h':
            img = PhotoImage(file="Voice/H.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'i':
            img = PhotoImage(file="Voice/I.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'j':
            img = PhotoImage(file="Voice/J.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'k':
            img = PhotoImage(file="Voice/K.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'l':
            img = PhotoImage(file="Voice/L.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'm':
            img = PhotoImage(file="Voice/M.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'n':
            img = PhotoImage(file="Voice/N.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'o':
            img = PhotoImage(file="Voice/O.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'p':
            img = PhotoImage(file="Voice/P.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'q':
            img = PhotoImage(file="Voice/Q.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'r':
            img = PhotoImage(file="Voice/R.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 's':
            img = PhotoImage(file="Voice/S.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 't':
            img = PhotoImage(file="Voice/T.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'u':
            img = PhotoImage(file="Voice/U.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'v':
            img = PhotoImage(file="Voice/V.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'w':
            img = PhotoImage(file="Voice/W.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'x':
            img = PhotoImage(file="Voice/X.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'y':
            img = PhotoImage(file="Voice/Y.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)
        elif i == 'z':
            img = PhotoImage(file="Voice/Z.png").subsample(x='5', y='5')
            lbl.configure(image=img)
            lbl.update()
            time.sleep(1)

    l2.after(100, l2.destroy())


#################################################################################################################

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
# Button Creation

voiceButton = tk.Button(frame,
                        text="Voice",
                        command=voice_text, font=buttonFont).place(x=1050, y=150)

printButton = tk.Button(frame,
                        text="Show",
                        command=printInput, font=buttonFont)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()

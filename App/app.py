from tkinter import *
import tkinter.font
import PIL
from PIL import Image, ImageTk
import protocol as protocol
import camera as cam
import pytesseract
import cv2
from opentrons import instruments, containers, robot
from opentrons.util import environment
import test

'''
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)'''

OPTIONS = [
"Run One Plate",
"Run Two Plates",
"Run Three Plates"
]

def betatestrun():
	photo4 = Image.open('petri1.png')
	photo5 = Image.open('petri2.png')
	photo6 = Image.open('petri3.png')
	photo4 = cv2.imread("petri1.png", cv2.IMREAD_GRAYSCALE)
	photo5 = cv2.imread("petri2.png", cv2.IMREAD_GRAYSCALE)
	photo6 = cv2.imread("petri3.png", cv2.IMREAD_GRAYSCALE)
	photoary = [photo4, photo5, photo6]
	optionget = variable.get()
	if optionget == OPTIONS[0]:
		protocol.btest(1, photoary)
	elif optionget == OPTIONS[1]:
		protocol.btest(2, photoary)
	else:
		protocol.btest(3, photoary)




def chng():
	photo1 = Image.open('opencv_frame_0.png')
	photo2 = Image.open('opencv_frame_1.png')
	photo3 = Image.open('opencv_frame_2.png')

	photo1 = photo1.resize((300,300),Image.ANTIALIAS)
	photo2 = photo2.resize((300,300),Image.ANTIALIAS)
	photo3 = photo3.resize((300,300),Image.ANTIALIAS)


	photo1=ImageTk.PhotoImage(photo1)
	photo2=ImageTk.PhotoImage(photo2)
	photo3=ImageTk.PhotoImage(photo3)

	panel1.config(image = photo1)
	panel2.config(image = photo2) 
	panel3.config(image = photo3) 


	photo1.photo_ref1 = photo1 # keep a reference
	photo2.photo_ref2 = photo2
	photo3.photo_ref3 = photo3

def chng2():
	photo4 = Image.open('petri1.png')
	photo5 = Image.open('petri2.png')
	photo6 = Image.open('petri3.png')

	photo4 = photo4.resize((300,300),Image.ANTIALIAS)
	photo5 = photo5.resize((300,300),Image.ANTIALIAS)
	photo6 = photo6.resize((300,300),Image.ANTIALIAS)

	photo4=ImageTk.PhotoImage(photo4)
	photo5=ImageTk.PhotoImage(photo5)
	photo6=ImageTk.PhotoImage(photo6)

	panel4.config(image = photo4)
	panel5.config(image = photo5) 
	panel6.config(image = photo6) 


	photo4.photo_ref1 = photo4 # keep a reference
	photo5.photo_ref2 = photo5
	photo6.photo_ref3 = photo6


window = Tk()
window.title("42Robotics Opentrons")
window.configure(background='white')
window.geometry("900x750")


photo1=Image.open('logo.png')
photo1=photo1.resize((300,300),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(photo1)


def betatest():
	test.betacameraphotos()
	#photo4 = Image.open('opencv_frame_0.png')
	#photo5 = Image.open('opencv_frame_1.png')
	#photo6 = Image.open('opencv_frame_2.png')
	chng2()


#test photo
#testphoto = Image.open('Circles-3.gif')
#testphoto = testphoto.resize((300,300),Image.ANTIALIAS)
#testphoto=ImageTk.PhotoImage(testphoto)


#photo1 = PhotoImage(file="ez.gif")
panel1 = Label (window, image=photo1, fg= "black") 
panel1.grid(row=1, column=0)
panel2 =Label (window, image=photo1, fg="black") 
panel2.grid(row=1, column=1)
panel3 = Label (window, image=photo1, fg="black") 
panel3.grid(row=1, column=2)

#dg.hello()

#init the photos and home the machine
def init():
	protocol.initall()
	cam.capturepetri()
	chng()
	print("done")

initbutton = Button(window, text="Init Robot", command=init)
initbutton.grid(row=2, column = 0, sticky=E)

'''
# this displays webcam, some problems there so dont use it for now
width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

lmain = Label(window)
lmain.grid(row=3, column=0)
show_frame()'''


#placeholder for button to select protocol

def ok():
	optionget = variable.get()
	print("selection is " + optionget)
	if optionget == OPTIONS[0]:
		protocol.mainprogram(1)
	elif optionget == OPTIONS[1]:
		protocol.mainprogram(2)
	else:
		protocol.mainprogram(3)
	cam.capturepetri()
	chng() 


variable = StringVar(window)
variable.set(OPTIONS[0])
dropdown = OptionMenu(window, variable, *OPTIONS)
dropdown.grid(row=2, column=1, sticky= E)

button = Button(window, text="Start", command=ok)
button.grid(row=2, column =2, sticky=W)

#beta thing
panel4 = Label (window, image=photo1, fg= "black") 
panel4.grid(row=4, column=0)
panel5 =Label (window, image=photo1, fg="black") 
panel5.grid(row=4, column=1)
panel6 = Label (window, image=photo1, fg="black") 
panel6.grid(row=4, column=2)

bottompanels = [panel4, panel5, panel6]

betabutton = Button(window, fg="Red", text="Beta Test MV", command = betatest)
betabutton.grid(row=3, column = 0, sticky=W)

betabutton = Button(window, fg="Red", text="Run Beta Test", command = betatestrun)
betabutton.grid(row=3, column = 1, sticky=E)


window.mainloop()

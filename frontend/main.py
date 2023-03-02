import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk
from tkinter import ttk

from abaRelatorio import *

cancel = False

def prompt_ok(event=0):
    global cancel, btn_esq, btn_dir , button1, button2
    cancel = True

    btn_esq.place_forget()
    btn_dir.place_forget()
    button1 = tk.Button(mainWindow, text="Good Image!", command=saveAndExit)
    button2 = tk.Button(mainWindow, text="Try Again", command=resume)
    button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
    button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
    button1.focus()

def saveAndExit(event=0):
    global prevImg

    if (len(sys.argv) < 2):
        filepath = "imageCap.png"
    else:
        filepath = sys.argv[1]

    print("Output file to: " + filepath)
    prevImg.save(filepath)
    resume()

def resume(event=0):
    global button1, button2, btn_esq, btn_dir, lmain, cancel

    cancel = False

    button1.place_forget()
    button2.place_forget()

    mainWindow.bind('<Return>', prompt_ok)
    btn_esq.place(bordermode=tk.INSIDE, relx=0.25, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    btn_dir.place(bordermode=tk.INSIDE, relx=0.75, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    lmain.after(10, show_frame)

def gerar_relatorio():
    global btn_esq, btn_dir, lmain, cancel, mainWindow

    cancel = False
    btn_esq.place_forget()
    btn_dir.place_forget()

    novaJanela()

cap = cv2.VideoCapture(0)
capWidth = cap.get(3)
capHeight = cap.get(4)

success, frame = cap.read()

mainWindow = tk.Tk(screenName="Camera Capture")
mainWindow.title('main')
mainWindow.geometry('{}x{}'.format(900, 700))
mainWindow.minsize(900, 700)
mainWindow.maxsize(900, 700)

mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
lmain = tk.Label(mainWindow, compound=tk.CENTER, anchor=tk.CENTER, relief=tk.RAISED, width=900, height=600)
btn_esq = tk.Button(mainWindow, text="Capture", command=prompt_ok)
btn_dir = tk.Button(mainWindow, text="gerar relatório", command=gerar_relatorio)

lmain.grid(row=0, column=0)
btn_esq.place(bordermode=tk.INSIDE, relx=0.25, rely=0.9, anchor=tk.CENTER, width=300, height=50)
btn_dir.place(bordermode=tk.INSIDE, relx=0.75, rely=0.9, anchor=tk.CENTER, width=300, height=50)
#button.focus()

def show_frame():
    global cancel, prevImg, btn_esq, btn_dir

    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if not cancel:
        lmain.after(10, show_frame)

show_frame()
mainWindow.mainloop()
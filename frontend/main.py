import tkinter as tk
import os
import cv2
import sys
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
from datetime import date
from bancoDados.clientes_db import  *
from abaRelatorio import *
from recognition import *

password = "senha"
database = "project_rt"
db = BancoDados(host="localhost", user="root", password=password, database=database)
db.connect()
client_db = Clientes_DB(db)


client_db.createTableClients()

cancel = False
name = None
process_this_frame = False
cap =None

#https://webninjadeveloper.com/python/python-3-opencv-tkinter-project-to-capture-webcam-save-it-as-png-image-file-using-pillow-library-gui-desktop-app/

def prompt_ok(event=0):
    global cancel, btn_esq, btn_dir , button1, button2, name, cap
    cancel = True
    process_this_frame = True

    _, frame = cap.read()
    frame, name = recognize(frame, process_this_frame)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

    print("nome armazenado: "+name)
    btn_esq.place_forget()
    btn_dir.place_forget()
    button1 = tk.Button(mainWindow, text="Good Image!", command=RegistrarFuncionrio)
    button2 = tk.Button(mainWindow, text="Try Again", command=resume)
    button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
    button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
    button1.focus()

def RegistrarFuncionrio(event=0):
    global button1, button2, btn_esq, btn_dir, lmain, cancel

    cancel = False

    password = "root"
    database = "project_rt"
    db = BancoDados(host="localhost", user="root", password=password, database=database)
    db.connect()
    #print(db.connection)
    client_db = Clientes_DB(db)
    register_db = Registro_DB(db)

    lista_funcionarios = client_db.allClientsName()
    #print(lista_funcionarios)
    id_client = 1
    tem_funcionario= False
    for nome in lista_funcionarios:
        if name in nome:
            tem_funcionario = True
            break
        id_client+=1

    button1.place_forget()
    button2.place_forget()

    mainWindow.bind('<Return>', prompt_ok)
    btn_esq.place(bordermode=tk.INSIDE, relx=0.25, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    btn_dir.place(bordermode=tk.INSIDE, relx=0.75, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    lmain.after(10, show_frame)

    if tem_funcionario :
        print("true")
        date_now = datetime.now()
        new_register = Registro(id_client, date_now, "Entrada")
        register_db.insertRegister(new_register)
        print(register_db.lastRegister(id_client))
        new_win = tk.Toplevel()
        new_win.title("confirmação de registro")
        new_win.geometry('{}x{}'.format(80, 80))
        new_win.minsize(80, 80)
        new_win.maxsize(80, 80)
        model_label = tk.Label(new_win, text='Acesso liberado')
        model_label.grid(row=0, column=0)
        button_ok = tk.Button(new_win, text="OK", command=new_win.destroy)
        button_ok.grid(row=1, column=0, pady=5, sticky=tk.E)
        #new_win.after(1500, new_win.destroy())

    else:
        print("false")
        new_win = tk.Toplevel()
        new_win.title("confirmação de registro")
        new_win.geometry('{}x{}'.format(80, 80))
        new_win.minsize(80, 80)
        new_win.maxsize(80, 80)
        model_label = tk.Label(new_win, text='Acesso Negado')
        model_label.grid(row=0, column=0)
        button_ok = tk.Button(new_win, text="OK", command=new_win.destroy)
        button_ok.grid(row=1, column=0, pady=5, sticky=tk.E)
        #new_win.after(1500, new_win.destroy())

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
    global cancel, prevImg, btn_esq, btn_dir, name

    _, frame = cap.read()
    frame, name = recognize(frame, process_this_frame=True)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if not cancel:
        lmain.after(10, show_frame)

show_frame()
mainWindow.mainloop()
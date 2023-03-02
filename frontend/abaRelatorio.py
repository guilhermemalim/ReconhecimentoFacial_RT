import tkinter as tk
from tkinter import ttk
from bancoDados import *
from bancoDados.banco_dados import BancoDados
from bancoDados.cliente import Cliente
from bancoDados.clientes_db import Clientes_DB
from bancoDados.registro import Registro
from bancoDados.registros_db import Registro_DB
from datetime import datetime
from datetime import date

# https://pt.stackoverflow.com/questions/23053/ajuda-tables-python27 -> table
# https://www.plus2net.com/python/tkinter-OptionMenu.php -> choose

def create_navigation(top_frame):
    options = tk.StringVar(top_frame)
    options.set(" ")  # default value

    l3 = tk.Label(top_frame, text='Selecione o funcionário', width=35)
    l3.grid(row=0, column=1)

    om1 = tk.OptionMenu(top_frame, options, "HTML", "PHP", "MySQL", "Python")
    om1.grid(row=0, column=2)

def atualizar_table(tree, register_db):
    data = [
        ("Argentina", "Buenos Aires", "ARS"),
        ("Australia", "Canberra", "AUD"),
        ("Brazil", "Brazilia", "BRL"),
        ("Canada", "Ottawa", "CAD"),
        ("China", "Beijing", "CNY"),
        ("France", "Paris", "EUR"),
        ("Germany", "Berlin", "EUR"),
        ("India", "New Delhi", "INR"),
        ("Italy", "Rome", "EUR"),
        ("Japan", "Tokyo", "JPY"),
        ("Mexico", "Mexico City", "MXN"),
        ("Russia", "Moscow", "RUB"),
        ("South Africa", "Pretoria", "ZAR"),
        ("United Kingdom", "London", "GBP"),
        ("United States", "Washington, D.C.", "USD"),
    ]

    #
    # Insere cada item dos dados
    for item in data:
        tree.insert('', 'end', values=item)

def create_table(center, register_db):

    # Inicia o Treeview com as seguintes colunas:
    dataCols = ('NOME', 'DATA', 'HORA', 'PRIORIDADE')
    tree = ttk.Treeview(center, columns=dataCols, show='headings')
    tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

    # Barras de rolagem
    ysb = ttk.Scrollbar(center, orient=tk.VERTICAL, command=tree.yview)
    xsb = ttk.Scrollbar(center, orient=tk.HORIZONTAL, command=tree.xview)
    tree['yscroll'] = ysb.set
    tree['xscroll'] = xsb.set
    ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
    xsb.grid(row=1, column=0, sticky=tk.E + tk.W)

    # Define o textos do cabeçalho (nome em maiúsculas)
    for c in dataCols:
        tree.heading(c, text=c.title())

    atualizar_table(tree, register_db)

def novaJanela():
    new_win = tk.Toplevel()
    new_win.title("Nova Janela")

    password = "root"
    database = "project_rt"
    db = BancoDados(host="localhost", user="root", password=password, database=database)
    db.connect()
    # client_db = Clientes_DB(db)
    register_db = Registro_DB(db)
    id_client = 1

    # layout all of the main containers
    new_win.grid_rowconfigure(1, weight=1)
    new_win.grid_columnconfigure(0, weight=1)

    top_frame = tk.Frame(new_win, width=450, height=50, pady=3)
    top_frame.grid(row=0, sticky="ew")

    create_navigation(top_frame)

    center = tk.Frame(new_win, width=50, height=40, padx=3, pady=3)
    center.grid(row=1, sticky="nsew")
    create_table(center, register_db)

    button_ok = tk.Button(new_win, text="OK", command=new_win.destroy)
    button_ok.grid(row=2, column=0, pady=5, sticky=tk.E)

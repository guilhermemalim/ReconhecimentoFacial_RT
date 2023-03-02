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

def novaJanela():
    new_win = tk.Toplevel()
    new_win.title("Nova Janela")



    # Inicia o Treeview com as seguintes colunas:
    dataCols = ('country', 'capital', 'currency')
    tree = ttk.Treeview(new_win, columns=dataCols, show='headings')
    tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

    # Barras de rolagem
    ysb = ttk.Scrollbar(new_win, orient=tk.VERTICAL, command=tree.yview)
    xsb = ttk.Scrollbar(new_win, orient=tk.HORIZONTAL, command=tree.xview)
    tree['yscroll'] = ysb.set
    tree['xscroll'] = xsb.set
    ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
    xsb.grid(row=1, column=0, sticky=tk.E + tk.W)

    # Define o textos do cabeçalho (nome em maiúsculas)
    for c in dataCols:
        tree.heading(c, text=c.title())

    # Dados:
    data = [
        ("Argentina",      "Buenos Aires",     "ARS"),
        ("Australia",      "Canberra",         "AUD"),
        ("Brazil",         "Brazilia",         "BRL"),
        ("Canada",         "Ottawa",           "CAD"),
        ("China",          "Beijing",          "CNY"),
        ("France",         "Paris",            "EUR"),
        ("Germany",        "Berlin",           "EUR"),
        ("India",          "New Delhi",        "INR"),
        ("Italy",          "Rome",             "EUR"),
        ("Japan",          "Tokyo",            "JPY"),
        ("Mexico",         "Mexico City",      "MXN"),
        ("Russia",         "Moscow",           "RUB"),
        ("South Africa",   "Pretoria",         "ZAR"),
        ("United Kingdom", "London",           "GBP"),
        ("United States",  "Washington, D.C.", "USD"),
    ]

    # Insere cada item dos dados
    for item in data:
        tree.insert('', 'end', values=item)

    button_ok = tk.Button(new_win, text="OK", command=new_win.destroy)
    button_ok.grid(row=1, column=0, pady=5, sticky=tk.E)


novaJanela()
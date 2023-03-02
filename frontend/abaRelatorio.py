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
from tkcalendar import DateEntry

# https://pt.stackoverflow.com/questions/23053/ajuda-tables-python27 -> table
# https://www.plus2net.com/python/tkinter-OptionMenu.php -> choose

tree = None
register_db = None
client_db = None
cal_inicial = None
cal_final = None


def create_navigation(top_frame):
    global cal_inicial, cal_final
    SelectItem = tk.StringVar(top_frame)
    SelectItem.set(" ")  # default value

    label_funcionario = tk.Label(top_frame, text='Selec. o funcionário', width=20)
    label_funcionario.grid(row=0, column=0)

    lista_funcionarios = ["HTML", "PHP", "MySQL", "Python"]

    options = tk.OptionMenu(top_frame, SelectItem, *lista_funcionarios)
    options.grid(row=0, column=1)

    label_data_inicial = tk.Label(top_frame, text='Selec. data inicial', width=15)
    label_data_inicial.grid(row=0, column=2)

    cal_inicial = DateEntry(top_frame, selectmode='day', date_pattern='dd/mm/yyyy')
    cal_inicial.grid(row=0, column=3, padx=15)

    label_data_final = tk.Label(top_frame, text='Selec. data inicial', width=15)
    label_data_final.grid(row=0, column=4)

    cal_final = DateEntry(top_frame, selectmode='day', date_pattern='dd/mm/yyyy')
    cal_final.grid(row=0, column=5, padx=15)

    search_button = ttk.Button(top_frame, text="Pesquisar", command=search_date)
    search_button.grid(row=0, column=6, padx=15)

def search_date():
    selected_date = cal_inicial.get()
    print(selected_date)

def atualizar_table():
    global tree, register_db, client_db
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

    data = register_db.allRegister_tablePrint(client_db)

    print(data)

    #
    # Insere cada item dos dados
    for item in data:
        tree.insert('', 'end', values=item)

def create_table(center):
    global tree, register_db, client_db
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

    atualizar_table()

def novaJanela():
    global register_db, client_db
    new_win = tk.Toplevel()
    new_win.title("Relatório")

    password = "root"
    database = "project_rt"
    db = BancoDados(host="localhost", user="root", password=password, database=database)
    db.connect()
    client_db = Clientes_DB(db)
    register_db = Registro_DB(db)
    id_client = 2

    # layout all of the main containers
    new_win.grid_rowconfigure(1, weight=1)
    new_win.grid_columnconfigure(0, weight=1)

    #criar o frame central
    center = tk.Frame(new_win, width=50, height=40, padx=3, pady=3)
    center.grid(row=1, sticky="nsew")
    create_table(center)

    # criar o frame topo
    top_frame = tk.Frame(new_win, width=450, height=50, pady=3)
    top_frame.grid(row=0, sticky="ew")
    create_navigation(top_frame)

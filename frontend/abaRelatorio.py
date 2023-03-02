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

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('NOME', 'DATA', 'HORA', "CARGO")
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        xsb.grid(row=1, column=0, sticky=tk.E + tk.W)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:
        self.data = [
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

        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)


def aba_relatorio():
    root = tk.Tk()


    password = "root"
    database = "project_rt"
    db = BancoDados(host="localhost", user="root", password=password, database=database)
    db.connect()
    print(db.connection)
    client_db = Clientes_DB(db)
    register_db = Registro_DB(db)

    # new_cliente = Cliente("Marcos Cabrera Neto", "21951799", "2195", "2")
    # client_db.insertClient(new_cliente)

    id_client = client_db.getID_nameCLient("Marcos Cabrera Neto")

    # date_now = datetime.now()
    # new_register = Registro(id_client, date_now, "Entrada")
    # register_db.insertRegister(new_register)
    # print(register_db.lastRegister(id_client))

    app = Application(master=root)
    app.mainloop()

aba_relatorio()
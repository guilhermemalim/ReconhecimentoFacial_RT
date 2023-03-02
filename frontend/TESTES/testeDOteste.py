import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Relatórios')
root.geometry('{}x{}'.format(900, 700))
root.minsize(900, 700)
root.maxsize(900, 700)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# ================== frame center
# create frame center
topo = tk.Frame(root, bg='blue', width=900, height=20, padx=3, pady=3)

# topo.grid_rowconfigure(0, weight=1)                   #essa aq vai ser o quanto de linhas q tem no banco de dados
# topo.grid_columnconfigure(5, weight=1)                #essa aq vai ser o quanto de colunas q tem no banco de dados
#
# # ===============HEADER da tabela
# label_nome = tk.Label(topo, text='Nome', justify=tk.CENTER, width=40)
# label_data = tk.Label(topo, text='Data', justify=tk.CENTER, width=10)
# label_hora= tk.Label(topo, text='Hora', justify=tk.CENTER, width=10)
# label_cargo = tk.Label(topo, text='Cargo', justify=tk.CENTER, width=10)
#
# label_nome.grid(row=0, column=1, sticky=tk.W, padx=50, pady=5)
# label_data.grid(row=0, column=2, sticky=tk.W, padx=50, pady=5)
# label_hora.grid(row=0, column=3, sticky=tk.W, padx=50, pady=5)
# label_cargo.grid(row=0, column=4, sticky=tk.W, padx=50, pady=5)

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
            self.e.insert(END, lst[i][j])


lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

total_rows = len(lst)
total_columns = len(lst[0])

topo.grid(row=0, sticky="N")
#center = tk.Frame(root, bg='orange', width=900, height=20, padx=3, pady=3)
#center.grid(row=1, sticky="nsew")
t = Table(root, rows = 5, cols= 5)

root.mainloop()
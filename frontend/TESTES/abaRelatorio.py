import tkinter as tk

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
center = tk.Frame(root, bg='gray2', width=900, height=20, padx=3, pady=3)
center.grid(row=0, sticky="ew")

center.grid_rowconfigure(0, weight=1)                   #essa aq vai ser o quanto de linhas q tem no banco de dados
center.grid_columnconfigure(5, weight=1)                #essa aq vai ser o quanto de colunas q tem no banco de dados

# ===============HEADER da tabela
label_nome = tk.Label(center, text='Nome', justify=tk.CENTER, width=40)
label_data = tk.Label(center, text='Data', justify=tk.CENTER, width=10)
label_hora= tk.Label(center, text='Hora', justify=tk.CENTER, width=10)
label_cargo = tk.Label(center, text='Cargo', justify=tk.CENTER, width=10)

label_nome.grid(row=0, column=1, sticky=tk.W, padx=50, pady=5)
label_data.grid(row=0, column=2, sticky=tk.W, padx=50, pady=5)
label_hora.grid(row=0, column=3, sticky=tk.W, padx=50, pady=5)
label_cargo.grid(row=0, column=4, sticky=tk.W, padx=50, pady=5)


# ===============first linha
# create row
center1 = tk.Frame(root, bg='gray2', width=900, height=20, padx=3, pady=3)
center1.grid(row=1, sticky="ew")

center1.grid_rowconfigure(0, weight=1)                   #essa aq vai ser o quanto de linhas q tem no banco de dados
center1.grid_columnconfigure(5, weight=1)                #essa aq vai ser o quanto de colunas q tem no banco de dados


label_nome1 = tk.Label(center1, text='Maattheus smith', width=40)
label_data1 = tk.Label(center1, text='01/03/2023', width=10)
label_hora1= tk.Label(center1, text='20:25', width=10)
label_cargo1 = tk.Label(center1, text='Normal', width=10)

label_nome1.grid(row=0, column=1, sticky=tk.EW, padx=50, pady=5)
label_data1.grid(row=0, column=2, sticky=tk.EW, padx=50, pady=5)
label_hora1.grid(row=0, column=3, sticky=tk.EW, padx=50, pady=5)
label_cargo1.grid(row=0, column=4, sticky=tk.EW, padx=50, pady=5)

root.mainloop()
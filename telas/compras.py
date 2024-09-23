import tkinter as tk
from colors import compras
from database.tables.compras import nova_lista_de_compras, all_listas,listas_de_compras

def gerar_lista(root):
    nova_lista_de_compras()
    listar_compras(root)


def listar_compras(root):
    global listas_de_compras
    listas= listas_de_compras
    for widgets in root.winfo_children():
        widgets.destroy()

    for index,lista in enumerate(listas):  
        label=tk.Label(root,text=lista['data'])
        label_total=tk.Label(root,text= f'R$: {lista['total']:.2f}')
        button_detalhes=tk.Button(root,text='detalhes')

        label.grid(row=index,column=0)
        label_total.grid(row=index,column=1)
        button_detalhes.grid(row=index,column=2)

def frame_compras(root):
    all_listas()
    frame=tk.Frame(root,background=compras)
    frame_listas=tk.Frame(frame)
    button_nova_lista=tk.Button(frame,text='gerar lista',command=lambda:gerar_lista(frame_listas))
    listar_compras(frame_listas)

    button_nova_lista.grid(row=0,column=0,sticky='w')
    frame_listas.grid(row=1,column=0,sticky='wesn')

    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    return frame

import tkinter as tk
import colors
from telas.vendas import frame_vendas
from telas.compras import frame_compras
from telas.pedidos import frame_pedidos
from telas.relatorios import frame_relatorios

def tela(root):
    frame_menus=tk.Frame(root,width=600)
    vendas=tk.Button(frame_menus,text="vendas",background=colors.vendas,command=lambda:f1.tkraise())
    compras=tk.Button(frame_menus,text="compras",background=colors.compras,command=lambda:f2.tkraise())
    pedidos=tk.Button(frame_menus,text="pedidos",background=colors.pedidos,command=lambda:f3.tkraise())
    relatorios=tk.Button(frame_menus,text="relatorios",background=colors.relatorios,command=lambda:f4.tkraise())

    f1 = frame_vendas(root)
    f2 = frame_compras(root)
    f3 = frame_pedidos(root)
    f4 = frame_relatorios(root)

    for frame in (f1, f2, f3, f4):
        frame.grid(row=1, column=0,columnspan=4, sticky='news')

    f1.tkraise()

    frame_menus.grid(row=0,column=0,columnspan=8,sticky="we")
    vendas.grid(column=0,row=0)
    compras.grid(column=1,row=0)
    pedidos.grid(column=2,row=0)
    relatorios.grid(column=3,row=0)
    return frame_menus
    
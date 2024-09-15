import tkinter as tk
from tela import tela

def menus(root):
    frame_menus=tk.Frame(root,background="yellow",width=100)
    
    vendas=tk.Button(frame_menus,text="vendas",background="#D8BFD8")
    compras=tk.Button(frame_menus,text="compras",background="#FFE4C4")
    pedidos=tk.Button(frame_menus,text="pedidos",background="blue")
    relatorios=tk.Button(frame_menus,text="resumo",background="purple")
    tela(frame_menus)

    frame_menus.grid(row=0,column=0)

    vendas.grid(column=0,row=0)
    compras.grid(column=1,row=0)
    pedidos.grid(column=2,row=0)
    relatorios.grid(column=3,row=0)
    return frame_menus
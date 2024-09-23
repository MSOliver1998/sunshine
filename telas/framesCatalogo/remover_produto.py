import tkinter as tk
from database.tables.produtos import del_prod, lista_de_produtos
from widgets.menu_option import menu_option
from widgets.options import *

def remover_produto(prod):
    del_prod(prod)
    change_options()

def frame_remover_produto(frame_catalogo):
    frame=tk.Frame(frame_catalogo)
    opcoes = ["selecionar"]

    global lista_de_produtos
    global options

    for i in lista_de_produtos:
        opcoes.append(i['nome'])

    menu,selecao=menu_option(frame)
    
    label_produtos=tk.Label(frame,text='produto')
    menu_opcoes = menu
    options.append(menu_opcoes)
    button_deletar=tk.Button(frame,text='Excluir',background='red',command=lambda:remover_produto(selecao.get()))

    label_produtos.grid(row=0,column=0)
    menu_opcoes.grid(row=1,column=0)
    button_deletar.grid(row=1,column=1)

    return frame


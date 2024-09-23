import tkinter as tk
from tkinter import ttk
from database.tables.catalogo import lista_de_produtos

def update_menu_option(option_menu):
        opcoes=['selecionar']
        lista=lista_de_produtos
        for i in lista:
            opcoes.append(i['nome'])
        opcao_selecionada = tk.StringVar()
        opcao_selecionada.set(opcoes[0])
        menu = option_menu["menu"]
        menu.delete(0, "end")
        for item in opcoes:
            menu.add_command(label=item,  command=lambda value=item: option_menu.setvar(option_menu.cget("textvariable"), value))


def menu_option(frame):
    opcao_selecionada=tk.StringVar(frame)
    opcoes=['selecionar']

    lista=lista_de_produtos
    for item in lista:
         opcoes.append(item['nome'])
   
    menu_option=ttk.OptionMenu(frame,opcao_selecionada,opcoes[0],*opcoes)

    return menu_option,opcao_selecionada

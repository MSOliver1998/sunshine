import tkinter as tk
from widgets.menu_option import *
from widgets.options import *
from database.tables.catalogo import lista_de_produtos
from widgets.descontos import adicionar_desconto

def confirmar(frame):
    valores = []
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry) and widget.get():
            valores.append(widget.get())
    print("Valores confirmados:", valores)

def editar_produto(frame,prod):
    print(prod)
    global lista_de_produtos

    for widget in frame.winfo_children():
            widget.destroy()

    for item in lista_de_produtos:
        if item['nome']== prod:
            label_produto=tk.Label(frame,text='PRODUTO')
            entry_nome=tk.Entry(frame)
            entry_nome.insert(0,item['nome'])
            label_preco=tk.Label(frame,text='PREÇO')
            entry_preco=tk.Entry(frame)
            entry_preco.insert(0,item['preço'])
            button_adicionar = tk.Button(frame, text='+', background='green', command=lambda: adicionar_desconto(frame))
            button_confirmar=tk.Button(frame,text='confirmar',background='green',command=lambda: confirmar(frame))

            label_produto.grid(row=0,column=0)
            entry_nome.grid(row=1,column=0)
            label_preco.grid(row=0,column=1)
            entry_preco.grid(row=1,column=1)
            button_adicionar.grid(row=20,column=0)
            button_confirmar.grid(row=20,column=1)

            if len(item['desconto'])>0:
                row=3
                label_quantidade=tk.Label(frame,text='QTD')
                label_valor=tk.Label(frame,text='PREÇO')
                label_quantidade.grid(row=2,column=0)
                label_valor.grid(row=2,column=1)

                for key,value in item['desconto'].items():
                    entry_quantidade=tk.Entry(frame,width=8)
                    entry_quantidade.insert(0,f'{key}')
                    entry_valor=tk.Entry(frame,width=8)
                    entry_valor.insert(0,f'{value}')
                    button_excluir=tk.Button(frame,text='-',background='red')

                    def excluir(entry_quantidade=entry_quantidade, entry_valor=entry_valor, button_excluir=button_excluir):
                        entry_quantidade.destroy()
                        entry_valor.destroy()
                        button_excluir.destroy()

                    button_excluir.config(command=excluir)

                    entry_quantidade.grid(row=row,column=0)
                    entry_valor.grid(row=row,column=1)
                    button_excluir.grid(row=row,column=2)
                    row+=1


def frame_editar_produto(root):

    frame=tk.Frame(root)
    menu_opt,selecao=menu_option(frame)
    menu=menu_opt
    options.append(menu)
    button_editar=tk.Button(frame,text='editar',background='yellow',command=lambda:editar_produto(frame_produto,selecao.get()))
    frame_produto=tk.Frame(frame)

    menu.grid(row=0,column=0)
    button_editar.grid(row=0,column=1)
    frame_produto.grid(row=1,column=0,columnspan=6)

    return  frame


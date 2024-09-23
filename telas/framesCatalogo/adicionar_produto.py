import tkinter as tk
from database.tables.produtos import *
from widgets.options import *

descontos_entries=[]
row=3

def criar_produto(produto):

    global lista_de_produtos

    produto['desconto']={

    }
    if len(descontos_entries)>0:
        for entries in descontos_entries:
            produto['desconto'][entries[0].get()]=float(entries[1].get())
    
    add_prod(produto)
    change_options()
        
def adicionar_desconto(frame_desconto,botao_desconto):
    global row
    row=row
    root=frame_desconto

    entry_quantidade=tk.Entry(root,width=4)
    entry_valor=tk.Entry(root,width=8)

    entry_quantidade.grid(row=row,column=0)
    entry_valor.grid(row=row,column=1)
    
    botao_desconto[0].grid(row=row+1,column=0)
    botao_desconto[1].grid(row=row+1,column=1)

    entries=[entry_quantidade,entry_valor]
    descontos_entries.append(entries)

    row+=1

def frame_adicionar_produto(frame_desconto):

    frame=tk.Frame(frame_desconto)

    label_nome=tk.Label(frame,text='Nome')
    entry_nome=tk.Entry(frame)

    label_preco=tk.Label(frame,text='Preço')
    entry_preco=tk.Entry(frame)

    label_quantidade=tk.Label(frame,text="Quantidade")
    label_valor=tk.Label(frame,text='Preço')

    button_novo_desconto=tk.Button(frame,text='+',command=lambda:adicionar_desconto(frame,[button_novo_desconto,button_finalizar]))
    button_finalizar=tk.Button(frame,text="finalizar",command=lambda: criar_produto({'nome':entry_nome.get(),'preço':float(entry_preco.get())}))

    label_nome.grid(row=0,column=0)
    entry_nome.grid(row=1,column=0)

    label_preco.grid(row=0,column=1)
    entry_preco.grid(row=1,column=1)

    label_valor.grid(row=2,column=1)
    label_quantidade.grid(row=2,column=0)

    button_novo_desconto.grid(row=row+1,column=0)
    button_finalizar.grid(row=row+1,column=1)

    return frame
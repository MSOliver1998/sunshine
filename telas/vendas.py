import tkinter as tk
from database.produtos import produtos as dt
from database.crud import *
from colors import vendas
from tkinter import ttk
from functions import *
from lista import *

def frame_vendas(root):
    def selecionar_opcao():
        quantidade = entry_unidades.get()
        prod=opcao_selecionada.get()
        preco=checar_valor_database(prod,quantidade)
        if(len(lista)==0):
            lista.append({
                "nome":prod,
                "quantidade":int(quantidade),
                "preço": preco
            })
        else:
            find=-1
            for index,produto in enumerate(lista):
                if(produto['nome']==prod):
                    find=int(index)
                    lista[index]['quantidade']+= int(quantidade)
                    lista[index]['preço']=checar_valor_database(prod,lista[index]['quantidade'])
                    break
                
            if(find==-1):
                lista.append({
                    "nome":prod,
                    "quantidade":int(quantidade),
                    'preço': preco
                })
        listar_produtos(root,lista)

    lista=[]
    opcoes = ["selecionar"]

    for i in dt:
        opcoes.append(i['nome'])

    opcao_selecionada = tk.StringVar()
    opcao_selecionada.set(opcoes[0])
    frame=tk.Frame(root,background=vendas,height=600,width=600)
    label_unidades=tk.Label(frame,text="unidades",background=vendas)
    entry_unidades=tk.Entry(frame,width=10)
    label_produto=tk.Label(frame,text="produto",width=20)
    menu_opcoes = ttk.OptionMenu(frame, opcao_selecionada, *opcoes)
    botao_adicionar=tk.Button(frame,text='+',background="#7CFC00",foreground="#98FB98",command=selecionar_opcao)
    botao_finalizar=tk.Button(frame,text="finalizar",background='#B0E0E6')

    label_unidades.grid(row=0,column=0)
    entry_unidades.grid(row=1,column=0)

    label_produto.grid(row=0,column=1)
    menu_opcoes.grid(row=1,column=1)

    botao_adicionar.grid(row=1,column=2)
    botao_finalizar.grid(row=1,column=3)

    return frame
